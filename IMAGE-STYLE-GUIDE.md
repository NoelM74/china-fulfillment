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
| Hero | displayed 1200×440; generate at **2400×880**, target under ~150 KB |
| Infographic | **1200×1500**, 4:5 portrait, single column, phone-legible |
| Location | `images/blog/` for post images, `images/site/` for page and service images |
| Filenames | lowercase, hyphenated, exact. Pages reference them literally |

---

## 8. Global negative prompt

Append to every generation:

> *no readable third-party brand logos, no courier or marketplace trademarks, no government seals or agency crests, no national flags rendered as logos, no watermarks, no stock-photo lens flare, no distorted hands, no gibberish text, no hard hats or hi-vis vests, no Western warehouse workers, no US-style green and orange pallet racking, no signage other than the text specified.*

---

## 9. Pre-upload checklist

Before any generated image goes into `images/`:

- [ ] Are the people Chinese, in their twenties, in **orange** polos?
- [ ] Is there a natural gender mix?
- [ ] Green floor, blue racking, white walls? Not a US distribution centre?
- [ ] If the logo appears, is it in-world and small, rather than an overlay?
- [ ] Any in-image text rendered correctly, digit for digit?
- [ ] Does the render actually match the alt text already written into the HTML?
- [ ] Filename lowercase and exact?

The alt text point matters most. Alt text ships in the HTML before the image exists, so a render that does not match it makes the page inaccurate for screen reader users and for search engines.
