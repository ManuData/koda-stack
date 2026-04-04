# ART DIRECTION — Sport-Chic Traveler
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> References: `assets/moodboard/sport_chic/` (9 images analyzed)

---

## Concept Brief

A sport-chic traveler — solo or duo — caught in a real moment with their smartphone.
The image reads as candid, not commercial. The outfit is the product. The environment
is the aspiration. The phone is the connection. No text. No graphic elements. Pure image.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Hero color    — leggings: coral #E8644A / sage green #8FAF8F /
                  dusty mauve #C4A0A0 (rotate per execution)
  Base          — white crop top: #F5F4FF
  Outer layer   — blazer: ecru #EDE8DC / sand #C8B99A / camel #C49A6C
  Sky           — pale desaturated blue-grey: #C8D4DC → #E8EDF0
  Skin warmth   — golden hour: #FFB067 as ambient

Mood: The ease of someone who has stopped trying to look good — and simply does.

Lighting:
  Golden hour backlight — low sun positioned behind subject, slightly
  camera-right or camera-left. Creates soft warm rim glow on hair,
  ears, and shoulders. Diffused, not dramatic. No harsh shadows.
  Upper frame: pale blue-grey desaturated sky — never deep blue.
  Lower frame: warm golden ambient on skin and outfit.
  Temperature split: warm lower two-thirds / cool pale upper third.
  Never: midday overhead light, studio flat lighting, cold tones.

Composition:
  Format: 3:4 vertical (1080×1350)
  Crop: waist-up to chest-up — never full-body
  Camera angle: low angle looking slightly upward — signature.
    Sky dominant in upper 30–40%. Subject gains visual authority.
  Subject placement: slight left-of-center (solo) / centered (duo)
  Depth layers: subject sharp → city skyline mid-bokeh → pale sky
  Environment: rooftop terrace (stone/tile floor, plants, railing)
    OR beach promenade (low wall, palms, turquoise sea)

Outfit (non-negotiable structure):
  1. High-waist seamless leggings — hero color, no logos
  2. Fitted white athletic crop top — always white
  3. Oversized blazer — neutral tone, always open/draped, never
     matching the leggings color
  4. Layered thin gold chains (2–3 layers)
  5. Hair: low bun with loose strands, or natural waves
  6. Smartphone: held naturally at chest/waist, screen toward subject

Expression:
  Solo: soft downward gaze at phone — not at camera. Neutral to soft,
  never forced smile.
  Duo: shared gaze at phone, genuine warmth, heads leaning together.
  Post-workout variant: subtle sweat sheen on forehead and collarbone,
  hair slightly damp, soft flush on cheeks.

Texture:
  35mm film look, ISO 400 grain, natural color grading.
  Realistic skin texture — no airbrushing, no plastic skin.
  Slightly desaturated midtones; leggings color and golden rim light
  stay fully saturated.

Do NOT:
  - Text, typography, or graphic elements inside the image
  - Full-body wide shot
  - Direct frontal camera stare (unless brief specifies it)
  - Harsh or flat lighting
  - Logos on any garment
  - Oversaturated HDR treatment
  - Matching outfits on duo shots
  - Forced smiles or stock-photo expressions
  - Neon or artificial color sources
---
```

---

## Generation Prompt — Solo (rooftop, coral, low angle)

```
candid close waist-up shot of a sport-chic young woman on a
sun-drenched hotel rooftop terrace with city skyline behind, she is
looking down at her smartphone with a soft natural expression, low
angle camera looking slightly upward, sky dominant in upper frame,
outfit: high-waist coral seamless leggings, fitted white athletic crop
top, ecru oversized blazer casually draped open, layered thin gold
chains, hair in relaxed low bun with loose strands, smartphone held
naturally at chest level eyes on screen, golden hour backlight from
low sun behind subject creating soft warm rim glow on hair and
shoulders, pale blue-grey desaturated sky upper background, warm bokeh
city skyline behind, natural sun-kissed skin tones, realistic skin
texture, 35mm film look, ISO 400 grain, natural color grading,
authentic candid summer mood, editorial quality, no text no logos
```

**Negative prompt:**
```
text, typography, logos, graphic lines, borders, overlays, looking at
camera, over-posed, stiff, stock photo, plastic airbrushed skin, neon,
HDR, oversaturated, indoor, winter, excessive sweat, full body shot,
harsh shadows, flat lighting, matching couple outfits
```

---

## Generation Prompt — Duo (beach promenade, golden backlight)

```
candid waist-up shot, two friends sitting on a low wall on a beach
promenade, a young woman and a young man, both naturally looking at a
smartphone he is holding, genuine soft smiles and warmth,
unaware-of-camera energy, she is leaning slightly on his shoulder,
woman outfit: high-waist seamless leggings in hero color, white
athletic crop top, oversized blazer in contrasting neutral tone, layered
thin gold chains, hair slightly damp natural waves; man outfit:
athletic shorts in complementary color — NOT matching the leggings,
fitted white tee, light unstructured shirt jacket open, clean white
sneakers, single fine gold chain, outfits contrasting not matching,
turquoise sea and palm trees softly blurred behind, warm golden hour
backlight from low sun behind subjects creating soft rim glow on hair
and shoulders, pale blue-grey sky in upper background, realistic
natural skin tones, realistic skin texture, 35mm film look, ISO 400
grain, authentic candid summer moment, no text no logos
```

**Negative prompt:**
```
text, typography, logos, graphic lines, looking at camera, over-posed,
matching outfits, plastic airbrushed skin, neon, HDR, oversaturated,
excessive sweat, studio lighting, midday harsh overhead light,
exaggerated expressions, stiff commercial look
```

---

## CLI Usage

```bash
# Solo — 3 candidates
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-sport-chic-traveler.md \
  --num 3 \
  --aspect 3:4

# Swap outfit color in the prompt to get coral / sage / mauve variants
```

## Reference Files
- `assets/moodboard/sport_chic/summer_proposal_2.png` — canonical solo reference
- `assets/moodboard/sport_chic/p2_angle_2.png` — canonical angle reference
- `assets/moodboard/sport_chic/color_v3_mauve.png` — warmest palette reference
- `assets/moodboard/sport_chic/duo_v1_sage.png` — canonical duo reference
- `assets/moodboard/sport_chic/env_v1_beach.png` — beach environment reference
