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

## Two rules that override everything else

**1. Bright objects on the dark ground.** The ground is deep navy. Every object therefore has to be **light**: kraft tan, white, cream, pale grey, bright orange. A black shoe or a dark grey van on navy is invisible, and that is what went wrong last time. The reference hero works because its cartons are tan and its buildings are white.

**2. Keep everything inside the middle band.** The image is cropped from 16:9 down to 2070×760, which **removes the top 17% and the bottom 17%**. Anything up there is lost. So every prompt below ends with a composition line putting all content in the central band, and it is not optional.

Shared base, repeated in each prompt so they can be pasted independently:

| | |
|---|---|
| Ground | Deep navy `#0d2144` to near-black `#001830`, faint darker grid |
| Objects | **Light coloured**, matte 3D, brightly lit, clear separation from the ground |
| Accent | Saturated orange `#DD7008` |
| Semantics | Green `#16a34a` correct, red `#d02222` wrong |
| Composition | All content in the central horizontal band, top and bottom 20% empty |
| Count | **Five objects maximum.** Ten is a mess |

---

## 1. `tariff-engineering-legal-line-2026.webp`

**Alt:** "A product designer and a customs document side by side, showing how a physical product change alters its tariff classification at the border"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black. A vertical glowing cyan seam of light runs down the exact centre, dividing the frame in two.

LEFT: A clean WHITE trainer with a thick CREAM coloured textured sole, floating in three-quarter view, brightly lit. A glowing green ring floats behind it like a halo, vertical, not on the ground. A green tick sits beside the shoe at the same height.

RIGHT: A plain LIGHT GREY boxy cargo van, floating in three-quarter view, brightly lit. A single pale seat rises out of it on a short orange arrow. A glowing red ring floats behind it like a halo, vertical. A red cross sits beside the van at the same height.

COMPOSITION: Both objects centred vertically and the same size. All content sits within the middle horizontal band of the frame. The top 20% and bottom 20% are empty dark background.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no black or dark grey objects, no text, no watermark, no real brand logos, no recognisable vehicle or footwear models, no people, no ground shadows below the objects.
```

**What changed:** the shoe is white and the van light grey, so they read against the navy. The rings are vertical haloes behind the objects instead of ellipses on the floor, so the crop cannot cut them off.

---

## 2. `hts-classification-mistakes-importers-2026.webp`

**Alt:** "A warehouse operator recording fibre content, materials and weights at intake, the product attributes that determine HTS classification and duty"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black.

CENTRE: A single kraft-brown cardboard carton, brightly lit, with a small pale tag hanging from its side. It sits on a glowing orange disc. A cyan ring of light surrounds it.

RIGHT: Two thick arrows leave the carton horizontally. The upper arrow is green and ends at a SHORT stack of three gold coins. The lower arrow is red and ends at a TALL stack of ten gold coins.

COMPOSITION: Only three elements: the carton on the left of centre, and the two coin stacks on the right. All arranged along one horizontal line across the middle of the frame. The top 20% and bottom 20% are empty dark background.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no orbiting objects, no ring of products around the carton, no garment, no shoe, no gift box, no cog, no battery, no black or dark grey objects, no text, no numerals, no watermark, no real brand logos, no people.
```

**What changed:** the five orbiting products are gone. They were spread top to bottom, which is exactly what the crop destroys, and they made the image busy without adding meaning. One carton, two arrows, two stacks, all on one line. The article carries the five categories in the infographic instead.

---

## 3. `cbp-binding-ruling-guide-2026.webp`

**Alt:** "An importer preparing a binding ruling request with product samples, specifications and photographs laid out ready for submission to CBP"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black. Three elements arranged left to right along a single horizontal line, joined by a thick orange arrow.

LEFT: A pale grey document sheet floating upright, dimly lit, with a glowing orange question mark hovering just above it.

CENTRE: A glowing cyan circular ring seen edge on, which the orange arrow passes through.

RIGHT: A bright WHITE document sheet floating upright, crisply lit, the brightest object in the image, carrying a raised circular orange disc in its lower corner. A green tick floats beside it.

COMPOSITION: All three elements at the same height, centred vertically, spread evenly across the width. The top 20% and bottom 20% are empty dark background. Clear dark-to-bright progression from left to right.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no black or dark grey objects, no readable text or writing on the documents, no government seals or crests, no agency badges, no eagle or shield emblems, no watermark, no real brand logos, no people.
```

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
