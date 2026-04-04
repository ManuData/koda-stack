# ART DIRECTION — Palawan Coffee Solo
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Brief: Solo sport-chic woman, beachside bamboo café, Palawan Philippines, golden hour

---

## Concept Brief

A beachside bamboo café at the edge of the Philippines. Turquoise water
visible beyond the palm fringe. A solo traveler, flat white in hand,
eyes on the horizon. The sea does what it always does — the traveler
does what they came to do. Nothing. Everything. This moment.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Turquoise sea                   — vibrant sky blue: #8DC8F5
  Golden hour beach light         — golden orange: #FFB067
  Palm canopy / shade             — deep tropical green: #4A7C59
  Outfit linen / skin warmth      — flamingo warm ambient: #FFBFC0
  Bamboo café structure           — warm natural tan: #C8B99A
  Upper sky                       — pale warm horizon haze: #F5E264 fading to #E8EDF0

Mood:
  The coffee you drink watching the sea go nowhere.
  No phone, no plan, no rush. Just the turquoise and the steam.

Lighting:
  Late afternoon golden hour — low sun from camera-right, positioned
  just above the horizon over the sea. Creates blazing warm backlight
  that halos the subject's hair, shoulder, and the steam from the cup.
  Palm fronds at upper frame edges filter the light into dappled warm
  patches. Turquoise sea catches the golden light as warm shimmer in
  bokeh. Bamboo café structure casts soft warm shadow. The temperature
  split is strong here: lower frame warm gold, upper frame transitions
  from warm horizon to cool pale sky — the brand's signature palette.
  Never: midday overhead, cold blue sea light, flat even lighting, flash.

Composition:
  Format: 3:4 vertical (1080×1350)
  Camera: low angle looking slightly upward — the sport-chic signature.
    Subject gains visual authority against the sea and sky.
  Subject: center to slight left, waist-up. One hand holding ceramic
    coffee cup at chest level, other hand relaxed. Eyes on the horizon
    or softly lowered — never at the camera.
  Sea: visible in mid-to-upper background through palm trunks or
    over a bamboo railing — turquoise, shimmering, full bokeh.
  Palm fronds: partially visible at upper frame edges, filtering light.
  Coffee: ceramic cup held in hand or on bamboo/driftwood table edge
    in lower frame, steam catching backlight.
  Depth layers: subject sharp → bamboo structure mid-detail → sea
    and palms mid-bokeh → horizon and sky full bokeh.
  Never: full-body wide shot, direct camera stare, tourist beach crowds,
    resort branding visible, symmetrical centered crop.

Outfit:
  High-waist wide-leg linen trousers — warm white or pale sand
  Fitted ribbed crop top — white or ivory
  Lightweight open linen shirt — coral #E8644A or pale flamingo,
    draped loosely, never buttoned — hero color of the outfit
  Layered thin gold chains (2–3 layers) catching backlight
  Hair: natural waves, slightly wind-lifted at the ends, sun-kissed
  Minimal footwear (if visible): bare feet or simple leather sandals

Coffee detail:
  Ceramic flat white or espresso — warm off-white cup
  Steam rising and catching the golden backlight — visible against
    the turquoise sea background
  Driftwood table edge or bamboo surface in lower frame
  No branded items, no plastic, no paper cups

Expression:
  Eyes on the sea or horizon — soft, open, present.
  Mouth relaxed. Not smiling for anyone. Just there.
  Hair strand or two caught in the sea breeze.
  Very subtle warmth on skin from the sun — natural glow, not
  excessive sweat. Just the honest warmth of an afternoon in Palawan.
  Never: direct camera stare, forced smile, stock-photo alertness.

Texture:
  35mm film, Kodak Portra 400, natural warm grain.
  Skin: golden warm, sun-kissed, natural — no airbrushing.
  Sea: turquoise warm bokeh shimmer in background — saturated but
    not postcard-oversaturated. Real, not HDR.
  Steam: backlit by golden hour, creates a soft halo effect.
  Never: HDR, oversaturated tropical postcard, heavy preset, plastic skin.

Do NOT:
  - Text, typography, logos, or graphic overlays
  - Subject looking at camera
  - Resort branding or signage visible
  - Takeaway or plastic cups
  - Tourists or resort crowds
  - Midday harsh overhead light
  - Cold blue sea tones — turquoise stays warm in golden hour
  - Full-body wide shot
  - Perfectly calm posed posture — allow natural movement
---
```

---

## Generation Prompt

```
candid low-angle photograph looking slightly upward of a solo sport-chic
young woman at a beachside bamboo café in Palawan Philippines, waist-up
framing, she is holding a ceramic flat white coffee cup at chest level
with soft steam catching the golden backlight, eyes on the horizon or
softly lowered never looking at camera, relaxed natural posture, outfit:
high-waist wide-leg pale linen trousers, fitted white ribbed crop top,
lightweight coral linen shirt draped open, layered thin gold chains
catching golden backlight, natural wavy hair with one strand lifted by
sea breeze, turquoise Philippine sea visible through palm trunks and
bamboo railing behind her in warm bokeh shimmer, palm fronds at upper
frame edges filtering tropical light, blazing golden hour backlight from
low sun over the sea creating warm halo on hair and shoulders and steam
from coffee cup, lower frame warm golden orange, upper frame pale warm
horizon sky, bamboo café surface edge visible in lower frame, Kodak
Portra 400 35mm film grain, natural sun-kissed skin texture, shallow
depth of field, authentic tropical travel mood, no text no logos
```

**Negative prompt:**
```
text, typography, logos, looking at camera, forced smile, posed, stock
photo, airbrushed skin, neon, HDR, oversaturated, cold blue sea light,
resort branding, takeaway cup, plastic cup, tourists, harsh overhead
midday light, full body wide shot, heavy preset filter, plastic skin
```

---

## CLI Usage

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-palawan-coffee-solo.md \
  --num 3 \
  --aspect 3:4
```

## Reference Files
- `skills/image-ad-generator/output/sport_chic_overshoulder_2.png` — low angle authority and backlight halo reference
- `skills/image-ad-generator/output/terrace_trio_natural_1.png` — golden hour blaze and outdoor warmth reference
- `assets/moodboard/sport_chic/env_v1_beach.png` — beach environment reference
