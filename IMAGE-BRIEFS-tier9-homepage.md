# Image Briefs — Tier 9 / Homepage replacements

**Four images. All replace existing homepage files in place.**

> **Status: delivered and live.** All four were generated, cropped to 1200×670 and installed on 18 September 2026. Each carries `srcset` at 400w, 720w and 1200w. The prompts below are kept as the record of what was asked for, and as the pattern for the three homepage images still on the old style.

> **Read `IMAGE-STYLE-GUIDE.md` first. It overrides anything here.**
>
> These four break the guide as it stands today: staff appear in **blue hi-vis vests and blue polos**, where §2 specifies **orange polos** and explicitly forbids hi-vis. They predate the guide. The recent blog heroes follow it, which is why they look better.

## Why these four

| Current file | Problem |
|---|---|
| `shenzhen-warehouse-interior-panoramic-ecommerce-fulfillment` | Blue uniforms. Wide establishing shot, no human focus |
| `crowdfunding-fulfillment-kickstarter-indiegogo-rewards-packing-china` | Blue hi-vis vests, plus AI-rendered Kickstarter and Indiegogo wordmarks |
| `drip-feed-small-shipment-amazon-fba-weekly-china` | Blue uniform, sparse and weak subject |
| `multi-supplier-receiving-dock-shenzhen-warehouse` | Blue hi-vis vests |

Three homepage images are staying: the Mandarin-speaking team office shot (office staff, §2's warehouse rule does not apply), the Yantian port aerial (no people, genuinely good), and the QC inspection shot until there is time to redo it.

## Conventions — these differ from the blog tiers

| | |
|---|---|
| **Generate** | 16:9 at 2K |
| **Deliver** | **exactly 1200×670**, `.webp`, sRGB |
| **Upload to** | `images/site/`, **reusing the exact existing filenames above** |
| **Filenames** | Do not rename. The markup, `sitemap.xml`, the schema and the `og:image` tag all point at these paths already |

**Composition matters more than usual here.** Images 2, 3 and 4 sit in service cards styled `object-fit:cover` in a 180px-tall box, so roughly the top and bottom 12% is cut. Keep the subject in the middle horizontal band.

> **Image 1 is the social share card.** It is `og:image`, `twitter:image` and the Organization `image` in structured data. On the page itself it sits behind a 86–93% opaque navy overlay in `.hero::before`, so barely 10% of it shows through and its on-page impact is small. It is what people see when your link is posted on LinkedIn, so it has to read clearly as a real working warehouse **at thumbnail size**. Compose it wider and simpler than you would for a page image.

## Shared setting

| | |
|---|---|
| People | Chinese, **aged 22 to 27**, mixed gender, **orange polo shirts** with a small chest logo |
| Below the waist | Ordinary personal clothing: jeans, chinos, trainers |
| Manner | Working and focused. Unposed. No stock-photo grinning at camera |
| Floor | **Green epoxy resin**, satin sheen, yellow demarcation lines |
| Racking | **Blue** steel |
| Walls | White or pale grey painted block |
| Ceiling | White, exposed, fluorescent strip lights |
| Cartons | Yellow-brown kraft, yellow plastic totes |

**Never:** hard hats, hi-vis vests, safety goggles, Western warehouse workers, all-male crews, US-style green and orange racking, cavernous vanishing-point aisles.

**On branding.** The small chest logo on the polo is the only place the brand should appear. Do not ask for large rendered signage or wordmarks: generated lettering comes out subtly wrong and that is exactly what makes an image read as fake. The real "PFC China Fulfillment" signage in the current photos is authentic, but a regenerated version of it will not be.

> **Check first whether a real photograph covers the scene.** A genuine photo of the actual team beats a generated one every time and no competitor can copy it. Generation is the fallback.

---

## 1. `shenzhen-warehouse-interior-panoramic-ecommerce-fulfillment.webp`

**Alt (already live in the markup):** "Racked inventory and packing benches inside the Shenzhen fulfilment warehouse, where D2C and crowdfunding orders are picked, packed and dispatched the same or next business day"

```
SCENE: The main floor of an eCommerce fulfilment warehouse in Shenzhen. Green epoxy resin floor with yellow demarcation lines. Blue steel racking on the left holding yellow-brown kraft cartons. A row of stainless steel packing benches along the right. White painted walls, white exposed ceiling with fluorescent strip lights.

SUBJECT: Two Chinese warehouse staff in their mid twenties, one man and one woman, both wearing orange company polo shirts with a small logo on the left breast. The woman stands at the nearest packing bench sealing a kraft carton with tape. The man walks past her pushing a trolley stacked with yellow plastic totes, mid stride, looking ahead at his work.

DETAILS: On the bench, a small stack of flat-packed cartons, a tape gun, and a label printer. Further down the aisle a third member of staff in the same orange polo is small in the frame, scanning a carton.

LIGHT: Bright even fluorescent light from above, with cool daylight entering from high windows on the left.

STYLE: Documentary workplace photography, 35mm, eye level, taken from about four metres back. Natural and unposed. Shallow depth of field on the background racking.

COMPOSITION: Both main figures in the middle horizontal band, the woman slightly left of centre. Wide horizontal composition that still reads clearly when shrunk to a small thumbnail.

EXCLUDE: no readable text or signage, no large logos or wordmarks, no hard hats, no hi-vis vests, no safety goggles, no Western workers, no third-party brand logos, no forklifts, no stock-photo smiling at camera.
```

**Why this scene:** this is the image people see when your link is shared. Two people plainly doing the work, at a size that survives a LinkedIn thumbnail.

---

## 2. `crowdfunding-fulfillment-kickstarter-indiegogo-rewards-packing-china.webp`

**Alt (already live):** "Kickstarter and Indiegogo backer rewards packed in batches against a campaign pledge manifest before worldwide dispatch from Shenzhen"

```
SCENE: A long packing bench set up for batch work in a Shenzhen fulfilment warehouse. Green epoxy resin floor, blue steel racking behind, white painted walls, fluorescent strip lighting.

SUBJECT: Three Chinese staff in their mid twenties, two women and one man, all in orange company polo shirts with a small chest logo, working along one side of the bench in a line. The nearest woman is placing a small product into an open kraft box. The others are assembling boxes further down, slightly out of focus.

DETAILS: Along the bench, identical open kraft boxes in a neat row, each with the same three items laid beside it ready to go in. A clipboard holding a printed tick-list rests on the bench in the foreground. Yellow plastic totes of components under the bench.

LIGHT: Even cool overhead light with one warm task lamp over the nearest work position.

STYLE: Documentary workplace photography, 35mm, slightly above eye level looking down the length of the bench, taken from about two and a half metres back. Natural and unposed.

COMPOSITION: The nearest woman and her open box in the middle horizontal band, centred vertically. The bench recedes to the right. Wide horizontal composition.

EXCLUDE: no readable text, no crowdfunding platform names or logos, no Kickstarter or Indiegogo branding, no banners or signage, no hard hats, no hi-vis vests, no Western workers, no third-party brand logos, no stock-photo smiling at camera.
```

**Why this changed:** the current image has Kickstarter and Indiegogo wordmarks rendered onto a warehouse banner. Rendering another company's trademark on your own wall implies a partnership you do not have, and generated lettering is always subtly wrong. The identical row of boxes carries the same meaning without naming anyone.

---

## 3. `drip-feed-small-shipment-amazon-fba-weekly-china.webp`

**Alt (already live):** "Weekly drip-feed consignments staged for Amazon FBA, sending small regular shipments from Shenzhen rather than one large inbound"

```
SCENE: A marked staging area on the floor of a Shenzhen fulfilment warehouse, with yellow demarcation lines painted on green epoxy resin. Blue steel racking behind, white painted walls, fluorescent strip lighting.

SUBJECT: A Chinese man in his mid twenties in an orange company polo shirt with a small chest logo crouches beside a half-height stack of kraft cartons on a pallet, applying a plain white barcode label to the top carton. He is concentrating on the label, not looking at the camera.

DETAILS: Three separate small pallet stacks stand in a row in the staging area, each only four or five cartons high, each already carrying plain white barcode labels. A handheld scanner rests on the nearest carton. A Chinese woman of similar age in the same orange polo checks a tablet in the background, out of focus.

LIGHT: Even cool overhead fluorescent light.

STYLE: Documentary workplace photography, 35mm, low eye level close to the pallet, taken from about two metres back. Natural and unposed.

COMPOSITION: The man and the carton he is labelling in the middle horizontal band, centred vertically. The other two pallet stacks recede to the right. Wide horizontal composition.

EXCLUDE: no readable text on labels, no Amazon logo or smile mark, no FBA branding, no courier livery, no vans or vehicles, no hard hats, no hi-vis vests, no Western workers, no third-party brand logos, no stock-photo smiling at camera.
```

**Why this scene:** several small stacks rather than one big one is the whole point of drip feeding. The current image shows a van, which says delivery, not staged weekly consignments.

---

## 4. `multi-supplier-receiving-dock-shenzhen-warehouse.webp`

**Alt (already live):** "Cartons from several suppliers arriving at the Shenzhen receiving dock to be counted, quality checked and consolidated into one outbound shipment"

```
SCENE: The inbound receiving area of a Shenzhen fulfilment warehouse, just inside a roller shutter door standing open to daylight. Green epoxy resin floor with yellow demarcation lines, blue steel racking to one side, white painted walls.

SUBJECT: A Chinese woman in her mid twenties in an orange company polo shirt with a small chest logo stands at an inbound pallet counting cartons, one hand touching a carton and the other holding a tablet. A Chinese man of similar age in the same orange polo kneels beside a second pallet, cutting the tape on a carton to check the contents.

DETAILS: Four or five pallets of cartons stand in the receiving area, visibly from different sources: different carton sizes, different shades of kraft, different tape colours, some shrink wrapped and some not. Daylight falls through the open shutter behind them.

LIGHT: Bright natural daylight from the open dock door behind, filled by cool overhead fluorescent light inside.

STYLE: Documentary workplace photography, 35mm, eye level, taken from about three metres back. Natural and unposed. Slight backlight from the doorway.

COMPOSITION: Both people in the middle horizontal band, the woman left of centre and the man right. Wide horizontal composition.

EXCLUDE: no readable text or supplier names, no large logos, signage or wordmarks, no hard hats, no hi-vis vests, no Western workers, no forklifts, no third-party brand logos, no stock-photo smiling at camera.
```

**Why this scene:** cartons that obviously come from different factories is what makes consolidation legible at a glance. Matching cartons would read as a single supplier.

---

## After the images land

Tell me and I will:

1. Drop them in and confirm each one decodes, is the right size and is not clipped by the card crop.
2. Add `srcset` across the homepage. It is deliberately not done yet, because generating resized variants of images that are about to be replaced would be wasted work.
3. Re-run the width sweep at 360, 390, 414, 768, 1024, 1280 and 1440 to confirm nothing shifts.

The alt text for all four is already written and live, so nothing needs editing on that side when the files are swapped.
