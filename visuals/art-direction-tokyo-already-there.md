# ART DIRECTION — Tokyo "Already There"
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Concept: C — Anti-editorial, real traveler, sport-chic
> Reference image: `skills/image-ad-generator/output/ad_candidate_2.png`
> References: `assets/moodboard/tokyo/`, `assets/moodboard/sport_chic/`

---

## Concept Brief

A sport-chic traveler standing centered on the Shibuya Sky observation deck
glass escalator. Arms slightly open — not posed, just present. The city of
Tokyo wraps around her through floor-to-ceiling glass on all sides. She is
not looking at the camera. She is already there. The image says: this is not
a dream destination. This is a Tuesday in October for someone who moves freely.

Brand copy overlay ("Already there." / "Explore") is applied post-generation
as a typography layer — not baked into the image prompt.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Leggings      — sage green: #8FAF8F
  Crop top      — white: #F5F4FF
  Blazer        — ecru/beige: #EDE8DC
  Gold accent   — jewelry + escalator rail: #FFB067
  Sky horizon   — flamingo pink: #FFBFC0
  Sky upper     — deep indigo: #211F54 → nebula purple: #7B2FD8
  City grid     — warm amber wash: #FFB067 at low opacity
  Glass panels  — cool silver-blue: #8DC8F5 tinted

Mood: The moment you stop being a tourist and start being somewhere.

Lighting:
  Golden hour — low sun behind and slightly to camera-right, visible
  through the glass panels as a warm amber bloom on the horizon.
  Flamingo pink and soft coral bleeding upward into the sky.
  Upper frame transitions from flamingo pink → nebula purple → deep indigo.
  Warm rim glow on subject's hair, shoulders, and gold chains.
  Glass panels catch and scatter the warm light as clean reflections.
  Tokyo city grid below is amber-washed — warm, infinite, detailed.
  Temperature split: warm lower two-thirds / cool purple upper third.
  Never: harsh overhead light, flat studio fill, cold desaturated tones.

Composition:
  Format: 3:4 vertical (1080×1350)
  Crop: full-body centered — the glass tunnel demands full height
  Camera angle: eye-level to slightly low — subject fills center axis
  Subject placement: perfectly centered — symmetric glass tunnel frames her
  Depth layers:
    1. Subject sharp (f/2.8 equivalent)
    2. Glass escalator architecture — mid-sharp, leading lines converging
    3. Tokyo skyline — full detail, warm bokeh at edges
    4. Sky — flamingo to indigo gradient, clean
  Leading lines: escalator rails and glass panel frames converge to
    subject as vanishing point. Symmetric tunnel creates natural vignette.
  Environment: Shibuya Sky observation deck — glass-enclosed escalator
    corridor, floor-to-ceiling transparent panels, yellow safety rails,
    city 250m below on all sides

Outfit (non-negotiable — from Sport-Chic DNA):
  1. High-waist seamless leggings — sage green #8FAF8F, no logos
  2. Fitted white athletic crop top — always white
  3. Oversized beige/ecru blazer — open, draped, never buttoned
  4. Layered thin gold chains (2–3 layers) — visible at collarbone
  5. Hair: sleek low bun, minimal loose strands
  6. Sneakers: clean white — visible but not prominent
  7. No bag, no accessories beyond jewelry

Expression & Pose:
  Arms slightly open or resting wide on the escalator rails — open,
  receptive, taking it all in. Not a power pose. Not a model pose.
  Just someone who has arrived and knows it.
  Gaze: sideways or slightly downward toward the city — never camera.
  Expression: quiet confidence, neutral-to-soft. Not smiling for the photo.

Texture:
  35mm film aesthetic, natural color grading, subtle grain.
  Glass reflections must feel real — partial city reflection in lower panels.
  Skin: warm, natural, sun-kissed. No airbrushing. Realistic texture.
  Fabric: leggings show stretch and form. Blazer has natural drape and crease.

Typography overlay (applied post-generation — NOT in image prompt):
  Headline:  "Already there."
             → Rethink Sans Bold
             → Color: #F5E264 (brand yellow)
             → Placement: bottom-right, ~8% margin from edge
             → Size: ~48–56pt equivalent at 1080px width
  CTA:       "Explore"
             → Rethink Sans Regular
             → Color: #FFFFFF
             → Placement: directly below headline, same right-alignment
             → Size: ~28pt — clearly subordinate to headline

Connecting Line (brand graphic — applied post-generation):
  Form: loose fluid open loop (brand signature)
  Color: solid yellow #F5E264 (bright photography variant)
  Placement: upper-left quadrant, partially bleeding off frame
  Scale: large — occupies roughly 25–30% of frame width
  Never: used as a border, underline, or structural element

Do NOT:
  - Text or graphic elements inside the image generation prompt
  - Cyberpunk or neon Tokyo aesthetic
  - Shibuya crossing street level (this is sky-level only)
  - Direct camera gaze
  - Forced smile or stock-photo expression
  - Logos on any garment
  - Oversaturated HDR treatment
  - Cold blue desaturated tones
  - Full crowd or busy background — city must feel vast, not chaotic
  - Matching outfit colors to background sky tones
---
```

---

## Generation Prompt

```
Cinematic travel photography, fit young woman mid-20s with toned athletic
physique, glowing warm sun-kissed skin, sleek hair pulled back in a low bun,
wearing high-waist sage green seamless leggings, fitted white athletic crop
top, oversized beige blazer draped open, layered thin gold chains at collarbone,
clean white sneakers. Standing perfectly centered on the Shibuya Sky glass
observation deck escalator corridor in Tokyo, arms resting open on the
escalator handrails, gaze turned sideways toward the cityscape, quiet
confidence, not posing for camera. Floor-to-ceiling glass panels on all sides
reveal Tokyo city grid 250 meters below — warm amber-washed, vast, infinite.
Glass escalator architecture creates perfect symmetric tunnel framing with
leading lines converging to subject. Golden hour sunset light — warm amber and
flamingo pink at horizon through glass, sky transitioning from flamingo pink
to nebula purple to deep indigo at the top of frame. Soft warm rim glow on
subject's hair and gold jewelry from low sun behind. Tokyo cityscape in full
detail, warm light across the city grid, yellow escalator safety rails echo
the golden tones. Real traveler energy — candid, present, self-assured.
35mm film aesthetic, natural color grading, realistic skin texture, cinematic
depth of field, symmetric architectural composition, magazine quality
```

**Negative prompt:**
```
text, typography, logos, graphic overlays, looking at camera, forced smile,
stock photo expression, over-posed, neon signs, cyberpunk, street level,
crowds, dark background, cold blue tones, harsh shadows, flat lighting,
airbrushed skin, HDR oversaturation, illustration, CGI, cartoon, indoor
studio, matching outfit to sky color, full face frontal gaze
```

---

## CLI Usage

```bash
# Generate 3 candidates at 3:4
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-tokyo-already-there.md \
  --num 3 \
  --aspect 3:4
```

---

## Reference Files

| File | Role |
|------|------|
| `skills/image-ad-generator/output/ad_candidate_2.png` | Approved composition reference — iterate from this |
| `assets/moodboard/tokyo/tokyo_elevator_6.jpg` | Silhouette at golden hour — color and mood target |
| `assets/moodboard/tokyo/tokyo_elevartor_5.jpg` | Escalator at sunset — light and drama target |
| `assets/moodboard/sport_chic/color_v1_sage.png` | Sage green outfit — canonical color reference |
| `assets/moodboard/sport_chic/p2_angle_2.png` | Low angle authority — composition reference |
| `assets/moodboard/sport_chic/summer_proposal_2.png` | Canonical sport-chic mood reference |
