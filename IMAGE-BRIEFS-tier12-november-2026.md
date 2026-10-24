# Image record: Tier 12 / November 2026 posts

**Images for the four November posts for D2C ecommerce and crowdfunding sellers. No AI-generated images in this batch.**

> **Status: complete.** Installed 24 October 2026. Heroes are free stock photographs from Pexels; infographics are rendered from HTML using real data, with no image generator involved. All live on the dev site.

> **Read `IMAGE-STYLE-GUIDE.md` first.** Where this file and the guide disagree, the guide wins.

## Rules applied

**Order of preference** (Noel, 24 October 2026): "Use real photos from file or from free image services like pexels and other before using ai generated content."

1. **Our own photos.** Checked `images/site/` first. The genuine company photographs are the office team, the warehouse team, Noel with the PFC van, the PFC delivery van and the blue PFC truck. None shows D2C packing, gift parcels, a customer doorstep or a creator's desk, and all are already used on service pages.
2. **Free stock.** Pexels, licence checked for each photo. Unsplash and Pixabay were not reachable from the build environment; Wikimedia Commons photos are mostly CC BY-SA, which needs attribution and share-alike.
3. **AI.** Not needed.

**Logos** (Noel, 24 October 2026): carrier, shipping-line and courier logos (Maersk, COSCO, Hapag-Lloyd, Yang Ming, DHL, UPS, FedEx and the like) are fine; they are partners. **Never show another 3PL or fulfilment company.** A porch photo with an Amazon box was rejected for that reason, since Amazon also sells fulfilment. See `IMAGE-STYLE-GUIDE.md` §4.

**People.** All three new heroes show the **customer's side** of the task (a gift, a doorstep, a creator's desk), which §2 of the style guide allows. None shows our warehouse, so the orange-polo rules do not apply.

## Heroes (2070×760, plus -760w, -1140w and -1520w copies)

| File in `images/blog/` | Post | Source | Photographer | Size |
|---|---|---|---|---|
| `christmas-2026-shipping-deadlines-from-china.webp` | Christmas 2026 deadlines | [Pexels 1661965](https://www.pexels.com/photo/three-gift-boxes-1661965/), "Three Gift Boxes" | Suzy Hazelwood | 63 KB |
| `shipping-d2c-orders-china-to-us-2027.webp` | US D2C, is de minimis back | [Pexels 13443801](https://www.pexels.com/photo/smiling-woman-receiving-package-from-courier-13443801/), "Smiling Woman Receiving Package from Courier" | Mizuno K | 80 KB |
| `kickstarter-indiegogo-shipping-duties-2027.webp` | Kickstarter and Indiegogo shipping | [Pexels 7857532](https://www.pexels.com/photo/woman-sitting-at-the-table-and-packing-orders-7857532/), "Woman Sitting at the Table and Packing Orders" | Kampus Production | 57 KB |
| `ieepa-tariff-refunds-china-sellers-2026.webp` | IEEPA refunds | [Pexels 5900074](https://www.pexels.com/photo/woman-sitting-behind-the-desk-and-looking-at-receipts-5900074/), "Woman Sitting Behind the Desk and Looking at Receipts" | Karolina Grabowska (Kaboompics) | 69 KB |

**Licence.** All are under the [Pexels licence](https://www.pexels.com/license/): free for commercial use, attribution not required, modification allowed. Not allowed: selling unaltered copies, implying the people or brands shown endorse us, or showing identifiable people in a bad light. The doorstep photo shows a smiling customer, in a positive light.

**Processing.** Centre crop to 2070×760 (the middle band, per §6), light denoise, WebP at quality 78. Visitors are served the 760–1520 copies through `srcset`.

## Infographics (1200×1500, plus -600w and -900w copies)

Rendered from HTML in the site font (Outfit) and brand navy and orange, flat on white, per §6. Source: `scripts/infographics/2026-11/make_infographics.py`; `bash scripts/infographics/2026-11/build.sh` rebuilds every infographic in that folder into `images/blog/`. **Edit the script, not the images.**

| File | Figures and their sources |
|---|---|
| `infographic-christmas-2026-dispatch-dates.webp` | Our published delivery times by market (US 6–10, UK 5–8, EU 6–14, Canada 5–9, Australia 4–7 days; express 2–5 business days) plus a peak buffer; **dates need Noel's sign-off** (CMS checklist §16) |
| `infographic-us-d2c-parcel-duty-2027.webp` | 12.5% Section 301 forced labor duty from 24 July 2026; Section 301 lists 7.5–100%; IEEPA collection ended 24 Feb 2026 (CBP CSMS); de minimis suspended, repealed from 1 July 2027; Entry Type 13 from 20 Jan 2027 (CBP, 14 Oct 2026) |
| `infographic-crowdfunding-reward-shipping-2027.webp` | US no threshold; EU €3 per item category from 1 July 2026; UK £135 VAT at sale; Canada CAD$20; Australia A$1,000 GST at sale (as in our market guides) |
| `infographic-ieepa-refund-who-gets-paid.webp` | CBP pays CAPE refunds by ACH to the importer of record; Section 122 and 301 not covered |

**When a figure changes**, update `make_infographics.py` and the matching article together, then run the build.

## Parked posts

The three bulk-freight posts first written for this round (sea freight to Amazon FBA, LCL vs FCL, China to Europe) were parked on 24 October 2026; see `data/content/parked/README.md`. Their heroes (Pexels 1554646 by Tom Fisk, 28438334 by Simon R. Minshall, 14776383 by Quang Nguyen Vinh) and infographics remain in `images/blog/` so the posts can be restored without redoing images.

## Shot list: real photos to replace stock

Real photographs of our own operation beat stock every time (§6). Where a hero could show our work instead of the customer's side, here is what to shoot at the Shenzhen warehouse. Save over the same filename at 2070×760 with the subject in the middle band, update the alt text in the draft frontmatter, and rebuild.

1. **Christmas deadlines.** Two staff in orange polos packing gift-wrapped D2C orders into mailers at a packing bench, a stack of finished parcels beside them. Suggested alt: *"Warehouse staff in orange polo shirts packing gift orders into mailers at the Shenzhen warehouse ahead of the Christmas cut-offs"*.
2. **Kickstarter and Indiegogo shipping.** Staff assembling reward kits on a bench: product, add-ons and inserts going into branded boxes, with a packing list. Suggested alt: *"Staff in orange polo shirts assembling crowdfunding reward kits with add-ons and inserts at the Shenzhen warehouse"*.
3. **US D2C and IEEPA refunds.** Keep the stock photos. Both show the customer's side, which our staff should not appear in.

Same people rules as always: Chinese staff aged 22 to 27, both men and women, orange polos with the small chest logo, no hard hats or hi-vis.
