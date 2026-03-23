# Imagen 3 — Model Reference

## Model ID
imagen-3.0-generate-002

## Aspect ratios

| Value  | Dimensions  | Use case                    |
|--------|-------------|-----------------------------|
| `1:1`  | 1080 × 1080 | Feed post (default)         |
| `4:5`  | 1080 × 1350 | Portrait feed               |
| `9:16` | 1080 × 1920 | Stories / Reels             |
| `16:9` | 1920 × 1080 | Landscape / YouTube preview |
| `3:4`  | 810 × 1080  | Alternative portrait        |

## Key parameters

| Parameter            | Type    | Values                                              | Notes                                        |
|----------------------|---------|-----------------------------------------------------|----------------------------------------------|
| `number_of_images`   | int     | 1–4                                                 | Max 4 per request                            |
| `aspect_ratio`       | string  | see table above                                     | Defaults to `1:1`                            |
| `safety_filter_level`| string  | `block_low_and_above` · `block_medium_and_above` · `block_only_high` | Use `block_only_high` for ad content        |
| `person_generation`  | string  | `dont_allow` · `allow_adult`                        | Set `allow_adult` for lifestyle/people ads   |

## Output format
- Returns raw image bytes (base64-encoded)
- Saved locally as PNG
- Must be uploaded to Cloudinary before Instagram publishing

## Prompt structure that works well
```
[subject] + [environment/setting] + [lighting] + [style] + [brand palette] + [composition]
```

Example:
```
minimalist AI dashboard interface, dark studio environment, warm amber rim lighting,
cinematic product shot, dominant #FF6B00 orange accents, centered hero composition,
bold sans-serif headline, 8K, commercial photography
```

## Prompt tips
- Describe the subject first, style last
- Name brand colors explicitly as hex or color name
- For readable text in the image: add `"bold sans-serif headline, legible, centered"`
- Imagen 3 understands natural language well — write conversationally, not keyword-stuffed
- Avoid negatives in the main prompt — Imagen 3 does not support a `negative_prompt` parameter

## What Imagen 3 is strong at
- Photorealistic product shots
- Accurate text rendering inside images
- Consistent lighting and composition
- Following detailed natural language briefs

## What to avoid
- Requesting copyrighted logos or brand marks
- Prompts with explicit violence, adult content, or real named individuals
- Overly abstract prompts — be specific about what you want to see

## Pricing (Google AI Studio)
| Tier        | Cost per image |
|-------------|----------------|
| Free        | Limited quota  |
| Paid        | ~$0.04 / image |

Full pricing: `ai.google.dev/pricing`