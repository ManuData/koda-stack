# ART DIRECTION — Instagram Ad: Light Through Stone (Concept B)
> Skill: `/concept` | Format: 3:4 | Platform: Instagram Feed

---

## Concept Brief

A single editorial hero image for a luxury Instagram ad. No text. No logo. No CTA. The Connecting Line is the sole brand identifier. A Moorish archway, riad doorway, or ancient stone corridor flooding with a dramatic diagonal shaft of golden light. A figure is partially caught in the beam — a hand, a shoulder, a turning face. The Connecting Line follows the diagonal of the light, large and flowing, as if the brand is made of the same material as the light.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  #211F54 — Deep Space Indigo (shadowed stone walls, upper frame)
  #7B2FD8 — Avelsky Purple (deep shadow areas, architectural depth)
  #FFB067 — Golden Orange (light shaft, illuminated stone, skin warmth)
  #FFBFC0 — Flamingo Pink (Connecting Line gradient start, warm shadow transition)
  #F5E264 — Sunrise Yellow (Connecting Line gradient end, brightest light point)
  #C5AAFF — Lavender Mist (cool shadow areas, upper stone)

Mood: The hush of stepping into a place that was beautiful long before you arrived,
      and will be beautiful long after. Architectural sensuality — light as structure,
      space as emotion.

Lighting:
  Single dramatic diagonal shaft of golden light entering from upper right.
  Light source: sun through a high window, archway opening, or gap in ancient stone.
  Light shaft angle: approximately 45 degrees from upper right to lower left.
  Illuminated areas: warm golden amber (#FFB067) — stone texture, floor, partial figure.
  Shadow areas: deep indigo-purple (#211F54) and lavender (#C5AAFF) — rich, not flat.
  The contrast between light shaft and deep shadow is the drama.
  No fill light in shadows — let them fall to dark purple-grey for depth.
  No artificial light. No flash. Pure atmospheric single-source.

Composition:
  3:4 portrait (1080×1440).
  Interior-to-exterior OR corridor shot with strong architectural framing.
  Diagonal light shaft cuts across the frame from upper right to lower left.
  Figure partially in silhouette, partially caught in the beam — suggestion of a person,
  not a portrait. A hand, a bare shoulder, a turning face edge, or a walking silhouette.
  Figure occupies no more than 30% of the frame — architecture and light dominate.
  Stone texture fills the frame — aged plaster, marble, terracotta, or carved stone.
  Deep shadows in upper left and lower right anchor the composition.
  Connecting Line follows and amplifies the diagonal of the light shaft,
  bleeding off upper-right and lower-left corners simultaneously.

Environment:
  Moorish archway, riad interior doorway, ancient stone corridor, or hammam entrance.
  Stone walls with visible texture — aged plaster, carved detail, terracotta tile, or marble.
  Architecture suggests North Africa, Southern Europe, or Middle East — ancient, refined.
  No modern furniture, no hotel branding, no visible signage.
  The space feels timeless — could be any century.

Texture:
  Stone grain and texture are critical — this image is partly about surface.
  Skin where visible: warm, naturally lit by the golden shaft.
  No film grain. Ultra clean luxury editorial quality.
  Connecting Line has subtle luminosity — glows slightly against the deep shadow areas.

Connecting Line (graphic overlay):
  Gradient version: flamingo pink (#FFBFC0) → golden orange (#FFB067) → sunrise yellow (#F5E264).
  Form: loose, fluid open loop — not a closed shape, not a border, not an underline.
  Scale: large — spans the full diagonal of the frame.
  Position: follows the diagonal of the light shaft, upper right to lower left,
  bleeding off both corners. Feels like the light and the line are the same force.
  Applied on top of photography layer, luminous against shadow areas.

NO TEXT of any kind:
  No headline. No CTA. No logo. No caption. No watermark.
  The Connecting Line is the only brand element.

References:
  1. VISUAL_DNA.md — color-01-mountain-sunrise.png (warm-to-cool contrast, silhouette depth)
  2. VISUAL_DNA.md — branding-02-connecting-line-buyer-persona-woman-travel.png (line as graphic companion)
  3. Julius Shulman — architectural light photography, light as structure
  4. Kengo Kuma — space as emotion, material sensitivity

Do NOT:
  - Any text, type, headline, logo, watermark, or caption overlay
  - Even, flat, or diffuse lighting — the shaft must be dramatic and directional
  - Modern interiors, hotel lobbies, contemporary furniture
  - Visible signage, branding, or logos on architecture
  - Subject as the primary focus — light and architecture lead
  - Connecting Line as a border, underline, or small decorative element
  - Film grain or heavy post-processing
  - Neon or oversaturated colours without gradation
  - Figure larger than 30% of frame
```

---

## Generation Prompt

```
Cinematic luxury editorial photograph inside an ancient stone corridor or Moorish archway,
a dramatic diagonal shaft of golden sunlight (#FFB067) cuts from upper right to lower left
across aged stone walls with rich visible texture — carved plaster, marble, or terracotta,
a solitary figure partially caught in the light beam — only a bare shoulder, turning face edge,
or silhouetted form visible, occupying no more than a third of the frame,
deep indigo-purple shadows (#211F54) fill the unlit areas creating extreme contrast,
the stone architecture feels ancient, timeless, North African or Southern European,
ultra realistic, luxury editorial photography, cinematic and atmospheric, 3:4 portrait.

Overlay: large fluid open-loop curve graphic in gradient flamingo pink to golden orange
to sunrise yellow, following the diagonal of the light shaft from upper right to lower left,
bleeding off both corners of the frame, luminous glow against the deep shadow areas,
scale spans the full diagonal of the frame.

No text, no typography, no words, no logo, no watermark, no signage anywhere in the image.
```

**Negative prompt:**
```
text, typography, words, headline, logo, watermark, caption, label, signage,
modern interior, hotel lobby, contemporary furniture, flat lighting, even lighting,
neon colours, overprocessed skin, film grain, filters, heavy vignette,
closed loop graphic, border graphic, underline, small decorative line,
large prominent figure, portrait, close-up face, posed subject,
visible brand names, price tags, modern architecture
```

**Model:** Imagen 4 (Gemini API)
**Settings:** 3:4 | 1080×1440 | photorealistic | luxury editorial quality
**Output:** `skills/image-ad-generator/output/`
