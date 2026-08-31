# Image Style Guide

**Standing rules for every image generated for china-fulfillment.com.** Every future `IMAGE-BRIEFS-tierN.md` must comply with this file. Where a brief and this guide disagree, this guide wins.

Last updated 31 August 2026.

---

## 1. The problem this fixes

Earlier tiers produced technically clean images that could have belonged to any 3PL on earth: anonymous warehouses, faceless workers, US-style pallet racking. They were not wrong, they were **generic**. Nothing in them said this company.

Two things fix that, and both are non-negotiable from here.

1. **The people are real and specific.** Chinese staff in their twenties, in the company's own orange uniform.
2. **The warehouse is the actual Shenzhen facility**, not a stock American distribution centre.

---

## 2. People

**Who appears in every image containing warehouse staff:**

| | |
|---|---|
| **Nationality** | Chinese |
| **Age** | 22 to 27. Young adults, not middle-aged |
| **Gender mix** | Both men and women, mixed naturally within a frame. Do not default to all-male |
| **Uniform** | **Orange polo shirt**, short sleeved, with a small chest logo |
| **Lower half** | Ordinary personal clothing: jeans, chinos, skirts, trainers. Not matching workwear trousers |
| **Manner** | Working, focused, unposed. Occasionally a natural smile. Never corporate stock-photo grinning |

**This corrects an error in Tiers 1 to 6**, which specified a *navy* polo shirt. That was wrong. The uniform is orange. Any future brief saying navy polo is a copy-paste mistake and should be corrected before generating.

**Never generate:**

- Western or racially ambiguous warehouse workers
- Workers aged 35 and up in operational roles
- Hard hats, hi-vis vests, or safety goggles. This is a fulfilment warehouse, not a construction site or a heavy-industry plant
- An all-male crew
- Empty warehouses with no people in them at all, unless the brief specifically calls for an architectural shot

---

## 3. The warehouse

Match the real facility. The distinguishing features, in rough order of how much they change the look:

| Feature | Reality | Not this |
|---|---|---|
| **Floor** | Green epoxy resin, satin sheen, yellow painted demarcation lines | Bare polished concrete |
| **Racking** | **Blue** steel racking and shelving | Green uprights with orange beams, the US pallet-rack look |
| **Walls** | White or pale grey painted block, some with red Chinese banner signage | Bare metal cladding |
| **Ceiling** | White, exposed, fluorescent strip lights | High steel truss with sodium lighting |
| **Air** | Wall-mounted and ceiling fans | Industrial HVAC ducting |
| **Cartons** | Yellow-brown kraft cartons, yellow plastic totes and crates | Grey plastic totes on roller conveyor |
| **Windows** | Small, with security grilles | Floor-to-ceiling glazing or clerestory bands |
| **Scale** | A working unit you can see across, human-sized | Cavernous, vanishing-point aisles |

**The single clearest tell of a wrong image** is a long roller conveyor running down a wide aisle between green-and-orange pallet racking with grey totes on it. That is a US distribution centre. It is not this warehouse, and it is exactly the generic look to avoid.

---

## 4. Logo usage

The logo may appear **subtly and in-world** where it would plausibly exist in reality. It must never look like a watermark.

**Where it works:**

- Small printed logo on the chest of the orange polo shirts, left breast, not oversized
- A modest printed label or stamp on kraft cartons
- Branded packing tape running along a carton seam
- A wall sign or board in the background, small in frame
- A screen or tablet interface visible at an angle

**Where it does not:**

- Floating over the image as an overlay or corner watermark
- Blown up as a graphic element
- On anything the company would not actually brand: a customer's product, a shipping label, a courier vehicle, a government document
- Stretched, recoloured, rotated, or given effects

**Rule of thumb:** if a photographer walking the floor would have caught it in frame, it belongs. If it had to be added afterwards, it does not.

**Do not put the logo on infographics.** They are clean flat-vector diagrams and the brand already reads through the palette.

---

## 5. Colour

Sampled directly from `images/site/new-cf-logo-no-bg.webp`.

| Use | Hex |
|---|---|
| Logo teal | `#2B677A` |
| Logo orange | `#DD7008` |
| Site dark ground | `#0d2144` (`--navy`) |
| Site deepest ink | `#0c1a2e` (`--ink`) |
| Accessible orange on light backgrounds | `#c25205` |
| Accessible orange on dark backgrounds | `#fa8738` |
| Off-white panel | `#f4f6fb` |

**Two cautions.**

The logo's teal `#2B677A` **does not appear anywhere in the site CSS.** It exists only in the logo. Do not build an infographic palette around it expecting it to match the site, and do not introduce it as a third brand colour without a decision to do so.

Tiers 1 to 6 quoted "brand navy `#0F1E3D`, brand orange `#F26B21`". **Neither value is in the site CSS.** The real equivalents are `#0d2144` and `#c25205`. Use the table above.

For infographics, text contrast still has to clear WCAG AA. `#DD7008` on white is roughly 3.4:1, which fails for normal body text. Use `#c25205` for small text on light grounds and reserve the logo orange for large headings, fills and bands.

---

## 6. Photographic treatment

Unchanged from earlier tiers and still correct:

- Photographic realism, documentary logistics, natural light
- 35mm or 50mm lens feel, eye level, shot from two to three metres back
- Deep shadows, warm neutral greys, one restrained orange accent
- Composition must stay readable when cropped to a narrow mobile strip
- **No on-image text in heroes**

## 7. Sizes and format

| | |
|---|---|
| Format | `.webp`, sRGB |
| Hero | **generate 16:9 at 2K, then crop to 2400×880.** Displayed 1200×440. Target under ~150 KB. Keep the subject centred so the crop is safe |
| Infographic | **generate 2:3 or 3:4 portrait at 2K, then resize to 1200×1500.** Single column, phone-legible. Use the highest quality setting |
| Location | `images/blog/` for post images, `images/site/` for page and service images |
| Filenames | lowercase, hyphenated, exact. Pages reference them literally |

---

## 8. Global negative prompt

Append to every generation:

> *no readable third-party brand logos, no courier or marketplace trademarks, no government seals or agency crests, no national flags rendered as logos, no watermarks, no stock-photo lens flare, no distorted hands, no gibberish text, no hard hats or hi-vis vests, no Western warehouse workers, no US-style green and orange pallet racking, no signage other than the text specified.*

---

## 9. How to write the prompt

Learned the hard way in Tier 7, whose first set generated poorly. These follow OpenAI's own guidance for their image models.

**Use labeled segments, not a paragraph.** One dense block is the single biggest cause of a bad render. Structure every photographic prompt as:

```
SCENE:    where we are, and the light
SUBJECT:  who or what the image is actually about
DETAILS:  at most three supporting elements
LIGHT:    only if SCENE has not covered it
STYLE:    lens, angle, treatment, composition
EXCLUDE:  the constraint line
```

For infographics, swap the first three for `LAYOUT:`, `HEADER:`, `CARDS:` or `STEPS:`, `FOOTER:`, `TYPE:`.

**Order is scene, then subject, then details, then constraints.** Lead with camera jargon and the subject arrives too late to anchor the image.

**Cap it at eight requirements.** Listing twenty causes the model to silently drop several, and you cannot tell which. Aim for 120 to 180 words.

**Negative constraints do work here.** OpenAI recommends stating exclusions explicitly, so keep the `EXCLUDE:` line. This is the opposite of the advice for some other models, and it is worth remembering which one you are prompting.

**In-image text.** Put every string in quotes or ALL CAPS and say "reading exactly". Keep it to **six or so strings and about 25 words of text in total** per canvas. Count words, not just strings: five one-word labels are far safer than three full sentences. Character accuracy degrades with total text volume. If a specific word comes out mangled, spell it letter by letter in the prompt. Use the highest quality setting for anything with small text.

**Generate at a common aspect ratio and crop.** GPT Image 2's exact supported size table could not be verified from a source worth trusting, and exotic ratios like 27:10 were probably never native. Generate 16:9 for heroes and 2:3 or 3:4 for infographics, then crop or resize to target. Keep subjects centred so the crop is safe.

**Iterate one change at a time.** Generate, look, change one thing. Changing four things at once tells you nothing about which one worked.

---

## 10. Pre-upload checklist

Before any generated image goes into `images/`:

- [ ] Are the people Chinese, in their twenties, in **orange** polos?
- [ ] Is there a natural gender mix?
- [ ] Green floor, blue racking, white walls? Not a US distribution centre?
- [ ] If the logo appears, is it in-world and small, rather than an overlay?
- [ ] Any in-image text rendered correctly, digit for digit?
- [ ] Does the render actually match the alt text already written into the HTML?
- [ ] Filename lowercase and exact?

The alt text point matters most. Alt text ships in the HTML before the image exists, so a render that does not match it makes the page inaccurate for screen reader users and for search engines.
