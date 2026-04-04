# ART DIRECTION — Hội An Coffee Solo
> Skill: `/image-ad-generator` | Format: 3:4 | Platform: Instagram Feed
> Brief: Solo sport-chic traveler, lantern-lit alley café, Hội An Vietnam, golden hour

---

## Concept Brief

A narrow alley in Hội An's old town. Worn mustard-yellow walls. Silk lanterns
hanging in strings above. A solo traveler at a small café table — cà phê phin
dripping slowly, phone on the table, eyes on nothing in particular.
The street breathes around them. A motorbike blurs past in the background.
They are unhurried. This is the whole point of the trip.

---

## Art Direction

```
ART DIRECTION
---
Palette:
  Hội An yellow (walls)           — worn mustard: #D4A843
  Lantern warm glow               — amber: #FFB067
  Deep alley shadow               — warm dark indigo: #211F54
  Outfit linen                    — natural sand: #C8B99A
  Coffee glass / ceramic          — warm ivory: #F5F4FF
  Sky glimpse above               — pale warm haze: #E8E0D0

Mood:
  The afternoon that had no plan and became the best one. Slow coffee,
  slow street, slow everything. The lanterns do the rest.

Lighting:
  Late afternoon golden hour — low sun entering the alley from one end,
  casting a warm shaft of directional amber light across the subject
  from camera-left or behind. Lanterns above add a secondary warm glow
  that wraps the scene in amber. Alley walls reflect warm yellow-gold
  back onto skin and outfit. Upper alley: a glimpse of pale warm sky
  between rooftops. Shadows in the alley are warm brown-indigo — never
  cold or blue. The cà phê phin glass catches the light.
  Never: cold white light, harsh overhead, flash, studio.

Composition:
  Format: 3:4 vertical (1080×1350)
  Camera: slightly elevated, 30° angle — as if from a standing passerby
    glancing down at a seated subject. Intimate but not intrusive.
  Subject: seated at a small café table, center-left frame, waist-up.
    One hand loosely on the table or around the coffee glass.
  Alley: recedes behind the subject — yellow walls narrowing, lanterns
    strung above, softly blurred motorbike or pedestrian mid-distance.
  Coffee: cà phê phin setup in lower frame — glass with drip filter on
    top or finished condensed milk layer visible at bottom.
  Depth layers: subject sharp → alley mid-bokeh with lanterns as warm
    bokeh orbs → far alley full bokeh.
  Never: wide full-body, subject looking at camera, symmetrical framing,
    tourist crowds in sharp focus.

Outfit:
  Tapered light linen jogger trousers — natural sand #C8B99A or warm white
  Clean fitted white tee — always white
  Unstructured linen shirt open — worn loosely, ecru or pale olive
  Fine single gold chain at neckline
  Clean minimal sneakers or simple leather sandals
  Hair: natural, relaxed — short or medium length, slightly tousled

Coffee detail:
  Cà phê phin — traditional Vietnamese metal drip filter sitting on top
    of a small glass, condensed milk visible as a creamy layer at the
    bottom, or finished and stirred
  OR: iced version — tall glass, dark coffee over ice, condensed milk
    swirling, small spoon resting on the rim
  Small ceramic side dish or local napkin on the table
  No branded items, no paper cups, no takeaway

Expression:
  Soft gaze — looking at the coffee, at the alley, or at nothing in particular.
  Slight lean — elbow on table, relaxed. Not performing. Just existing.
  Never: forced smile, direct camera look, alert stock-photo posture.

Texture:
  35mm film, Kodak Portra 400, warm grain.
  Alley walls: slightly faded, textured plaster — real not pristine.
  Skin: warm amber glow from reflected wall light — sun-kissed, natural.
  Lanterns: soft warm bokeh orbs of amber and gold in background.
  Never: HDR, oversaturated, over-sharpened, plastic skin, heavy preset.

Do NOT:
  - Text, typography, logos, or graphic overlays
  - Subject looking at camera
  - Takeaway or branded cups
  - Tourists in sharp focus in background
  - Cold or blue lighting in alley shadows
  - Over-cleaned or pristine walls — Hội An's charm is the worn texture
  - Full-body wide shot
  - Forced expression
---
```

---

## Generation Prompt

```
candid slightly elevated photograph of a solo sport-chic young man seated
at a small outdoor café table in a narrow Hội An alley, Vietnam, waist-up
framing, relaxed posture with elbow on table, soft gaze looking at his
coffee or into the middle distance, never looking at camera, outfit:
tapered natural linen jogger trousers, clean white fitted tee, unstructured
ecru linen shirt worn open, fine gold chain, minimal clean sneakers,
traditional Vietnamese cà phê phin drip coffee setup on table with
condensed milk layer visible in glass, small ceramic side piece, worn
mustard-yellow plaster walls of Hội An old town on both sides, silk
lanterns strung above the alley creating warm amber bokeh orbs in upper
frame, soft motorbike blurred in far background, late afternoon golden
hour light entering the alley from one end creating warm directional
shaft across subject, alley shadows warm brown not cold, pale warm sky
visible above rooftops, natural warm skin tones, Kodak Portra 400 35mm
film grain, shallow depth of field, authentic Southeast Asia travel mood,
no text no logos
```

**Negative prompt:**
```
text, typography, logos, looking at camera, forced smile, posed, stock photo,
airbrushed skin, neon, HDR, oversaturated, cold blue shadows, takeaway cup,
branded cup, tourists in sharp focus, full body wide shot, pristine clean
walls, heavy filter, plastic skin
```

---

## CLI Usage

```bash
python3 skills/image-ad-generator/scripts/generate.py \
  --visual visuals/art-direction-hoian-coffee-solo.md \
  --num 3 \
  --aspect 3:4
```

## Reference Files
- `skills/image-ad-generator/output/kyoto_street_jeans_1.png` — alley composition and natural film tone reference
- `skills/image-ad-generator/output/terrace_trio_natural_3.png` — coffee table detail and warm ambient light
