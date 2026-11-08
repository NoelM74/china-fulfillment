# Image record: Tier 13 / posts of 8 November 2026

**Images for the US market page, the China to USA shipping post, three dropshipping posts and three comparison posts. No AI-generated images in this batch.**

> **Status: complete.** Installed 8 November 2026. Heroes are free stock photographs from Pexels; infographics are rendered from HTML, with no image generator involved. All live on the dev site.

> **Read `IMAGE-STYLE-GUIDE.md` first.** Where this file and the guide disagree, the guide wins.

## Rules applied

**Order of preference** (Noel, 24 October 2026): "Use real photos from file or from free image services like pexels and other before using ai generated content." Our own photos in `images/site/` were checked first; none show a US doorstep, a seller's home office, branded unboxing or air cargo, and they are already used on service pages.

**Logos** (Noel, 24 October 2026): carrier and airline logos are fine; never another 3PL or fulfilment company. The air cargo hero shows an airline's tail colours, which is allowed. No photo shows a 3PL's branding. See `IMAGE-STYLE-GUIDE.md` §4.

**People.** The heroes with people show the customer's or seller's side (a doorstep, a home office, a small studio), which §2 of the style guide allows. None shows our warehouse, so the orange-polo rules do not apply.

## Heroes (2070×760, plus -760w, -1140w and -1520w copies)

| File in `images/blog/` | Post | Source | Photographer |
|---|---|---|---|
| `china-to-us-fulfillment-2027.webp` | China to US fulfillment | [Pexels 6682773](https://www.pexels.com/photo/a-delivery-man-carrying-a-box-6682773/), "A Delivery Man Carrying a Box" | Kampus Production |
| `shipping-from-china-to-usa-d2c-2027.webp` | Shipping from China to the USA | [Pexels 6169669](https://www.pexels.com/photo/close-up-photo-of-stacked-carton-boxes-6169669/), "Close-up Photo of Stacked Carton Boxes" | Tima Miroshnichenko |
| `switch-from-dropshipping-to-china-3pl.webp` | When to switch from dropshipping | [Pexels 7289719](https://www.pexels.com/photo/woman-using-brown-box-for-packaging-7289719/), "Woman Using Brown Box for Packaging" | Kampus Production |
| `aliexpress-cj-dropshipping-vs-own-stock-china-warehouse.webp` | AliExpress or CJ vs own stock | [Pexels 4483610](https://www.pexels.com/photo/warehouse-with-concrete-floors-4483610/), "Warehouse with Concrete Floors" | Tiger Lily |
| `dropshipping-to-branded-d2c-store.webp` | Dropshipping to a branded store | [Pexels 7857523](https://www.pexels.com/photo/close-up-of-person-packing-an-order-into-a-cardboard-box-7857523/), "Close-up of Person Packing an Order into a Cardboard Box" | Kampus Production |
| `best-shopify-fulfillment-brands-sourcing-from-china-2027.webp` | Best Shopify fulfillment | [Pexels 7857553](https://www.pexels.com/photo/woman-standing-next-to-a-desk-with-a-laptop-and-cardboard-boxes-and-writing-on-paper-7857553/), "Woman Standing next to a Desk with a Laptop and Cardboard Boxes and Writing on Paper" | Kampus Production |
| `shipbob-alternatives-international-brands-2027.webp` | ShipBob alternatives | [Pexels 9749472](https://www.pexels.com/photo/boxes-being-loaded-onto-an-airplane-9749472/), "Boxes Being Loaded onto an Airplane" | Ethan Nguyen |
| `best-crowdfunding-fulfillment-companies-2027.webp` | Best crowdfunding fulfillment | [Pexels 12354555](https://www.pexels.com/photo/photograph-of-brown-cardboard-boxes-12354555/), "Photograph of Brown Cardboard Boxes" | Ayrat |

**Licence.** All are under the [Pexels licence](https://www.pexels.com/license/): free for commercial use, attribution not required, modification allowed. Not allowed: selling unaltered copies, implying the people or brands shown endorse us, or showing identifiable people in a bad light. Each page was checked on 8 November 2026.

**Processing.** Cropped to 2070×760 (centre, except the Shopify hero, shifted up to keep the face, and the crowdfunding hero, shifted down to keep the whole stack), light denoise, WebP at quality 78.

## Infographics (1200×1500, plus -600w and -900w copies)

Rendered from HTML in the site font (Outfit), navy and orange on white, per §6. Source: `scripts/infographics/2026-11/make_infographics.py` (items 8 and 9); `bash scripts/infographics/2026-11/build.sh` rebuilds them. **Edit the script, not the images.**

| File | Figures and their sources |
|---|---|
| `infographic-china-to-us-fulfillment-2027.webp` | Our $0.99 pick and pack and 6–10 day US delivery time (published); MFN + Section 301 list duty + 12.5% forced labor duty; de minimis repealed from 1 July 2027 (as in `shipping-d2c-orders-china-to-us-2027`) |
| `infographic-shipping-china-to-usa-2027.webp` | Express 3–5 business days, postal ~10–20 days, bulk air 5–10 days, sea 14–16 days to the West Coast (our shipping guide, early 2026); standard DDP 6–10 days (published); Entry Type 13 from 20 January 2027 (CBP) |

**When a figure changes**, update `make_infographics.py` and the matching article together, then run the build.

## Shot list: real photos to replace stock

1. **China to US fulfillment.** Staff in orange polos sealing a DDP parcel at a packing bench with a US address label visible but unreadable. Suggested alt: *"Warehouse staff in orange polo shirts sealing a DDP parcel for a US customer at the Shenzhen warehouse"*.
2. **Dropshipping posts.** Racking with one brand's stock, cartons labelled with SKU codes only, and a member of staff checking a delivery against a packing list.
3. **Branded store.** A branded mailer being packed with tissue and an insert card at our bench.

Same people rules as always: Chinese staff aged 22 to 27, both men and women, orange polos with the small chest logo, no hard hats or hi-vis.
