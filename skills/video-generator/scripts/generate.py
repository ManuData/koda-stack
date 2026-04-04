#!/usr/bin/env python3
"""
Generate videos via Kling AI API.

Usage:
  # From an art-direction .md file (reads Generation Prompt + Negative prompt):
  python3 scripts/generate.py --visual visuals/art-direction-bali-coffee-solo.md

  # Image-to-video (first frame input):
  python3 scripts/generate.py --visual visuals/video-prompt-marrakech-souk-reel.md \
    --image assets/moodboard/video_reels/hf_20260401_130307_64273041.png

  # Plain text prompt:
  python3 scripts/generate.py "slow overhead descent into Marrakech souk, cinematic"

  # Full JSON control:
  python3 scripts/generate.py '{"prompt": "...", "negative": "...", "duration": 5, "mode": "pro"}'
"""

import sys
import os
import json
import re
import time
import hmac
import hashlib
import base64
import argparse
import requests
from pathlib import Path

# ── Environment ───────────────────────────────────────────────────────────────

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")

ACCESS_KEY = os.environ.get("KLING_API_KEY")
SECRET_KEY = os.environ.get("KLING_SECRET_KEY")

if not ACCESS_KEY or not SECRET_KEY:
    print(
        "Error: KLING_API_KEY and KLING_SECRET_KEY must be set in your .env file.",
        file=sys.stderr,
    )
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

BASE_URL     = "https://api.klingai.com"
MODEL        = "kling-v1-6"
POLL_INTERVAL = 15   # seconds between status checks
MAX_WAIT      = 600  # 10 minutes max per task

OUTPUT_DIR = Path(__file__).parent.parent / "output"

# ── JWT Auth ──────────────────────────────────────────────────────────────────

def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

def generate_jwt() -> str:
    """Generate a HS256 JWT token for Kling API authentication."""
    header  = {"alg": "HS256", "typ": "JWT"}
    now     = int(time.time())
    payload = {"iss": ACCESS_KEY, "exp": now + 1800, "nbf": now - 5}

    header_enc  = _b64url(json.dumps(header,  separators=(",", ":")).encode())
    payload_enc = _b64url(json.dumps(payload, separators=(",", ":")).encode())
    signing_input = f"{header_enc}.{payload_enc}"

    sig = hmac.new(
        SECRET_KEY.encode("utf-8"),
        signing_input.encode("utf-8"),
        hashlib.sha256,
    ).digest()

    return f"{signing_input}.{_b64url(sig)}"

def _headers() -> dict:
    return {
        "Authorization": f"Bearer {generate_jwt()}",
        "Content-Type":  "application/json",
    }

# ── Markdown Parser ───────────────────────────────────────────────────────────

def extract_from_brief(md_path: Path) -> tuple[str, str]:
    """
    Extract prompt and negative prompt from an art-direction .md file.
    Checks for ## Video Prompt first, then falls back to ## Generation Prompt.
    Compatible with all existing art-direction files in visuals/.
    """
    text = md_path.read_text(encoding="utf-8")

    # Priority 1: ## Video Prompt section (video-specific overrides)
    video_section = re.search(r"## Video Prompt.*?```(.*?)```", text, re.DOTALL)
    if video_section:
        prompt = video_section.group(1).strip()
        neg = re.search(
            r"\*\*Negative prompt.*?\*\*\W*```(.*?)```",
            text[video_section.end():], re.DOTALL
        )
        return prompt, neg.group(1).strip() if neg else ""

    # Priority 2: ## Generation Prompt (same as image-ad-generator)
    gen_section = re.search(r"## Generation Prompt.*?```(.*?)```", text, re.DOTALL)
    if gen_section:
        prompt = gen_section.group(1).strip()
        neg = re.search(r"\*\*Negative prompt.*?\*\*\W*```(.*?)```", text, re.DOTALL)
        return prompt, neg.group(1).strip() if neg else ""

    raise ValueError(
        f"No prompt found in {md_path}.\n"
        "Expected a '## Video Prompt' or '## Generation Prompt' section."
    )

# ── Image Encoding ────────────────────────────────────────────────────────────

def encode_image(image_path: str) -> str:
    """
    Encode a local image file to a base64 data URI.
    Also accepts an http/https URL — returned as-is.
    """
    if image_path.startswith(("http://", "https://")):
        return image_path

    path = Path(image_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    suffix = path.suffix.lower()
    mime = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }.get(suffix, "image/jpeg")

    b64 = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# ── API Calls ─────────────────────────────────────────────────────────────────

def _post_with_retry(url: str, body: dict, retries: int = 4) -> dict:
    """POST with exponential backoff on 429 rate-limit responses."""
    wait = 10
    for attempt in range(retries):
        resp = requests.post(url, headers=_headers(), json=body, timeout=30)
        if resp.status_code == 429:
            # Kling uses 429 for both rate limits AND insufficient balance.
            # Check the actual error code before retrying.
            try:
                err = resp.json()
                code = err.get("code")
                msg  = err.get("message", "unknown")
                # 1102 = insufficient credits — no point retrying
                if code == 1102:
                    raise RuntimeError(
                        f"Kling account balance is empty (code {code}: {msg}). "
                        "Add credits at https://klingai.com to generate videos."
                    )
            except (ValueError, KeyError):
                pass
            print(f"  Rate limited — retrying in {wait}s...", flush=True)
            time.sleep(wait)
            wait *= 2
            continue
        resp.raise_for_status()
        data = resp.json()
        if data.get("code") != 0:
            raise RuntimeError(f"Kling API error: {data.get('message', data)}")
        return data
    raise RuntimeError(f"Rate limit persisted after {retries} retries.")


def _submit_text2video(
    prompt: str,
    negative_prompt: str,
    duration: int,
    mode: str,
    aspect_ratio: str,
) -> str:
    """Submit a text-to-video task. Returns task_id."""
    url  = f"{BASE_URL}/v1/videos/text2video"
    body = {
        "model_name":      MODEL,
        "prompt":          prompt,
        "negative_prompt": negative_prompt,
        "cfg_scale":       0.5,
        "mode":            mode,
        "aspect_ratio":    aspect_ratio,
        "duration":        str(duration),
    }
    data = _post_with_retry(url, body)
    return data["data"]["task_id"]


def _submit_image2video(
    prompt: str,
    negative_prompt: str,
    image: str,
    duration: int,
    mode: str,
) -> str:
    """Submit an image-to-video task. Returns task_id."""
    url  = f"{BASE_URL}/v1/videos/image2video"
    body = {
        "model_name":      MODEL,
        "image":           image,
        "prompt":          prompt,
        "negative_prompt": negative_prompt,
        "cfg_scale":       0.5,
        "mode":            mode,
        "duration":        str(duration),
    }
    data = _post_with_retry(url, body)
    return data["data"]["task_id"]


def _poll_task(task_id: str, task_type: str) -> list[str]:
    """
    Poll a task until it succeeds. Returns list of video URLs.
    task_type: "text2video" or "image2video"
    """
    url   = f"{BASE_URL}/v1/videos/{task_type}/{task_id}"
    start = time.time()

    print(f"  [{task_id}] Generating", end="", flush=True)

    while True:
        elapsed = time.time() - start
        if elapsed > MAX_WAIT:
            raise TimeoutError(
                f"Task {task_id} timed out after {int(elapsed)}s"
            )

        resp = requests.get(url, headers=_headers(), timeout=30)
        resp.raise_for_status()
        data   = resp.json()

        if data.get("code") != 0:
            raise RuntimeError(f"Kling API polling error: {data.get('message', data)}")

        task   = data["data"]
        status = task.get("task_status", "")

        if status == "succeed":
            print(f" done ({int(elapsed)}s)")
            videos = task.get("task_result", {}).get("videos", [])
            return [v["url"] for v in videos]

        if status == "failed":
            msg = task.get("task_status_msg", "unknown reason")
            raise RuntimeError(f"Task {task_id} failed: {msg}")

        print(".", end="", flush=True)
        time.sleep(POLL_INTERVAL)


def _download(url: str, dest: Path) -> None:
    """Download a video from URL to local path."""
    resp = requests.get(url, stream=True, timeout=120)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

# ── Main Generation ───────────────────────────────────────────────────────────

def generate(
    prompt:          str,
    negative_prompt: str  = "",
    image_path:      str  = None,
    num_videos:      int  = 2,
    duration:        int  = 5,
    mode:            str  = "std",
    aspect_ratio:    str  = "9:16",
) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    task_type = "image2video" if image_path else "text2video"
    image_data = encode_image(image_path) if image_path else None

    # Submit all tasks first
    print(f"Submitting {num_videos} {task_type} task(s) — model: {MODEL}, {duration}s, {mode}, {aspect_ratio}")
    task_ids = []
    for i in range(num_videos):
        if image_data:
            task_id = _submit_image2video(
                prompt, negative_prompt, image_data, duration, mode
            )
        else:
            task_id = _submit_text2video(
                prompt, negative_prompt, duration, mode, aspect_ratio
            )
        task_ids.append(task_id)
        print(f"  Task {i + 1}/{num_videos} submitted: {task_id}")

    # Poll and download each task
    saved = []
    for idx, task_id in enumerate(task_ids, start=1):
        video_urls = _poll_task(task_id, task_type)
        for video_url in video_urls:
            dest = OUTPUT_DIR / f"video_candidate_{idx}.mp4"
            print(f"  Downloading → {dest.name} ...", end="", flush=True)
            _download(video_url, dest)
            print(" saved.")
            saved.append(str(dest))

    return {
        "prompt":          prompt,
        "negative_prompt": negative_prompt,
        "model":           MODEL,
        "mode":            mode,
        "duration":        duration,
        "aspect_ratio":    aspect_ratio,
        "image_input":     image_path,
        "videos":          saved,
    }

# ── Entry Point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Kling AI video generator")
    parser.add_argument(
        "brief", nargs="?", default=None,
        help="Prompt string or JSON object. Ignored when --visual is used.",
    )
    parser.add_argument(
        "--visual", metavar="PATH",
        help="Path to an art-direction .md file",
    )
    parser.add_argument(
        "--image", metavar="PATH",
        help="Input image for image-to-video mode (local path or URL)",
    )
    parser.add_argument("--num",      type=int, default=2,     help="Number of videos (default: 2)")
    parser.add_argument("--duration", type=int, default=5,     choices=[5, 10], help="Duration in seconds (default: 5)")
    parser.add_argument("--mode",     type=str, default="std", choices=["std", "pro"], help="Generation mode: std or pro (default: std)")
    parser.add_argument("--aspect",   type=str, default="9:16", help="Aspect ratio (default: 9:16)")

    args  = parser.parse_args()
    num   = args.num
    dur   = args.duration
    mode  = args.mode
    aspect = args.aspect
    image_path = args.image

    if args.visual:
        brief_path = Path(args.visual).resolve()
        prompt, negative = extract_from_brief(brief_path)
    else:
        raw = args.brief or "cinematic travel moment, golden hour, 35mm film"
        try:
            data       = json.loads(raw)
            prompt     = data.get("prompt", raw)
            negative   = data.get("negative", "")
            num        = int(data.get("num", num))
            dur        = int(data.get("duration", dur))
            mode       = data.get("mode", mode)
            aspect     = data.get("aspect", aspect)
            image_path = data.get("image", image_path)
        except json.JSONDecodeError:
            prompt   = raw
            negative = ""

    result = generate(
        prompt=prompt,
        negative_prompt=negative,
        image_path=image_path,
        num_videos=num,
        duration=dur,
        mode=mode,
        aspect_ratio=aspect,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
