# Image Briefs — Tier 7 / Customs & Classification Cluster

**Six images: 3 heroes + 3 infographics.** Rewritten 31 August 2026 after the first set generated poorly.

> **Read `IMAGE-STYLE-GUIDE.md` first.** It is the standing rule set and overrides anything here.

---

## Why the previous prompts failed, so we stop repeating it

The old prompts were each a **single dense paragraph of 170 to 229 words** carrying nine to thirteen sentences and twenty-plus separate requirements. OpenAI's own guidance for their image models says to do the opposite:

| Their guidance | What the old prompts did |
|---|---|
| Use **labeled segments or line breaks**, not one dense paragraph | One unbroken paragraph, every time |
| Order as **scene → subject → details → constraints** | Opened with camera jargon, subject buried behind it |
| Listing twenty requirements causes the model to **drop several** | Twenty-plus requirements per prompt |
| Put in-image text **in quotes**, specify typography, keep layouts light | Up to ten separate text strings on one canvas |

One assumption I had was wrong and worth stating: **negative constraints do work here.** OpenAI explicitly recommends stating exclusions like "no watermark, no extra text, no logos". So the `EXCLUDE:` line stays, and it earns its place.

**On dimensions.** I could not verify GPT Image 2's exact supported size and aspect-ratio table from a source I trust, and the community lists contradict each other. So these briefs no longer ask for an exotic ratio directly. **Generate at a common ratio, then crop.** That works regardless of what the model supports natively, and a 27:10 banner was almost certainly never a native output size.

**Work one at a time.** Generate, look, change one thing, regenerate. Do not tweak four things at once.

---

## Conventions

| | |
|---|---|
| **Format** | `.webp`, sRGB |
| **Heroes** | generate **16:9 at 2K**, then crop to **2070×760**, the size the existing library uses. Keep the focal object dead centre; the crop is a narrow strip |
| **Infographics** | generate **2:3 or 3:4 portrait at 2K**, then resize to **1200×1500**. Use the highest quality setting: small text needs it |
| **Palette** | site navy `#0d2144`, accessible orange `#c25205`, logo orange `#DD7008`, logo teal `#2B677A`, warm greys, white |
| **Upload to** | `images/blog/`, exact lowercase filenames |

The three posts are staged `noindex`, out of `sitemap.xml`, with no blog card. These images complete them.

---

# HEROES

**Style lock, read before generating any of the three.**

These are **not photographs.** They are conceptual 3D renders on a deep navy ground, matching `images/blog/amazon-fba-inbound-placement-fees-2026.webp`, which is the best hero in the existing library and the only one that looks like it belongs to this site.

Every hero shares this base. It is repeated in each prompt so you can paste them independently:

| | |
|---|---|
| Ground | Deep navy `#0d2144` fading to near-black `#001830`, with a faint darker grid |
| Objects | Matte 3D rendered, soft studio lighting, gentle contact shadows |
| Accent | Saturated orange `#DD7008` |
| Semantics | Green `#16a34a` = correct or lawful. Red `#d02222` = wrong or penalised |
| Highlight | A glowing cyan-blue rim light or ring on the focal object |
| Feel | Editorial tech diagram, high contrast, saturated. Not a photo, not a flat icon |

**What killed the previous attempts:** they asked for photographic realism with "warm neutral greys and one restrained orange accent". That is a recipe for a beige stock photo that shares no colour with the website. Navy ground, orange accent, saturated. Bold beats tasteful here.

---

## 1. `tariff-engineering-legal-line-2026.webp`

**Alt:** "A product designer and a customs document side by side, showing how a physical product change alters its tariff classification at the border"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black at the edges, with a faint darker grid. A vertical glowing cyan-blue seam of light runs down the exact centre, splitting the frame into two halves.

LEFT HALF: A matte 3D trainer floating in three-quarter view, its thick textured outer sole clearly visible and rendered in a contrasting material. It sits inside a glowing green ring with a green tick mark.

RIGHT HALF: A matte 3D cargo van floating in three-quarter view. A single seat rises out of it on a curved orange arrow, lifting away. It sits inside a glowing red ring with a red cross.

STYLE: 3D product visualisation, matte materials, soft studio lighting, gentle contact shadows, saturated and high contrast. Wide horizontal composition, both objects at equal size and equal height.

EXCLUDE: no text, no watermark, no real brand logos, no recognisable shoe or vehicle models, no photographic backgrounds, no people, no beige or warm grey.
```

---

## 2. `hts-classification-mistakes-importers-2026.webp`

**Alt:** "A warehouse operator recording fibre content, materials and weights at intake, the product attributes that determine HTS classification and duty"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black, with a faint darker grid.

CENTRE: A single kraft-brown 3D carton sits on a glowing orange disc, a small blank tag hanging from its side. A cyan-blue ring of light surrounds it.

DIVERGING PATHS: Two thick arrows leave the carton and curve outward. The upper arrow is green and leads to a short stack of three gold coins. The lower arrow is red and leads to a tall stack of nine gold coins, noticeably higher.

FLOATING AROUND: Five small matte 3D objects orbit the carton at a distance, evenly spaced: a folded garment, a trainer, a closed gift box, a cog, and a battery cell.

STYLE: 3D product visualisation, matte materials, soft studio lighting, saturated and high contrast, editorial tech diagram. Wide horizontal composition, carton dead centre.

EXCLUDE: no text, no numerals, no watermark, no real brand logos, no photographic backgrounds, no people, no beige or warm grey.
```

**Why the carton is centred:** the hero crops to a wide strip. Anything important near the edges is lost.

---

## 3. `cbp-binding-ruling-guide-2026.webp`

**Alt:** "An importer preparing a binding ruling request with product samples, specifications and photographs laid out ready for submission to CBP"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black, with a faint darker grid. A left-to-right progression across the frame, joined by a thick orange arrow.

LEFT: A dim grey 3D document sheet floating at a slight angle, with a large glowing orange question mark hovering above it. Low light, muted.

CENTRE: A glowing cyan-blue circular portal ring, edge on, that the orange arrow passes through.

RIGHT: A brightly lit 3D document sheet, crisp and white, carrying a raised circular orange embossed disc in its lower corner. A green tick floats beside it. This side is the brightest point in the image.

STYLE: 3D product visualisation, matte materials, soft studio lighting, saturated and high contrast, editorial tech diagram. Wide horizontal composition with a clear dark-to-bright gradient left to right.

EXCLUDE: no text, no readable writing on the documents, no government seals or crests, no agency badges, no eagle or shield emblems, no watermark, no real brand logos, no people, no beige or warm grey.
```

**On the embossed disc:** plain and abstract, an orange circle with a raised rim. If it starts resembling an official government seal, regenerate. It represents certainty, not a specific agency.

---

# INFOGRAPHICS

Text load is deliberately cut. The old versions asked for up to ten separate strings on one canvas, which is where character accuracy fell apart. These ask for five or six.

Set every quoted string **exactly**. Check every digit before uploading.

## 4. `infographic-tariff-engineering-line.webp`

**Alt:** "The tariff engineering line: Converse adds felt to outsoles and sells the shoe it imported, which is lawful, while Ford imported vans with seats removed at the port and settled for 365 million dollars, which is artifice"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, split into two stacked halves separated by a thin horizontal rule.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "WHERE THE LINE SITS".

TOP HALF: A green rounded card with a white check icon. Bold dark navy heading reading exactly "LAWFUL". Below it one grey line reading exactly "The customer receives what was imported".

BOTTOM HALF: A dark red rounded card with a white cross icon. Bold dark navy heading reading exactly "ARTIFICE". Below it one grey line reading exactly "The change is undone at the port".

FOOTER: A deep navy band across the bottom with white bold text reading exactly "$365 MILLION SETTLEMENT".

TYPE: Modern geometric sans-serif. Large type, high contrast, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no brand logos, no recognisable shoe or vehicle models, no extra text beyond the strings specified.
```

## 5. `infographic-classification-traps.webp`

**Alt:** "Five categories where HTS classification most often goes wrong: apparel by fibre percentage and knit or woven, footwear by upper and sole material and ankle coverage, retail sets by essential character, parts versus accessories governed by chapter notes, and products with batteries"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, a single column of five evenly spaced rounded white cards with thin light grey borders.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "FIVE CATEGORIES THAT GO WRONG".

CARDS: Each card has a simple two-colour line icon on the left and one bold dark navy word beside it. The five read exactly, top to bottom: "APPAREL", "FOOTWEAR", "RETAIL SETS", "PARTS", "BATTERIES".

ICONS: In the same order, a folded garment, a shoe outline, a gift box, a gear, a battery cell. Line icons only, orange and navy.

FOOTER: An orange band across the bottom with white bold text reading exactly "AUDIT YOUR TOP TEN BY DUTY PAID".

TYPE: Modern geometric sans-serif. Large type, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no brand logos, no extra text beyond the strings specified.
```

**Note:** the old version put a full explanatory sentence under every heading. The detail lives in the article; the image only has to carry the five categories.

This one runs to seven strings against the guide's six, but five of them are single words and the whole canvas carries only 18 words, the lightest of the three. Word count is the constraint that matters, not string count. Leave it as is.

## 6. `infographic-binding-ruling-path.webp`

**Alt:** "The binding ruling path: search CROSS at rulings.cbp.gov first, then file through the eRulings portal, receive a control number within one business day, and expect most classification rulings within 30 calendar days, around 90 days if referred to Headquarters"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, showing a vertical four-step path. A thin navy line runs down the left with a numbered navy circle at each step.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "FROM QUESTION TO RULING".

STEPS: Four steps down the page, each with a bold dark navy heading. They read exactly, top to bottom: "SEARCH CROSS", "FILE VIA ERULINGS", "CONTROL NUMBER 1 DAY", "RULING ISSUED 30 DAYS".

FOOTER: An orange band across the bottom with white bold text reading exactly "IT BINDS CBP. IT ALSO BINDS YOU."

TYPE: Modern geometric sans-serif. Large type, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no brand logos, no extra text beyond the strings specified.
```

**Note on "ERULINGS":** if the model mangles it, spell it out letter by letter in the prompt as E-R-U-L-I-N-G-S. OpenAI recommends this for words a model gets wrong.

---

## If a generation still comes out wrong

Change **one** thing and regenerate. In rough order of what usually fixes it:

1. **Wrong warehouse look?** Move the `SCENE:` line detail earlier and cut a `DETAILS:` item. It is competing for attention.
2. **Wrong people?** Put "Chinese woman in her mid-twenties, orange polo shirt" as the literal first words of `SUBJECT:`.
3. **Garbled text?** Cut a string. Five is comfortable, eight is not. Raise the quality setting.
4. **Too busy?** Delete the whole `DETAILS:` block. These prompts survive without it.
5. **Wrong crop?** Generate square and crop, rather than asking for the banner ratio directly.

Log what worked so the next tier starts from a better base.
