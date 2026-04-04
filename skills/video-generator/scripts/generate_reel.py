#!/usr/bin/env python3
"""
Generate a cinematic reel from source stills using Kling AI image-to-video,
then stitch all clips into a single final MP4.

Pipeline:
  1. Submit all shots to Kling image2video simultaneously
  2. Poll all tasks in parallel until complete
  3. Download each clip
  4. Trim each clip to its target duration
  5. Stitch clips into the final reel (ffmpeg preferred, OpenCV fallback)

Output: skills/video-generator/output/marrakech_reel_ai.mp4

Usage:
  python3 generate_reel.py                  # std mode, 5s clips
  python3 generate_reel.py --mode pro       # pro mode for better quality
  python3 generate_reel.py --stitch-only    # skip generation, stitch existing clips
  python3 generate_reel.py --no-stitch      # generate clips only, skip final stitch
"""

import os
import sys
import json
import time
import hmac
import hashlib
import base64
import argparse
import requests
import threading
import subprocess
import shutil
from pathlib import Path
from dotenv import load_dotenv

# ── Environment ───────────────────────────────────────────────────────────────

load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")

ACCESS_KEY = os.environ.get("KLING_API_KEY")
SECRET_KEY = os.environ.get("KLING_SECRET_KEY")

if not ACCESS_KEY or not SECRET_KEY:
    print("Error: KLING_API_KEY and KLING_SECRET_KEY must be set in .env", file=sys.stderr)
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

BASE_URL      = "https://api.klingai.com"
MODEL         = "kling-v1-6"
POLL_INTERVAL = 15
MAX_WAIT      = 600   # 10 min per task

ROOT       = Path(__file__).parent.parent.parent.parent
ASSETS     = ROOT / "assets/moodboard/video_reels"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
CLIPS_DIR  = OUTPUT_DIR / "clips_marrakech"
FINAL_OUT  = OUTPUT_DIR / "marrakech_reel_ai.mp4"

# ── Shot Deck ─────────────────────────────────────────────────────────────────
#
# Each entry: (filename, target_duration_s, prompt, negative_prompt)
#
# target_duration_s: how long this shot lasts in the final reel
# Kling generates 5s clips — we trim to target_duration in post

_NEG = (
    "text, logos, looking at camera, forced smile, posed, stock photo, "
    "cold light, HDR, modern elements, tour group, selfie, guidebook visible, "
    "tourist pose, airbrushed skin, phone in hand"
)

SHOTS = [
    # ── Shot 1 — G — Hook: overhead descent (1.5s) ──────────────────────────
    (
        "hf_20260401_130307_64273041-10a1-41a2-b081-1f297a89792e.png",
        1.5,
        (
            "Starting from a perfect 90-degree overhead bird's-eye view looking straight down "
            "onto a Marrakech medina souk cobblestone floor, the camera performs an extremely "
            "slow smooth vertical descent — as if gently falling from directly above, dropping "
            "approximately 30% closer to the subject over 5 seconds. The woman in white wide-leg "
            "linen trousers and orange crossbody bag remains centered in the frame throughout. "
            "Her white outfit is the anchor point against the dark cobblestone and surrounding "
            "colorful spice barrels. Very subtle life — a barely perceptible sway of a hanging "
            "fabric at the upper frame edge. Warm amber and golden market light. Kodak Portra 400 "
            "film grain. The descent feels like gravity made graceful."
        ),
        _NEG,
    ),
    # ── Shot 2 — B — World: wide corridor pan (2.0s) ────────────────────────
    (
        "hf_20260401_130306_25911b77-fe5c-4615-b3f3-14555d6ad700.png",
        2.0,
        (
            "Eye-level shot of a full Marrakech medina souk corridor. The woman in white wide-leg "
            "trousers and orange crossbody bag stands mid-figure in the alley. Colorful textiles "
            "hang overhead, spice trays and lanterns flank both sides of the cobblestone corridor. "
            "The camera performs a slow smooth horizontal pan from left to right following the "
            "direction of the warm golden light entering from the left. Pan speed: the frame moves "
            "approximately 4-5% of its width over 5 seconds — imperceptible as movement, felt as "
            "life. The hanging textiles sway imperceptibly — a single breath of warm air. The "
            "woman's weight shifts very slightly, completely natural. A blurred figure passes "
            "at the far end of the corridor. Warm golden hour light, film grain throughout."
        ),
        _NEG,
    ),
    # ── Shot 3 — I — Emotional peak: back shot push into amber (2.5s) ───────
    (
        "hf_20260401_130307_888fd39e-a2d9-43f2-9ec5-ed65eac50708.png",
        2.5,
        (
            "The woman in white stands with her back to the camera, facing a Marrakech medina "
            "market stall that radiates warm amber light — lanterns glowing deep orange, spice "
            "pyramids catching the warmth, shelves packed with crafts lit from within. The camera "
            "performs the slowest possible push-in: a smooth barely-there forward dolly move, "
            "closing approximately 5-8% of the distance over 5 seconds. Her breathing is visible — "
            "the back of her white top rises and falls once slowly. Her orange crossbody bag hangs "
            "with the faintest pendulum micro-sway. Her hair drifts slightly from a gentle warm air "
            "current rising from the stall. The amber light from the stall flickers once at the "
            "2-second mark — a single candle flutter. Everything else is completely still. "
            "Warm, glowing, intimate, painterly. This is the emotional center of the reel."
        ),
        _NEG,
    ),
    # ── Shot 4 — E — Immersion: zoom toward lanterns (2.0s) ─────────────────
    (
        "hf_20260401_130306_c9172f5a-530e-432d-b330-f7c92c109f08.png",
        2.0,
        (
            "A richly lit Marrakech spice market stall — the warmest most amber frame in the "
            "sequence. Hanging mosaic lanterns dominate the upper left, glowing deep orange and "
            "gold. Spice pyramids below in saffron yellow, paprika red, cumin brown. The woman "
            "in white leans toward the spice display. The camera performs a slow zoom-in toward "
            "the lantern cluster upper-left — a 1.0x to 1.12x move over 5 seconds, smooth and "
            "continuous. The lanterns sway once — a single pendulum beat at 1 second. Micro "
            "sparkles within the mosaic glass as the angle shifts imperceptibly. The warm amber "
            "light pulses imperceptibly — breathing rather than flickering. Film grain adds "
            "texture to the shadows. The entire frame feels bathed in warm oil."
        ),
        _NEG,
    ),
    # ── Shot 5 — D — Build: mid eye-level touch (1.5s) ──────────────────────
    (
        "hf_20260401_130306_489b2b66-7b70-43f9-9d2b-3d39bc423836.png",
        1.5,
        (
            "Mid eye-level candid moment in a Marrakech medina souk. The woman in white wide-leg "
            "linen outfit and orange crossbody bag leans forward, her fingertips about to touch "
            "the turmeric powder on a spice display tray. Her body language is curious and "
            "unhurried — completely present in the moment. Mosaic lanterns hang glowing warm "
            "amber to the left. Warm golden side light illuminates her face and the spice colors "
            "simultaneously. The camera performs a gentle slow zoom-in over 5 seconds. The spice "
            "tray shows perfectly arranged color stripes: turmeric yellow, paprika orange, chili "
            "red, cumin brown. Natural warm skin tones, Kodak Portra 400 film grain."
        ),
        _NEG,
    ),
    # ── Shot 6 — C — Rhythm break: overhead tilt reveal (2.0s) ──────────────
    (
        "hf_20260401_130306_3855d97e-21d1-4991-8727-0d6f5b4c9cb9.png",
        2.0,
        (
            "Return to the overhead perspective — bird's-eye view from directly above the "
            "Marrakech souk. The woman in white is positioned at the left third of the frame "
            "reaching toward a spice display that creates a graphic horizontal stripe pattern: "
            "turmeric yellow, saffron orange, paprika red, cumin brown, dried herb green. "
            "The camera performs a slow tilt — the overhead camera nods forward 3 degrees over "
            "5 seconds — revealing more of the spice stripe pattern below her. The cobblestone "
            "floor recedes slightly. Her white figure becomes smaller relative to the colorful "
            "abundance surrounding her. She is a detail in a larger painting. A single spice "
            "vendor's hand appears at the far edge of frame at 2 seconds, adjusting a container. "
            "A hanging fabric at the upper-left edge drifts a centimeter. Graphic, abstract."
        ),
        _NEG,
    ),
    # ── Shot 7 — K — Close: corridor push, she belongs (3.5s) ───────────────
    (
        "hf_20260401_130307_af7e1e34-c0b7-4f9d-8671-06a7b65120f4.png",
        3.5,
        (
            "The closing shot — the widest eye-level view of the full Marrakech souk corridor. "
            "The woman in white stands mid-left in the cobblestone alley, arm extended mid-reach "
            "toward the spice display, her pose the most relaxed of the sequence. The souk "
            "stretches behind her: warm bokeh figures in the distance, hanging textiles and "
            "lanterns receding into a warm golden blur at the vanishing point. The camera "
            "performs its slowest push-in — a forward dolly from 1.0x to 1.08x over 5 seconds, "
            "so slow it reads as the world breathing inward around her. At 1 second: a blurred "
            "figure passes deep in the background corridor. At 2 seconds: hanging textiles drift "
            "once — the slowest possible pendulum, one complete breath. At 3 seconds: she shifts "
            "her weight — a micro-movement of the hip, her bag swings half a centimeter and stops. "
            "She settles. She belongs. Final frame: complete stillness. The souk surrounds her. "
            "This is not a destination. This is a connection."
        ),
        _NEG,
    ),
]

# ── JWT Auth ──────────────────────────────────────────────────────────────────

def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def _jwt() -> str:
    header  = {"alg": "HS256", "typ": "JWT"}
    now     = int(time.time())
    payload = {"iss": ACCESS_KEY, "exp": now + 1800, "nbf": now - 5}
    h = _b64url(json.dumps(header,  separators=(",", ":")).encode())
    p = _b64url(json.dumps(payload, separators=(",", ":")).encode())
    sig = hmac.new(SECRET_KEY.encode(), f"{h}.{p}".encode(), hashlib.sha256).digest()
    return f"{h}.{p}.{_b64url(sig)}"

def _headers() -> dict:
    return {"Authorization": f"Bearer {_jwt()}", "Content-Type": "application/json"}

# ── Image Encoding ────────────────────────────────────────────────────────────

def _encode_image(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Source image not found: {path}")
    return base64.b64encode(path.read_bytes()).decode()

# ── API ───────────────────────────────────────────────────────────────────────

def _submit(image_b64: str, prompt: str, negative: str, duration: int, mode: str) -> str:
    """Submit an image2video task. Returns task_id."""
    url  = f"{BASE_URL}/v1/videos/image2video"
    body = {
        "model_name":      MODEL,
        "image":           image_b64,
        "prompt":          prompt,
        "negative_prompt": negative,
        "cfg_scale":       0.5,
        "mode":            mode,
        "duration":        str(duration),
    }
    wait = 10
    for attempt in range(5):
        resp = requests.post(url, headers=_headers(), json=body, timeout=60)
        if resp.status_code == 429:
            try:
                err  = resp.json()
                code = err.get("code")
                msg  = err.get("message", "unknown")
                if code == 1102:
                    raise RuntimeError(
                        f"Kling account balance is empty (code {code}: {msg}). "
                        "Top up at https://klingai.com to generate videos."
                    )
            except (ValueError, KeyError):
                pass
            print(f"    Rate limited — retrying in {wait}s...", flush=True)
            time.sleep(wait)
            wait *= 2
            continue
        if not resp.ok:
            try:
                body_err = resp.json()
            except Exception:
                body_err = resp.text
            raise RuntimeError(f"Kling API {resp.status_code}: {body_err}")
        data = resp.json()
        if data.get("code") != 0:
            raise RuntimeError(f"Kling API error: {data.get('message', data)}")
        return data["data"]["task_id"]
    raise RuntimeError("Rate limit persisted after 5 retries.")


def _poll(task_id: str, label: str) -> str:
    """
    Poll task until complete. Returns the video URL.
    Runs in a background thread — results written to shared dict.
    """
    url   = f"{BASE_URL}/v1/videos/image2video/{task_id}"
    start = time.time()
    print(f"  [{label}] Polling {task_id[:8]}...", flush=True)

    while True:
        elapsed = time.time() - start
        if elapsed > MAX_WAIT:
            raise TimeoutError(f"[{label}] Timed out after {int(elapsed)}s")

        resp = requests.get(url, headers=_headers(), timeout=30)
        resp.raise_for_status()
        data   = resp.json()
        if data.get("code") != 0:
            raise RuntimeError(f"[{label}] Polling error: {data.get('message', data)}")

        task   = data["data"]
        status = task.get("task_status", "")

        if status == "succeed":
            videos = task.get("task_result", {}).get("videos", [])
            if not videos:
                raise RuntimeError(f"[{label}] No videos in result")
            url_out = videos[0]["url"]
            print(f"  [{label}] Done ({int(elapsed)}s) ✓", flush=True)
            return url_out

        if status == "failed":
            msg = task.get("task_status_msg", "unknown")
            raise RuntimeError(f"[{label}] Task failed: {msg}")

        time.sleep(POLL_INTERVAL)


def _download(url: str, dest: Path) -> None:
    resp = requests.get(url, stream=True, timeout=120)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

# ── Stitch ────────────────────────────────────────────────────────────────────

def _stitch_ffmpeg(clip_paths: list[Path], durations: list[float], output: Path) -> bool:
    """
    Trim each clip to its target duration and concat with ffmpeg.
    Returns True if successful, False if ffmpeg not available.
    """
    if not shutil.which("ffmpeg"):
        return False

    concat_file = CLIPS_DIR / "concat.txt"
    trimmed     = []

    for i, (clip, dur) in enumerate(zip(clip_paths, durations)):
        trimmed_path = CLIPS_DIR / f"trimmed_{i+1:02d}.mp4"
        cmd = [
            "ffmpeg", "-y", "-i", str(clip),
            "-t", str(dur),
            "-c", "copy",
            str(trimmed_path),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        trimmed.append(trimmed_path)

    with open(concat_file, "w") as f:
        for p in trimmed:
            f.write(f"file '{p.resolve()}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(output),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return True


def _stitch_opencv(clip_paths: list[Path], durations: list[float], output: Path) -> None:
    """OpenCV fallback: decode each clip, keep only target frames, write final."""
    try:
        import cv2
        import numpy as np
    except ImportError:
        print("Error: neither ffmpeg nor opencv-python is available for stitching.", file=sys.stderr)
        sys.exit(1)

    FPS    = 24
    W, H   = 1080, 1920
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(output), fourcc, FPS, (W, H))

    for clip, dur in zip(clip_paths, durations):
        cap        = cv2.VideoCapture(str(clip))
        src_fps    = cap.get(cv2.CAP_PROP_FPS) or 24
        keep       = int(dur * FPS)
        src_keep   = int(dur * src_fps)
        frame_idx  = 0

        while frame_idx < src_keep:
            ret, frame = cap.read()
            if not ret:
                break
            # Resize / crop to 1080×1920 if needed
            fh, fw = frame.shape[:2]
            if fw != W or fh != H:
                scale = H / fh
                nw    = int(fw * scale)
                frame = cv2.resize(frame, (nw, H), interpolation=cv2.INTER_LANCZOS4)
                fh2, fw2 = frame.shape[:2]
                if fw2 > W:
                    xs    = (fw2 - W) // 2
                    frame = frame[:, xs:xs + W]
                elif fw2 < W:
                    pad   = (W - fw2) // 2
                    frame = cv2.copyMakeBorder(frame, 0, 0, pad, W - fw2 - pad,
                                               cv2.BORDER_CONSTANT, value=0)
            # Resample to output FPS if source FPS differs
            out_frame = int(frame_idx * FPS / src_fps)
            for _ in range(max(1, out_frame - (frame_idx - 1))):
                writer.write(frame)
            frame_idx += 1

        cap.release()

    writer.release()

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate + stitch a Kling AI video reel")
    parser.add_argument("--mode",        default="std", choices=["std", "pro"],
                        help="Kling generation mode (default: std)")
    parser.add_argument("--duration",    default=5,     type=int, choices=[5, 10],
                        help="Clip duration per shot in seconds (default: 5)")
    parser.add_argument("--stitch-only", action="store_true",
                        help="Skip generation — stitch existing clips in clips_marrakech/")
    parser.add_argument("--no-stitch",   action="store_true",
                        help="Generate clips only, skip final stitch")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CLIPS_DIR.mkdir(parents=True, exist_ok=True)

    targets   = [s[1] for s in SHOTS]
    clip_paths = [CLIPS_DIR / f"shot_{i+1:02d}.mp4" for i in range(len(SHOTS))]

    # ── Step 1: Generation ────────────────────────────────────────────────────
    if not args.stitch_only:
        total_cost = len(SHOTS) * (0.42 if args.mode == "pro" else 0.14)
        print(f"\nReel generator — {len(SHOTS)} shots — {sum(targets):.1f}s total")
        print(f"Mode: {args.mode} | Clip duration: {args.duration}s | Est. cost: ~${total_cost:.2f}")
        print(f"Source: {ASSETS}")
        print(f"Clips:  {CLIPS_DIR}\n")

        # Encode all images first
        print("Encoding source images...")
        encoded = []
        for i, (filename, _, _, _) in enumerate(SHOTS, 1):
            path = ASSETS / filename
            enc  = _encode_image(path)
            encoded.append(enc)
            print(f"  Shot {i}: {filename[:40]}")

        # Submit all tasks
        print(f"\nSubmitting {len(SHOTS)} image2video tasks...")
        task_ids = []
        for i, ((filename, _, prompt, neg), enc) in enumerate(zip(SHOTS, encoded), 1):
            task_id = _submit(enc, prompt, neg, args.duration, args.mode)
            task_ids.append(task_id)
            print(f"  Shot {i}/{len(SHOTS)} submitted: {task_id}")
            if i < len(SHOTS):
                time.sleep(1)  # brief pause between submits

        # Poll all tasks in parallel
        print(f"\nPolling {len(SHOTS)} tasks in parallel...")
        results = {}
        errors  = {}
        lock    = threading.Lock()

        def poll_worker(idx, task_id, label):
            try:
                url = _poll(task_id, label)
                with lock:
                    results[idx] = url
            except Exception as e:
                with lock:
                    errors[idx] = str(e)

        threads = []
        for i, task_id in enumerate(task_ids):
            label = f"Shot {i+1}"
            t = threading.Thread(target=poll_worker, args=(i, task_id, label), daemon=True)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        if errors:
            for idx, msg in errors.items():
                print(f"  ERROR Shot {idx+1}: {msg}", file=sys.stderr)
            sys.exit(1)

        # Download clips
        print(f"\nDownloading {len(results)} clips...")
        for i in sorted(results.keys()):
            dest = clip_paths[i]
            print(f"  Shot {i+1} → {dest.name} ...", end="", flush=True)
            _download(results[i], dest)
            size = dest.stat().st_size / (1024 * 1024)
            print(f" {size:.1f}MB")

    # ── Step 2: Stitch ────────────────────────────────────────────────────────
    if not args.no_stitch:
        # Verify all clips exist
        missing = [p for p in clip_paths if not p.exists()]
        if missing:
            print(f"\nMissing clips (run without --stitch-only first):", file=sys.stderr)
            for p in missing:
                print(f"  {p}", file=sys.stderr)
            sys.exit(1)

        print(f"\nStitching {len(clip_paths)} clips → {FINAL_OUT.name} ...")

        ok = _stitch_ffmpeg(clip_paths, targets, FINAL_OUT)
        if not ok:
            print("  ffmpeg not found — using OpenCV fallback...")
            _stitch_opencv(clip_paths, targets, FINAL_OUT)

        size = FINAL_OUT.stat().st_size / (1024 * 1024)
        print(f"\nDone. {size:.1f}MB → {FINAL_OUT}")
        print(f"\nInstall ffmpeg for better stitching quality:")
        print(f"  brew install ffmpeg")

    print("\nShot clips saved to:")
    for i, p in enumerate(clip_paths):
        if p.exists():
            print(f"  Shot {i+1}: {p}")


if __name__ == "__main__":
    main()
