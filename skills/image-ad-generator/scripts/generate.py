#!/usr/bin/env python3
"""
Generate Instagram ad images via Imagen 3 (Google AI).

Usage:
  # From a visual brief markdown file (reads Generation Prompt + Negative prompt sections):
  python3 scripts/generate.py --visual ../../visuals/art-direction-instagram-ad-01.md

  # From a plain text prompt:
  python3 scripts/generate.py "young woman laughing at beach, golden hour"

  # From a JSON object (full control):
  python3 scripts/generate.py '{"prompt": "...", "negative": "...", "aspect": "9:16", "num": 3}'
"""

import sys
import os
import json
import re
import argparse
from pathlib import Path
from google import genai               # type: ignore[import]
from google.genai import types         # type: ignore[import]

# ── Config ────────────────────────────────────────────────────────────────────

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL   = "imagen-4.0-generate-001"

DEFAULT_STYLE = (
    "editorial quality, commercial photography, Instagram ad aesthetic, "
    "9:16 vertical, ultra realistic, 8K"
)

OUTPUT_DIR = Path(__file__).parent.parent / "output"

# ── Markdown parser ────────────────────────────────────────────────────────────

def extract_from_brief(md_path: Path) -> tuple[str, str]:
    """
    Extract the Generation Prompt and Negative prompt from an art-direction .md file.

    Handles two formats:
      Format A (ad-01): ## Generation Prompt + fenced block, then **Negative prompt:** + fenced block
      Format B (ad-02): ## Generate + fenced block with 'Prompt:' and 'Negative prompt:' keys inside
    """
    text = md_path.read_text(encoding="utf-8")
    prompt = ""
    negative = ""

    # ── Format A: ## Generation Prompt section ────────────────────────────────
    gen_section = re.search(
        r"## Generation Prompt.*?```(.*?)```",
        text, re.DOTALL
    )
    if gen_section:
        prompt = gen_section.group(1).strip()
        neg_section = re.search(
            r"\*\*Negative prompt.*?\*\*\W*```(.*?)```",
            text, re.DOTALL
        )
        if neg_section:
            negative = neg_section.group(1).strip()
        return prompt, negative

    # ── Format B: ## Generate section with Prompt: / Negative prompt: keys ────
    gen_block = re.search(
        r"## Generate.*?```(.*?)```",
        text, re.DOTALL
    )
    if gen_block:
        block = gen_block.group(1)

        # Extract multi-line value after 'Prompt:' until next key or end
        prompt_match = re.search(
            r"Prompt:\s*(.*?)(?=\n\s*\n\w|\nNegative prompt:|\nModel:|\nSettings:|\Z)",
            block, re.DOTALL
        )
        neg_match = re.search(
            r"Negative prompt:\s*(.*?)(?=\n\s*\n\w|\nModel:|\nSettings:|\Z)",
            block, re.DOTALL
        )

        if prompt_match:
            # Collapse indented continuation lines into one paragraph
            prompt = re.sub(r"\s+", " ", prompt_match.group(1)).strip()
        if neg_match:
            negative = re.sub(r"\s+", " ", neg_match.group(1)).strip()

    if not prompt:
        raise ValueError(
            f"Could not find a Generation Prompt in {md_path}.\n"
            "Expected either a '## Generation Prompt' section or a "
            "'## Generate' section with a 'Prompt:' key."
        )

    return prompt, negative

# ── Generation ────────────────────────────────────────────────────────────────

def generate(
    prompt: str,
    negative_prompt: str = "",
    num_images: int = 3,
    aspect_ratio: str = "9:16",
) -> dict:
    client = genai.Client(api_key=API_KEY)

    # Gemini API does not support negative_prompt in GenerateImagesConfig
    # (that param is Vertex AI only). Fold it into the prompt instead.
    full_prompt = f"{prompt.strip()}, {DEFAULT_STYLE}"
    if negative_prompt:
        full_prompt += f". Do NOT include: {negative_prompt.strip()}"

    response = client.models.generate_images(
        model=MODEL,
        prompt=full_prompt,
        config=types.GenerateImagesConfig(
            number_of_images=num_images,
            aspect_ratio=aspect_ratio,
        ),
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    saved = []
    for i, generated_image in enumerate(response.generated_images):
        filename = OUTPUT_DIR / f"ad_candidate_{i + 1}.png"
        filename.write_bytes(generated_image.image.image_bytes)
        saved.append(str(filename))

    return {
        "prompt":          full_prompt,
        "negative_prompt": negative_prompt,
        "model":           MODEL,
        "aspect_ratio":    aspect_ratio,
        "images":          saved,
    }

# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Imagen 3 Instagram ad generator")
    parser.add_argument(
        "brief",
        nargs="?",
        default=None,
        help="Prompt string or JSON object. Ignored when --visual is used.",
    )
    parser.add_argument(
        "--visual",
        metavar="PATH",
        help="Path to an art-direction .md file (e.g. visuals/art-direction-instagram-ad-01.md)",
    )
    parser.add_argument("--num",    type=int, default=3,     help="Number of images (default: 3)")
    parser.add_argument("--aspect", type=str, default="9:16", help="Aspect ratio (default: 9:16)")

    args = parser.parse_args()

    num    = args.num
    aspect = args.aspect

    if args.visual:
        brief_path = Path(args.visual).resolve()
        prompt, negative = extract_from_brief(brief_path)
    else:
        raw = args.brief or "AI creative tool, dark studio, amber glow"
        try:
            data     = json.loads(raw)
            prompt   = data.get("prompt", raw)
            negative = data.get("negative", "")
            num      = int(data.get("num", num))
            aspect   = data.get("aspect", aspect)
        except json.JSONDecodeError:
            prompt   = raw
            negative = ""

    result = generate(
        prompt=prompt,
        negative_prompt=negative,
        num_images=num,
        aspect_ratio=aspect,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()