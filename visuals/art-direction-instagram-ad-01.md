# ART DIRECTION — Instagram Ad Hero Image
> Skill: `/art-direction` | Format: 9:16 | Platform: Instagram Feed + Stories

---

## Concept Brief

A single editorial hero image for an Instagram ad. The subject is a young woman mid-laugh, caught in an unguarded, joyful travel moment — beach or coastal environment at golden hour. The Avelsky Connecting Line graphic overlays the scene as the dominant graphic companion, large and partially bleeding off frame.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  #211F54 — Deep Space Indigo (upper sky, background anchor)
  #7B2FD8 — Avelsky Purple (mid-sky bleed, optional colour wash)
  #FFB067 — Golden Orange (horizon light, skin warmth)
  #FFBFC0 — Flamingo Pink (Connecting Line gradient start)
  #F5E264 — Sunrise Yellow (Connecting Line gradient end, typography accent)

Mood: The exact second she forgets the camera exists — warm, free, alive.
      The brand promise made visual: enjoying every moment without limits.

Lighting:
  Golden hour, horizon as single light source — warm orange-amber from camera left,
  45-degree angle hitting subject's face and shoulder.
  Upper two-thirds of frame: deep cool sky grading from cobalt → lavender → deep indigo (#211F54).
  No fill light on shadows — let them fall to dark purple-grey (~#2D2535) for silhouette depth.
  No artificial-looking light. No studio. No flash.

Composition:
  9:16 vertical (1080×1920).
  Subject placed left-of-centre, slightly low in frame — sky dominates upper half.
  Connecting Line graphic enters from right edge, loops loosely across upper-centre, partially bleeding off top-right.
  Shallow depth of field — subject sharp, background beach/sea softly blurred.
  Text block "Connecting moments" sits lower third, white, oversized — letters bleed off left and right edges.

Environment:
  Beach or coastal cliffside at golden hour. Natural water or sand visible in soft focus.
  Warm amber light on horizon. Sky transitions warm → cool as it rises.
  No props, no staged elements. Candid travel energy.

Texture:
  Clean digital — no film grain. Editorial quality. Skin tones true-to-life, not over-processed.
  Connecting Line has subtle luminosity/glow on dark areas.

Typography:
  Rethink Sans Bold.
  Primary line: "Connecting" — white, ultra-large, bleeds off frame left.
  Secondary line: "moments" — white, same weight, bleeds off frame right.
  Accent: One word or short phrase in #F5E264 (Sunrise Yellow).
  Placement: lower third, structural — text is a layout element, not a caption.

Connecting Line (graphic overlay):
  Gradient version: flamingo pink (#FFBFC0) → golden orange (#FFB067) → sunrise yellow (#F5E264).
  Form: loose, fluid open loop — not a closed shape, not a border.
  Scale: fills roughly 60% of frame width.
  Position: off-centre right, top bleeds off frame edge.
  Applied on top of photography layer, not behind subject.

References:
  1. VISUAL_DNA.md — branding-02-connecting-line-buyer-persona-woman-travel.png (line over travel subject)
  2. VISUAL_DNA.md — color-03-seascape-dusk.png (full palette: purple, pink, gold, lavender in one frame)
  3. VISUAL_DNA.md — branding-05-connecting-line-buyer-persona-fun.png (candid unguarded energy)

Do NOT:
  - Posed, stock-photo-style expressions or body language
  - Flat or even lighting anywhere in the frame
  - Neon or oversaturated single hues without gradation
  - Connecting Line used as a border, underline, or divider
  - Small or centred text — it must bleed and feel structural
  - Generic travel clichés (passport, airplane, luggage close-ups)
  - Purple (#7B2FD8) as a small accent — if present, it owns the frame
```

---

## Generation Prompt (ready for Nano Banana)

```
Candid editorial photograph of a young woman mid-laugh on a sun-drenched coastal beach,
golden hour, warm amber-orange light from camera left at 45 degrees striking her face and shoulder,
upper sky transitions from cobalt to deep indigo (#211F54), shallow depth of field,
water and sand softly blurred in background, skin tones natural and warm,
dark purple-grey shadows (#2D2535) creating depth layers,
ultra realistic, photograph, editorial quality, 9:16 vertical.

Overlay: large fluid loop graphic in gradient flamingo pink to golden orange to sunrise yellow,
positioned off-centre right, partially bleeding off top-right edge of frame,
scale fills approximately 60% of frame width, not a border or underline.

Typography lower third: "Connecting" ultra-large white Rethink Sans Bold bleeding off left edge,
"moments" same weight bleeding off right edge, one accent word in yellow (#F5E264).
```

**Negative prompt:**
```
posed, stock photo, studio light, flat lighting, neon colours, artificial colours,
symmetrical composition, centred text, small text, luggage, passport, airplane,
overprocessed skin, filters, film grain, closed loop graphic, border graphic
```

**Model:** Nano Banana (nano-banana.ai)
**Settings:** 9:16 | 1080×1920 | photorealistic | editorial quality
**Output:** `visuals/shot-01.png`
