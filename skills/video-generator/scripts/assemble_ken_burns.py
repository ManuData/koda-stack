#!/usr/bin/env python3
"""
Assemble a 15-second 9:16 Ken Burns reel from Marrakech souk stills.
Applies per-shot zoom/pan motion following the storyboard in:
  visuals/storyboard-marrakech-souk-reel.md

Output: skills/video-generator/output/marrakech_reel.mp4
"""

import cv2
import numpy as np
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

FPS      = 24
OUT_W    = 1080
OUT_H    = 1920
OUTPUT   = Path(__file__).parent.parent / "output" / "marrakech_reel.mp4"
ASSETS   = Path(__file__).parent.parent.parent.parent / "assets/moodboard/video_reels"

# ── Shot Deck (from storyboard) ───────────────────────────────────────────────
#
# Each shot: (filename, duration_s, motion, params)
#
# motion types:
#   zoom_in   — slow zoom toward anchor point
#   zoom_out  — slow zoom out from anchor point
#   pan_right — slow horizontal pan right
#   pan_down  — slow vertical pan downward
#
# anchor: "center" | "top_left" | "top_right" | "bottom_center"

SHOTS = [
    # 1 — G — Hook: overhead centered, slow zoom in toward white figure
    (
        "hf_20260401_130307_64273041-10a1-41a2-b081-1f297a89792e.png",
        1.5, "zoom_in", {"start": 1.00, "end": 1.10, "anchor": "center"},
    ),
    # 2 — B — World: wide eye-level, slow pan right following the light
    (
        "hf_20260401_130306_25911b77-fe5c-4615-b3f3-14555d6ad700.png",
        2.0, "pan_right", {"amount": 0.04},
    ),
    # 3 — I — Emotional peak: back shot, slow push into the amber glow
    (
        "hf_20260401_130307_888fd39e-a2d9-43f2-9ec5-ed65eac50708.png",
        2.5, "zoom_in", {"start": 1.00, "end": 1.08, "anchor": "center"},
    ),
    # 4 — E — Immersion: intimate amber, zoom toward lanterns upper-left
    (
        "hf_20260401_130306_c9172f5a-530e-432d-b330-f7c92c109f08.png",
        2.0, "zoom_in", {"start": 1.00, "end": 1.12, "anchor": "top_left"},
    ),
    # 5 — D — Build: mid eye-level, gentle zoom in
    (
        "hf_20260401_130306_489b2b66-7b70-43f9-9d2b-3d39bc423836.png",
        1.5, "zoom_in", {"start": 1.00, "end": 1.08, "anchor": "center"},
    ),
    # 6 — C — Rhythm break: overhead, slow pan down revealing spice stripes
    (
        "hf_20260401_130306_3855d97e-21d1-4991-8727-0d6f5b4c9cb9.png",
        2.0, "pan_down", {"amount": 0.03},
    ),
    # 7 — K — Close: wide corridor, ultra-slow push in — she belongs here
    (
        "hf_20260401_130307_af7e1e34-c0b7-4f9d-8671-06a7b65120f4.png",
        3.5, "zoom_in", {"start": 1.00, "end": 1.08, "anchor": "center"},
    ),
]

# ── Image Loading ─────────────────────────────────────────────────────────────

def load_and_crop_916(path: Path) -> np.ndarray:
    """
    Load image, scale to fit height=1920, center-crop width to 1080.
    Converts 3:4 source into 9:16 output frame.
    """
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Cannot load image: {path}")

    h, w = img.shape[:2]

    # Scale so height fills OUT_H
    scale  = OUT_H / h
    new_w  = int(w * scale)
    img    = cv2.resize(img, (new_w, OUT_H), interpolation=cv2.INTER_LANCZOS4)

    # Center-crop width to OUT_W
    h2, w2 = img.shape[:2]
    if w2 < OUT_W:
        # Image too narrow — pad with black edges
        pad   = (OUT_W - w2) // 2
        img   = cv2.copyMakeBorder(img, 0, 0, pad, OUT_W - w2 - pad,
                                   cv2.BORDER_CONSTANT, value=(0, 0, 0))
    else:
        x_start = (w2 - OUT_W) // 2
        img     = img[:, x_start:x_start + OUT_W]

    return img

# ── Ken Burns Engine ──────────────────────────────────────────────────────────

def _zoom_crop(img: np.ndarray, zoom: float, anchor: str) -> np.ndarray:
    """
    Crop a zoomed-in region from img and scale back to OUT_W x OUT_H.
    anchor controls which part of the image is the focal point.
    """
    h, w   = img.shape[:2]
    crop_w = int(OUT_W / zoom)
    crop_h = int(OUT_H / zoom)

    # Anchor position
    if anchor == "center":
        x = (w - crop_w) // 2
        y = (h - crop_h) // 2
    elif anchor == "top_left":
        x, y = 0, 0
    elif anchor == "top_right":
        x = w - crop_w
        y = 0
    elif anchor == "bottom_center":
        x = (w - crop_w) // 2
        y = h - crop_h
    else:
        x = (w - crop_w) // 2
        y = (h - crop_h) // 2

    x = max(0, min(x, w - crop_w))
    y = max(0, min(y, h - crop_h))

    cropped = img[y:y + crop_h, x:x + crop_w]
    return cv2.resize(cropped, (OUT_W, OUT_H), interpolation=cv2.INTER_LANCZOS4)


def apply_ken_burns(
    img: np.ndarray,
    motion: str,
    params: dict,
    t: float,          # 0.0 → 1.0 over the shot duration
) -> np.ndarray:
    """Return a single OUT_W × OUT_H frame for time t."""

    h, w = img.shape[:2]

    # ── zoom_in ────────────────────────────────────────────────────────────
    if motion == "zoom_in":
        zoom = params["start"] + (params["end"] - params["start"]) * t
        return _zoom_crop(img, zoom, params.get("anchor", "center"))

    # ── zoom_out ───────────────────────────────────────────────────────────
    if motion == "zoom_out":
        zoom = params["start"] - (params["start"] - params["end"]) * t
        return _zoom_crop(img, zoom, params.get("anchor", "center"))

    # ── pan_right ──────────────────────────────────────────────────────────
    if motion == "pan_right":
        amount   = params["amount"]
        base_zoom = 1.06           # slight zoom to give horizontal room
        crop_w   = int(OUT_W / base_zoom)
        crop_h   = int(OUT_H / base_zoom)
        x_range  = w - crop_w
        # Start left-of-center, end right-of-center
        x_mid    = (w - crop_w) // 2
        x_travel = int(w * amount)
        x = x_mid - x_travel // 2 + int(x_travel * t)
        y = (h - crop_h) // 2
        x = max(0, min(x, w - crop_w))
        y = max(0, min(y, h - crop_h))
        cropped  = img[y:y + crop_h, x:x + crop_w]
        return cv2.resize(cropped, (OUT_W, OUT_H), interpolation=cv2.INTER_LANCZOS4)

    # ── pan_down ───────────────────────────────────────────────────────────
    if motion == "pan_down":
        amount    = params["amount"]
        base_zoom = 1.06
        crop_w    = int(OUT_W / base_zoom)
        crop_h    = int(OUT_H / base_zoom)
        y_travel  = int(h * amount)
        x         = (w - crop_w) // 2
        y_mid     = (h - crop_h) // 2
        y         = y_mid - y_travel // 2 + int(y_travel * t)
        x = max(0, min(x, w - crop_w))
        y = max(0, min(y, h - crop_h))
        cropped   = img[y:y + crop_h, x:x + crop_w]
        return cv2.resize(cropped, (OUT_W, OUT_H), interpolation=cv2.INTER_LANCZOS4)

    # Fallback — static
    return img

# ── Render ────────────────────────────────────────────────────────────────────

def render():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(OUTPUT), fourcc, FPS, (OUT_W, OUT_H))

    total_frames = sum(int(dur * FPS) for _, dur, _, _ in SHOTS)
    total_dur    = sum(dur for _, dur, _, _ in SHOTS)
    print(f"Rendering {len(SHOTS)} shots — {total_dur:.1f}s — {total_frames} frames @ {FPS}fps")
    print(f"Output: {OUTPUT}\n")

    rendered = 0
    for i, (filename, duration, motion, params) in enumerate(SHOTS, 1):
        path       = ASSETS / filename
        num_frames = int(duration * FPS)
        print(f"  Shot {i}/{len(SHOTS)}  {filename[:36]}  {duration}s  [{motion}]")

        img = load_and_crop_916(path)

        for f in range(num_frames):
            t     = f / max(num_frames - 1, 1)   # smooth 0.0 → 1.0
            frame = apply_ken_burns(img, motion, params, t)
            writer.write(frame)
            rendered += 1

        pct = rendered / total_frames * 100
        print(f"          {pct:.0f}% complete ({rendered}/{total_frames} frames)")

    writer.release()

    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"\nDone. {size_mb:.1f} MB → {OUTPUT}")


if __name__ == "__main__":
    render()
