# ART DIRECTION — Burning Man: Blue Hour Fire Glow
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Brief: Chic man traveler, Black Rock Desert playa, blue hour with distant fire installation glow

---

## Concept Brief

The playa after the sun drops. The sky turns the brand's deepest colors —
indigo, lavender, a last warm ember at the horizon. In the distance, a flame
sculpture pulses orange. A man stands still in all of it. Not performing.
Not searching. Just there, in the middle of the most extraordinary ordinary
moment on earth. The fire finds him. The dark sky holds him.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Upper sky / zenith              — deep brand indigo: #211F54
  Mid sky                         — nebula purple: #7B2FD8
  Lower sky / horizon             — lavender mist: #C5AAFF
  Fire installation glow          — golden orange: #FFB067
  Warm horizon ember              — flamingo: #FFBFC0
  Desert floor in fire glow       — warm dark: #0D0B1E with amber edge

Mood:
  Alone in the middle of everything, and exactly right about it.

Lighting:
  Blue hour dual-source lighting:
    1. AMBIENT SKY: deep cool blue-indigo from above, wrapping the
       scene in the brand's darkest tone. Fills shadows with cool
       purple-blue — never cold grey, always warm indigo.
    2. FIRE INSTALLATION: warm orange point-light source from
       background, camera-right or camera-left at distance.
       Casts a warm amber-orange rim on subject's far shoulder,
       side of face, and the edges of the vest/overshirt.
       Creates a warm-cold split on the subject's body:
         Near side (facing camera): cool lavender-blue ambient
         Far side (facing fire): warm amber #FFB067 rim glow
    3. Desert floor: dark with a warm amber reflection from the
       distant fire — visible in the foreground as a low warm pool.
  Sky gradient bottom to top:
    Warm ember at horizon #FFBFC0 → lavender #C5AAFF →
    nebula purple #7B2FD8 → deep indigo #211F54 at zenith.
  Dust haze: present but thinner than golden hour — glows cool
    purple-blue in the ambient sky light, with warm amber edges
    near the fire installation.
  Never: artificial neon, club lighting, cold blue without warmth,
    flat moonlit look, overexposed fire.

Composition:
  Format: 3:4 vertical (1080×1350)
  Camera: eye level to low — intimate. Subject fills center of frame.
    Sky occupies upper 35–45%, giving the indigo room to breathe.
  Subject: center frame, waist-up. Slightly turned — 3/4 angle,
    not fully frontal. One shoulder toward the fire source catches
    the warm rim. Face in cool ambient light, partially lit.
    Eyes: forward into the distance, or slightly downward — present,
    internal. Never at camera.
  Background: fire installation or flame sculpture visible as a
    warm orange bokeh glow in the mid-distance background, slightly
    off-center. Art car silhouette possible in far background.
  Depth layers:
    Subject sharp → flat dark desert floor → fire glow mid-bokeh →
    distant installation silhouette → gradient sky
  Dust: a fine haze at ankle level catching the warm fire glow,
    and faint cool purple dust above.
  Never: subject looking at camera, crowds, sharp background elements,
    bright festival lights, artificial LED strips.

Outfit:
  Wide-leg linen trousers — ivory or warm white, slightly dusty
  Open structured vest — dark charcoal or deep olive, worn over:
  Sheer or gauze overshirt — open, catching the ambient light
  Multiple layered gold chains — 3–4, varying lengths
  Leather wrist cuff — worn, aged
  Statement belt — wide leather or woven, earthy tone
  Boots — worn leather ankle boots, dusty
  Hair: natural, wind-tousled, slightly damp from the night air
  Skin: dust particles visible on forearms and collarbone,
    warm amber rim light catching the dust on skin

Expression / Body language:
  Still. Present. Internal.
  Not performing — inhabiting.
  Slight chin tilt, shoulders relaxed, arms loose at sides or
  one hand in trouser pocket.
  The fire is behind him. He knows it's there. He doesn't turn.

Texture:
  35mm film, Kodak Portra 400 pushed — allow the sky indigo and
  the fire orange to be fully saturated. The brand's darkest and
  most dramatic palette in full expression.
  Grain slightly more pronounced in shadows — adds depth and mood.
  Skin: warm amber rim on dust-kissed surface — real texture,
  no airbrushing, the desert is visible on him.
  Never: clean digital sharpness, over-processed shadows, HDR,
    plastic skin, styled hair, spotless outfit.

Do NOT:
  - Text, typography, logos, or graphic overlays
  - Subject looking at camera
  - LED strip lights or artificial neon
  - Crowds in focus
  - Clean pristine outfit and hair
  - Flat sky with no gradient
  - Fire so bright it blows out — it should glow, not flash
  - Costume look — this is fashion editorial in a desert
  - Urban or modern background elements
  - Cold grey shadows — shadows are warm indigo, always
---
```

---

## Generation Prompt

```
cinematic blue hour photograph of a chic young man standing alone on the
Black Rock Desert playa at Burning Man dusk, waist-up framing, 3/4 angle
slightly turned, camera at eye level, sky dominates upper frame in deep
indigo-to-lavender-to-warm-ember gradient, distant fire sculpture or flame
installation visible as a warm amber-orange bokeh glow off to one side in
the mid-background, warm amber rim light from the fire catching his far
shoulder and jaw edge, near side of face lit by cool lavender-blue ambient
sky, outfit: wide-leg ivory linen trousers slightly dusty, open dark
structured vest over sheer gauze overshirt open, multiple layered gold
chains 3-4 lengths, worn leather wrist cuff, statement leather belt,
worn dusty ankle boots, hair natural and wind-tousled, fine desert dust
visible on forearms and collarbone skin, eyes forward into the distance
never at camera, posture still and present, fine purple-blue dust haze
at ground level with warm amber edge near fire source, sky gradient from
warm flamingo ember at horizon rising through lavender through nebula
purple to deep indigo-black at zenith, flat dark desert floor with warm
amber reflection pool from distant fire, Kodak Portra 400 35mm film grain
pushed slightly, natural realistic skin texture, authentic Burning Man
playa mood, no text no logos no crowds
```

**Negative prompt:**
```
text, typography, logos, looking at camera, posed stock photo, clean styled
hair, spotless outfit, LED neon strips, crowds in focus, flat grey sky,
cold blue without warmth, HDR, over-sharpened digital, airbrushed plastic
skin, costume look, bright overexposed fire, urban background, indoor,
cheerful expression, forced smile
```

---

## CLI Usage

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-burningman-blue-hour.md \
  --num 3 \
  --aspect 3:4
```

## Reference Files
- `assets/moodboard/color/color-03-seascape-dusk.png` — full brand palette in one frame: purple, pink, gold, lavender
- `assets/moodboard/color/color-01-mountain-sunrise.png` — warm-to-purple gradient with silhouette depth layers
- `skills/image-ad-generator/output/hoian_angle_low.png` — low angle subject authority reference
