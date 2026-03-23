---
name: image-ad-generator
description: >
  Generate Instagram ad images using Imagen 3 on Google AI (Gemini API).
  Use when the user asks to create an ad visual, generate a social media
  image, or produce creative for Instagram.
allowed-tools: Read, Bash(python3*)
model: claude-sonnet-4-6
---

# Instagram Ad Generator

Read `CLAUDE.md` for brand colors and visual style before building the prompt.

## Option A — From a visual brief file (recommended)

Point the script at one of the art-direction files in `visuals/`:

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-instagram-ad-01.md
```

The script automatically extracts the **Generation Prompt** and **Negative prompt**
sections from the markdown file and generates **3 images** at **9:16**.

## Option B — From a plain text prompt

```bash
python3 skills/image-ad-generator/scripts/generate.py "your prompt here"
```

## Option C — Full JSON control

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  '{"prompt": "...", "negative": "...", "aspect": "9:16", "num": 3}'
```

## CLI flags

| Flag | Default | Description |
|------|---------|-------------|
| `--visual PATH` | — | Path to art-direction `.md` file |
| `--num N` | 3 | Number of images to generate |
| `--aspect RATIO` | `9:16` | Aspect ratio (e.g. `1:1`, `4:5`) |

## Output

The script prints a JSON object with saved file paths:

```json
{
  "prompt": "...",
  "negative_prompt": "...",
  "model": "imagen-3.0-generate-002",
  "aspect_ratio": "9:16",
  "images": [
    "skills/image-ad-generator/output/ad_candidate_1.png",
    "skills/image-ad-generator/output/ad_candidate_2.png",
    "skills/image-ad-generator/output/ad_candidate_3.png"
  ]
}
```

Present the image paths to the user as a numbered list and ask which
candidate they want to keep or if they'd like to iterate with a new prompt.