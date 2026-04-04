# ART DIRECTION — Burning Man: Golden Hour Blaze
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Brief: Chic woman traveler, Black Rock Desert playa, blazing golden hour backlight

---

## Concept Brief

The playa at golden hour is the brand's color palette made real.
A woman walks through the dust — duster coat catching the wind, hair alive,
goggles pushed up. The sun is behind her. She is the silhouette. The sky is
everything the brand has always been. No crowd. No chaos. Just her and the
burning horizon.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Horizon fire                    — golden orange: #FFB067
  Lower sky / dust haze           — flamingo warm: #FFBFC0
  Mid sky                         — lavender mist: #C5AAFF
  Upper sky                       — deep brand indigo: #211F54
  Desert floor                    — warm alkali dust: #D4C5A9
  Outfit duster coat              — burnt sienna: #C4622D

Mood:
  The moment the playa becomes a cathedral — and one person knows it.

Lighting:
  Full golden hour backlight — sun positioned at the horizon directly
  behind or slightly camera-right of the subject. Low, blazing, the
  entire lower sky is on fire. Effect on subject:
    — Strong warm rim light outlining the duster coat edges, hair,
      shoulder line and ankles in pure #FFB067 gold
    — Subject's front face/chest in soft warm shadow — not black,
      lit by the ambient sky reflection off the alkali desert floor
    — Dust particles in the air between camera and subject catch
      the backlight and create a warm golden haze layer
  Sky temperature from bottom to top:
    Horizon: #FFB067 blazing → #FFBFC0 flamingo → #C5AAFF lavender →
    #211F54 deep indigo at the very top — the brand gradient, full expression.
  Desert floor: warm pale gold, flat, extending to the horizon.
  Never: midday overhead, cold light, even exposure, no dust haze.

Composition:
  Format: 3:4 vertical (1080×1350)
  Camera: low angle looking slightly upward — the sport-chic signature
    carried into the desert. Subject gains full authority against
    the burning sky. Sky dominates upper 40–50% of frame.
  Subject: center-left, waist-up to full silhouette — this is the one
    execution where a full silhouette is permitted if the rim light
    is strong enough to define the outfit.
  OR: 3/4 rear angle — subject walking away from camera toward the
    horizon, duster coat billowing behind, hair wild, sun blazing
    ahead of her. Most cinematic option.
  Depth layers:
    Subject sharp or strong silhouette → desert floor flat →
    distant art installation/fire sculpture mid-bokeh in warm haze →
    burning horizon → indigo sky
  Dust: visible as a warm haze between subject and camera, and
    kicked up faintly around feet/coat hem.
  Never: crowded frame, direct camera stare, clean still hair,
    flat gray sky, sharp background installations.

Outfit:
  Oversized duster coat — burnt sienna #C4622D or desert sand,
    open and billowing in the wind — the hero garment
  Flowing wide-leg linen trousers — ivory or pale sand
  Structured bandeau or crop top — warm white
  Layered gold and silver jewelry — chains, cuffs, rings
  Statement goggles pushed up on forehead (not covering eyes)
  Ankle boots — worn leather, dusty
  Hair: completely loose, wild from desert wind — strands
    lifting and trailing behind in the backlight

Expression / Body language:
  Walking toward the horizon or standing still facing away.
  If face is visible: eyes forward, open, present. Never at camera.
  Posture: free, unhurried, inhabiting the space completely.
  Coat hem and hair in motion — wind is the co-director here.

Texture:
  35mm film, Kodak Portra 400 slightly pushed — allow the sky
  gradient to be fully saturated here. This is the one execution
  where the brand's full color palette earns maximum expression.
  Desert floor: pale warm alkali texture, flat and vast.
  Dust haze: softens midground, adds depth and authenticity.
  Skin where visible: dust-kissed, warm, sun-struck — alive.
  Never: HDR crunching, over-sharpened, digital sterility,
    clean polished desert floor, styled hair.

Do NOT:
  - Text, typography, logos, or graphic overlays in the image
  - Subject looking directly at camera
  - Hair clean or styled — must be wind-wild
  - Crowds or other people in sharp focus
  - Grey or overcast sky
  - Clean outfit — light dust on coat hem and boots is correct
  - Goggles over eyes (they belong pushed up on forehead)
  - Matching or themed festival costume look — this is fashion,
    not costume
  - Corporate clean feeling — the playa is raw
---
```

---

## Generation Prompt

```
cinematic low-angle shot of a chic young woman walking across the Black
Rock Desert playa at Burning Man golden hour, waist-up to full figure,
camera angled slightly upward so the blazing desert sky dominates the
upper frame, she is walking toward or past the camera with her back
partially turned, oversized burnt sienna duster coat billowing open in
the desert wind, flowing ivory wide-leg linen trousers, structured white
crop top, layered gold and silver chains and jewelry, statement goggles
pushed up on forehead not covering eyes, worn dusty ankle boots, hair
completely loose and wild lifting in the wind catching the golden
backlight, strong warm rim light from blazing sun at horizon directly
behind subject outlining coat edges hair and shoulders in pure gold,
subject front lit softly by warm sky reflection off alkali desert floor,
golden dust haze in air between camera and subject catching backlight,
sky gradient from blazing orange-gold at horizon rising through flamingo
pink to lavender to deep indigo at top of frame, distant art installation
or fire sculpture as warm glowing bokeh in background, flat pale alkali
desert floor extending to horizon, Kodak Portra 400 35mm film pushed
slightly, natural dust-kissed skin, authentic Burning Man playa mood,
no text no logos no crowds
```

**Negative prompt:**
```
text, typography, logos, looking at camera, forced smile, posed stock photo,
clean styled hair, goggles over eyes, costume look, crowds in focus, grey sky,
HDR, oversaturated digital, harsh cold light, clean outfit, polished skin,
airbrushed, neon artificial light, urban background, indoor
```

---

## CLI Usage

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-burningman-golden-hour.md \
  --num 3 \
  --aspect 3:4
```

## Reference Files
- `assets/moodboard/color/color-02-beach-sunset.png` — maximum warm-cool contrast palette reference
- `assets/moodboard/color/color-03-seascape-dusk.png` — full brand gradient in one sky reference
- `skills/image-ad-generator/output/sport_chic_profile_1.png` — rim light and silhouette reference
