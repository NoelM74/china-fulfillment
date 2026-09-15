# Image Briefs — Tier 8 / September and October posts

**Six images: 3 heroes + 3 infographics.**

> **Read `IMAGE-STYLE-GUIDE.md` first.** It overrides anything here. The rules that matter most, both learned by getting them wrong in Tier 7:
>
> **Objects must be light against the dark ground.** A navy background only works when what sits on it is bright. State the colour explicitly, every time.
>
> **Compose inside the middle band.** Heroes crop from 16:9 to 2070×760, which removes the top 17% and the bottom 17%. Every prompt below carries a composition line. It is not optional.

## Conventions

| | |
|---|---|
| **Heroes** | generate **16:9 at 2K**, crop to **2070×760**. Focal object dead centre |
| **Infographics** | generate **2:3 or 3:4 portrait at 2K**, resize to **1200×1500**. Highest quality setting |
| **Format** | `.webp`, sRGB |
| **Upload to** | `images/blog/`, exact lowercase filenames |

**All 3 posts are staged `noindex`, out of `sitemap.xml`, with no blog card.** These images complete them.

> **Timing note on post 1.** That post is about a deadline of **18 September 2026**. Its value decays quickly once the date passes. If only one image gets made this week, make that hero.

---

# HEROES

Shared base, repeated in each prompt so they can be pasted independently:

| | |
|---|---|
| Ground | Deep navy `#0d2144` fading to near-black `#001830`, faint darker grid |
| Objects | **Light coloured**, matte 3D, brightly lit |
| Accent | Saturated orange `#DD7008` |
| Semantics | Green `#16a34a` valid, red `#d02222` rejected |
| Composition | Middle band only, top and bottom 20% empty |
| Count | **Five objects maximum** |

---

## 1. `cbp-form-5106-importer-number-voided-2026.webp`

**Alt:** "An importer checking the physical address and contact details recorded on a customs identity form against the details CBP holds on file"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black, with a faint darker grid.

CENTRE: A bright WHITE document sheet floating upright, crisply lit, the brightest object in the frame. A large orange magnifying glass hovers over its upper half.

LEFT: A pale grey office building icon connected to the document by a short green line, with a small green tick beside it.

RIGHT: A pale grey shipping container icon connected to the document by a short red line that is visibly broken in the middle, with a small red cross beside it.

COMPOSITION: All three elements at the same height, centred vertically, spread evenly across the width. The top 20% and bottom 20% are empty dark background.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no black or dark grey objects, no readable text or writing on the document, no government seals or crests, no agency badges, no eagle or shield emblems, no flags, no watermark, no real brand logos, no people.
```

**The idea:** a correct address keeps the chain intact, a wrong one breaks it. No text needed to read that.

---

## 2. `epr-ppwr-eu-packaging-compliance-2026.webp`

**Alt:** "Packaging materials weighed and recorded by type for extended producer responsibility reporting across separate EU country registries"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black, with a faint darker grid.

CENTRE: A bright kraft-brown cardboard box, open and empty, sitting on a glowing orange weighing scale platform. A cyan ring of light surrounds it.

AROUND IT: Three light coloured packaging materials float in an arc above the box, evenly spaced and clearly separated: a pale flattened cardboard sheet, a translucent white poly bag, and a roll of cream packing tape.

COMPOSITION: The box and scale dead centre, the three materials arranged in a shallow arc across the middle of the frame rather than stacked vertically. The top 20% and bottom 20% are empty dark background.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no black or dark grey objects, no text, no numerals, no recycling symbols, no EU flag, no stars, no country flags, no watermark, no real brand logos, no people.
```

**Note:** no recycling symbols. They are close to real certification marks and we do not want to imply a certification.

---

## 3. `subscription-box-fulfillment-from-china-2026.webp`

**Alt:** "A monthly subscription box being assembled to a fixed pack-out specification, with rotating contents laid out ready for a single batch dispatch"

**Prompt:**

```
SCENE: A 3D conceptual illustration on a deep navy background (#0d2144) fading to near-black, with a faint darker grid.

CENTRE: A bright CREAM coloured open subscription box, seen from a three-quarter angle, sitting on a glowing orange disc. A cyan ring of light surrounds it.

ABOVE THE BOX: Four small light coloured objects float in a shallow horizontal arc, spaced apart, as if descending into the box: a pale cylinder, a small white jar, a folded cream cloth, and a flat card.

RIGHT: Three identical closed cream boxes in a neat receding row, smaller and slightly dimmer, suggesting a batch about to ship.

COMPOSITION: Everything sits in the middle horizontal band. The arc above the box is shallow and wide, not tall. The top 20% and bottom 20% are empty dark background.

STYLE: 3D product visualisation, matte materials, bright studio lighting, saturated, high contrast against the dark ground.

EXCLUDE: no black or dark grey objects, no text, no numerals, no watermark, no real brand logos, no recognisable products, no people.
```

---

# INFOGRAPHICS

Set every quoted string **exactly**. Check every word before uploading. Keep to six strings and roughly 25 words of text per canvas.

## 4. `infographic-form-5106-checklist.webp`

**Alt:** "What CBP Form 5106 must show from 18 September 2026: importer name, tax identifier, mailing address, a physical address that is not a broker, forwarder, registered agent, PO box or business service centre, plus a telephone number and email address belonging to the importer"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, split into two stacked halves separated by a thin horizontal rule.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "YOUR PHYSICAL ADDRESS".

TOP HALF: A green rounded card with a white tick icon and bold dark navy text reading exactly "YOUR PLACE OF BUSINESS".

BOTTOM HALF: A dark red rounded card with a white cross icon, and beneath it four short grey lines reading exactly "Customs broker", "Freight forwarder", "PO box", "Registered agent".

FOOTER: An orange band across the bottom with white bold text reading exactly "WRONG ADDRESS. VOIDED NUMBER."

TYPE: Modern geometric sans-serif. Large type, high contrast, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no government seals or crests, no brand logos, no extra text beyond the strings specified.
```

## 5. `infographic-epr-country-registries.webp`

**Alt:** "EPR registration is country by country across the EU: LUCID in Germany, Citeo in France, CONAI in Italy and Ecoembes in Spain, with non-EU sellers needing an authorised representative in each country"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, a single column of four evenly spaced rounded white cards with thin light grey borders.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "ONE COUNTRY, ONE REGISTRY".

CARDS: Each card carries a bold dark navy country name on the left and a grey registry name on the right. The four read exactly, top to bottom: "GERMANY / LUCID", "FRANCE / CITEO", "ITALY / CONAI", "SPAIN / ECOEMBES".

FOOTER: An orange band across the bottom with white bold text reading exactly "NO EU ENTITY? YOU NEED A REPRESENTATIVE."

TYPE: Modern geometric sans-serif. Large type, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no country flags, no EU flag, no stars, no maps, no brand logos, no extra text beyond the strings specified.
```

**Note:** no flags and no map. Registry names are the content, and a map invites the wrong idea that one registration covers the bloc.

## 6. `infographic-subscription-box-cycle.webp`

**Alt:** "Why subscription boxes break normal fulfilment: the whole cohort ships in one batch, the contents rotate every cycle, and stock is committed weeks ahead against a subscriber count that keeps moving"

**Prompt:**

```
LAYOUT: A flat vector infographic, portrait, pure white background, a single column of three evenly spaced rounded white cards with thin light grey borders.

HEADER: A deep navy bar across the top with white bold sans-serif text reading exactly "WHY BOXES ARE DIFFERENT".

CARDS: Each card has a simple two-colour line icon on the left in orange and navy, and bold dark navy text beside it. The three read exactly, top to bottom: "EVERYTHING SHIPS AT ONCE", "CONTENTS CHANGE MONTHLY", "YOU BUY BEFORE YOU KNOW".

ICONS: In order, several identical boxes in a row, a box with a circular rotation arrow around it, and a calendar with a question mark.

FOOTER: An orange band across the bottom with white bold text reading exactly "ASSEMBLE AT SOURCE".

TYPE: Modern geometric sans-serif. Large type, generous whitespace.

EXCLUDE: no gradients, no drop shadows, no 3D, no photographs, no brand logos, no extra text beyond the strings specified.
```

---

## If a generation comes out wrong

Change **one** thing and regenerate.

1. **Objects dark or muddy?** Put the colour word in capitals at the start of the object description. WHITE, CREAM, KRAFT-BROWN.
2. **Content lost in the crop?** Flatten the arrangement. Arcs should be wide and shallow, never tall.
3. **Garbled text?** Cut a string and raise the quality setting.
4. **Too busy?** Delete one object. Five is the ceiling and four is usually better.
