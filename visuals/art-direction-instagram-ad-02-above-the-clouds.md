# Art Direction — Instagram Ad 02: Above the Clouds

> Concept: A male traveler at altitude, face turned upward, sky as protagonist.
> Pipeline: /brief → /concept C → /art-direction → /generate
> Status: Ready for generation

---

## Brief

```
Topic: eSIM for travelers — stay connected without friction
Angle: The freedom of a traveler who never thinks about connectivity —
       he's just fully present in the experience
Audience: Young adventurous men, 20-35, who prioritize experiences
          over logistics
Platform: Instagram (feed ad)
Format: Single image, 4:5 (1080×1350)
Tone: Bold, optimistic, companion-like — warm but sophisticated
Key message: You're already connected. Go further.
Constraints: No CTA text. No product in frame. Inspirational only.
             Brand visual language (Connecting Line) must be present.
```

---

## Art Direction

```
Palette:
  #0D0B1E — Near-black indigo (dominant sky, upper frame)
  #211F54 — Deep Space Indigo (mid-sky, atmospheric depth)
  #7B2FD8 — Avelsky Purple (sky gradient transition zone)
  #C5AAFF — Lavender Mist (cloud tones, diffused light)
  #FFBFC0 — Flamingo Pink (cloud edges catching warm light)
  #FFB067 — Golden Orange (horizon glow, skin rim light)

Mood: Quiet awe — the stillness you only find when you're far from
      everything familiar, and realise that's exactly where you belong.

Lighting: Natural golden hour from below the horizon, camera left
          at 30 degrees. Warm golden-orange (#FFB067) rim light
          catches the left edge of the subject's face and shoulder.
          The sky behind transitions cool — lavender to deep indigo
          at the top. No fill light. Shadows stay deep purple-grey
          (~#2D2535). Light source is the horizon, not the sun directly.

Composition: Low angle looking up. Subject occupies lower 25% of
             frame — grounded, small against the sky. Face turned
             upward or slightly away, expression open and still.
             Sky owns 70% of the frame. Shallow DOF — subject
             sharp, clouds softly diffused. Slight upward Dutch
             tilt (5°) to give the sky tension and scale.
             Format: 4:5 (1080×1350) for Instagram feed.

Environment: Mountain summit or high-altitude ridge at golden hour.
             Clouds at or below eye level — he is above them.
             Distant peaks fading into purple haze. No urban
             elements. No visible technology. Pure altitude.

Texture: Real photographic grain (ISO 800 equivalent). Slightly
         matte finish — not glossy. Atmospheric haze adds
         natural diffusion to background. No HDR over-processing.

Typography: None in this image. Visual speaks alone.

Connecting Line: Large fluid open curve in gradient
                 (flamingo pink #FFBFC0 → golden orange #FFB067
                 → sunrise yellow #F5E264). Positioned upper-right,
                 arcing from top edge and bleeding off the right
                 frame. Scale: spans at least 50% of frame width.
                 Sits above the photography layer, semi-transparent
                 at 85% opacity where it crosses the sky.

References:
  1. Chris Burkard — high-altitude surf & adventure photography
     (color temperature split, small figure vs vast environment)
  2. Patagonia Fall 2022 campaign — real skin, real altitude,
     no retouching
  3. Sony "Xperia" brand photography 2021 — sky as protagonist,
     human as anchor

Do NOT:
  - Fake HDR or oversaturated skies
  - Pose the subject — he should look like he was caught, not directed
  - Use neon or artificial light sources
  - Place the Connecting Line symmetrically or centered
  - Add any text, logo, or product in frame
  - Use a blue sky — the palette is indigo/purple, not daylight blue
```

---

## Generate

```
SHOT 01
---
Prompt: Young man at high-altitude mountain summit, low camera angle
        looking up, subject occupies lower quarter of frame, face
        turned slightly upward with calm open expression, golden rim
        light from camera-left catching left cheekbone and shoulder
        edge, sky dominates 70% of frame, clouds sit at or below
        eye level in soft lavender and flamingo pink tones, sky
        graduates from deep indigo #0D0B1E at top through nebula
        purple #7B2FD8 to warm golden-orange glow at horizon,
        distant mountain peaks fading into purple atmospheric haze,
        shallow depth of field, subject sharp, clouds softly diffused,
        slight upward 5-degree dutch tilt, natural photographic grain
        ISO 800, matte finish, no HDR, editorial travel photography,
        ultra realistic, photograph quality

Negative prompt: Neon lights, artificial lighting, blue daylight sky,
                 oversaturated HDR, posed expression, stock photo feel,
                 city elements, phone or device visible, text, logo,
                 flat lighting, symmetrical composition, glossy finish,
                 smooth noiseless skin

Model: Nano Banana (nano-banana.ai, Gemini-powered)

Settings:
  Aspect ratio: 4:5 (1080×1350px)
  Style: Photorealistic / editorial
  Quality: High
  Guidance: High fidelity to prompt

Output: visuals/shot-01-above-the-clouds.png
---
```

---

## Post-production note

The Connecting Line is a brand graphic overlay — add it after generation in your editing tool (Figma, Photoshop, or Final Cut Pro):
- Form: Large fluid open curve, upper-right quadrant, bleeding off right edge
- Color: Gradient left-to-right — flamingo pink #FFBFC0 → golden orange #FFB067 → sunrise yellow #F5E264
- Opacity: 85% where overlapping sky
- Scale: Minimum 50% of frame width
- Reference: `assets/moodboard/branding/branding-01-connecting-line-buyer-persona-sea-summer.png`
