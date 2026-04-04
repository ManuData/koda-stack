# ART DIRECTION — Bali Coffee Solo
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Brief: Solo sport-chic woman, open-air rice terrace café, Bali, morning golden hour

---

## Concept Brief

A solo traveler at a Bali rice terrace café — mid-sip, eyes lowered, unbothered.
The terraces drop behind her in layers of wet green. The steam from her espresso
rises into the humid morning air. She is not performing. She arrived, she ordered,
she is exactly where she wants to be. The phone is face-down on the table.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Tropical green (rice terraces)  — deep lush: #4A7C59
  Morning mist / sky              — pale warm haze: #E8E0D0
  Skin warmth / golden ambient    — golden orange: #FFB067
  Outfit base                     — ecru / warm linen: #EDE8DC
  Coffee ceramic                  — off-white warm: #F5F4FF
  Shadow depth                    — warm dark indigo: #211F54

Mood:
  The first coffee of the trip — before the itinerary, before the photos,
  before anything. Just her, the terraces, and the steam.

Lighting:
  Soft morning golden hour — low sun from camera-right at approximately
  30–40 degrees, warm directional side light on face and shoulder.
  Humidity haze diffuses the light: no hard edges, everything slightly
  veiled in warm mist. Upper background: pale warm sky filtered through
  tropical canopy — dappled, not direct. Rice terraces catch the early
  light in their water surface, creating soft gold reflections in bokeh.
  Never: midday overhead, cold blue light, flash, studio flat.

Composition:
  Format: 3:4 vertical (1080×1350)
  Camera: eye level to slightly above — not overhead, not looking up.
    Intimate, as if sitting at the next table.
  Subject: center-left of frame, waist-up crop. Head and upper body
    fill mid-frame. Space to the right where the terraces breathe.
  Coffee cup: in the lower-center of frame, hands wrapped around it
    or just set down, steam visible rising from cup surface.
  Background: rice terraces in stepped layers dropping away behind,
    mid-to-full bokeh. Tropical canopy at upper edges of frame.
  Depth layers: subject sharp → table edge mid-sharp → terraces
    mid-bokeh → sky/canopy full bokeh.
  Phone: face-down on the table in lower frame or absent — never in hand.
  Never: wide full-body, direct camera stare, symmetrical centered crop,
    tourist-heavy background.

Outfit:
  High-waist wide-leg linen trousers — warm ecru or natural linen #EDE8DC
  Fitted ribbed crop top — white or off-white
  Lightweight open kimono jacket — draped loosely, sage green #8FAF8F
    or dusty sand, never buttoned
  Layered thin gold chains (2–3), one slightly longer
  Hair: natural waves slightly damp from humidity, loosely pulled back
    or half-up with face-framing strands
  Minimal footwear (if visible): simple leather sandal

Coffee detail:
  Small ceramic espresso cup or flat white — off-white or terracotta tone
  Visible latte art — rosette or tulip
  Soft steam rising from cup surface
  Reclaimed dark wood table surface, worn texture
  No branded items, no paper cups, no plastic

Expression:
  Eyes lowered — looking at the coffee cup or softly at the view.
  Mouth slightly relaxed — post-sip or about to sip.
  Shoulders dropped, posture easy. No tension. No performance.
  Never: direct camera stare, forced smile, stock-photo alertness.

Texture:
  35mm film, Kodak Portra 400, natural warm grain.
  Skin: warm, sun-kissed, lightly dewy from humidity — not airbrushed.
  Slightly desaturated midtones — rice terrace greens and gold chains
  stay fully saturated. Morning haze softens contrast naturally.
  Never: HDR, oversaturated, heavy Instagram warm filter, smooth skin.

Do NOT:
  - Text, typography, logos, or graphic overlays
  - Subject looking at camera
  - Takeaway cups, branded cups, plastic
  - Tourists or crowds in background
  - Midday harsh overhead light
  - Overly saturated tropical postcard look
  - Wide full-body shot
  - Forced smile or posed expression
  - Phone in hand — face-down or off-table only
---
```

---

## Generation Prompt

```
candid eye-level photograph of a solo sport-chic young woman at an open-air
Bali rice terrace café, waist-up framing, she is mid-sip or just lowering
her espresso cup with eyes softly downward and relaxed natural expression,
never looking at camera, outfit: high-waist wide-leg ecru linen trousers,
fitted white ribbed crop top, lightweight sage green kimono jacket draped
open, layered thin gold chains, natural wavy hair slightly damp loosely
pulled back, small terracotta ceramic espresso cup with visible latte art
and soft steam rising on reclaimed dark wood table in foreground, rice
terraces dropping in stepped lush green layers behind her in warm bokeh,
tropical canopy at upper frame edges, soft morning golden hour side light
from camera-right creating warm glow on skin and hair, humidity haze
diffusing the light, pale warm misty sky, natural dewy skin texture,
Kodak Portra 400 35mm film grain, shallow depth of field, authentic
candid travel mood, no text no logos
```

**Negative prompt:**
```
text, typography, logos, looking at camera, forced smile, posed, stock photo,
plastic airbrushed skin, neon, HDR, oversaturated, harsh midday light,
takeaway cup, branded cup, tourists in background, phone in hand, full body
wide shot, cold blue tones, heavy filter
```

---

## CLI Usage

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-bali-coffee-solo.md \
  --num 3 \
  --aspect 3:4
```

## Reference Files
- `skills/image-ad-generator/output/kyoto_street_jeans_1.png` — natural color grading and candid energy
- `skills/image-ad-generator/output/kyoto_bamboo_1.png` — tropical environment, outfit tone reference
