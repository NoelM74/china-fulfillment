# CMS update checklist: October 2026

What the live site (china-fulfillment.com) is still missing from this repo. I checked it against production on 3 October 2026.

Everything below is on the `main` branch. Copy from the built `.html` files in the repo root, **not** from `data/content/drafts/`.

**Dev site:** https://china-fulfillment.borufashions.workers.dev/ builds automatically from `main`, so every change below is already live there. Open a page on the dev site to see exactly how it should look on china-fulfillment.com. Image files can be downloaded straight from it too, for example https://china-fulfillment.borufashions.workers.dev/images/blog/infographic-who-is-the-importer.webp

---

## How to copy a page

1. Upload the page's images to a new CMS folder, for example `/Upload/202610/`.
2. In the copied HTML, find and replace the image paths with that folder:
   - `/images/blog/` → `/Upload/202610/`
   - `images/site/` → `/Upload/202610/`

   This also fixes the `srcset` lines, so phones load the small copies.
3. Keep everything in the `<head>`: title, meta description, canonical, Open Graph tags and every `<script type="application/ld+json">` block. These blocks are what Google and the AI search tools read.
4. Keep the logo at `https://www.china-fulfillment.com/image/logo.png`, as the live posts already do.
5. Each new image comes in several sizes, for example `name.webp`, `name-600w.webp` and `name-900w.webp`. If you only upload the main file, delete the `srcset="..."` and `sizes="..."` attributes from that `<img>` tag. Otherwise the browser asks for files that do not exist.

---

## 1. Five new blog posts (all return 404 on production)

| Page (repo file = live URL) | Preview | Images to upload from `images/blog/` |
|---|---|---|
| `eu-customs-reform-importer-distance-sales-2026.html` | [dev](https://china-fulfillment.borufashions.workers.dev/eu-customs-reform-importer-distance-sales-2026) | `eu-customs-reform-importer-distance-sales-2026.webp` + `-760w` `-1140w` `-1520w`, `infographic-eu-customs-reform-timeline.webp` + `-600w` `-900w` |
| `section-301-forced-labor-tariff-china-2026.html` | [dev](https://china-fulfillment.borufashions.workers.dev/section-301-forced-labor-tariff-china-2026) | `section-301-forced-labor-tariff-china-2026.webp` + `-760w` `-1140w` `-1520w`, `infographic-section-301-duty-stack.webp` + `-600w` `-900w` |
| `best-china-3pl-companies-2026.html` | [dev](https://china-fulfillment.borufashions.workers.dev/best-china-3pl-companies-2026) | `best-china-3pl-companies-2026.webp` + `-760w` `-1140w` `-1520w`, `infographic-china-3pl-types.webp` + `-600w` `-900w` |
| `importer-of-record-china-fulfillment-2026.html` | [dev](https://china-fulfillment.borufashions.workers.dev/importer-of-record-china-fulfillment-2026) | `importer-of-record-china-fulfillment-2026.webp` + `-760w` `-1140w` `-1520w`, `infographic-who-is-the-importer.webp` + `-600w` `-900w` |
| `china-3pl-vs-freight-forwarder-vs-sourcing-agent.html` | [dev](https://china-fulfillment.borufashions.workers.dev/china-3pl-vs-freight-forwarder-vs-sourcing-agent) | `china-3pl-vs-freight-forwarder-vs-sourcing-agent.webp` + `-760w` `-1140w` `-1520w`, `infographic-who-does-what-china.webp` + `-600w` `-900w` |

That is 25 image files in total. The `-760w`, `-1140w` and similar endings sit before `.webp`, for example `best-china-3pl-companies-2026-760w.webp`.

Then:
- [ ] Add the five blog cards to the live blog page. Copy them from `blog.html` (search for each post's file name).
- [ ] Add the five URLs to the live sitemap. The entries are in `sitemap.xml`, after the Q4 peak season entry.
- [ ] After publishing, request indexing for each URL in Google Search Console.

## 2. Q4 peak season post: refreshed rates

- [ ] `q4-peak-season-fulfillment-from-china-2026.html` ([dev](https://china-fulfillment.borufashions.workers.dev/q4-peak-season-fulfillment-from-china-2026)): replace the live article body with the repo version. It has the 1 October 2026 Drewry container rates (for example LA $7,835 per 40ft) and TAC air freight data. The live page still has the old figures.
- No new images. The live page already has the hero and infographic.

## 3. About Us: new "Our Shenzhen Base" section

- [ ] `about-us.html` ([dev](https://china-fulfillment.borufashions.workers.dev/about-us)), lines 378 to 396: copy the whole "FLEET & PREMISES" section. It reuses the existing team-card styles, so no new CSS is needed.
- Images from `images/site/`:
  - `china-fulfillment-cofounder-shenzhen-warehouse-van.webp` + `-400w` `-720w`
  - `pfc-express-delivery-van-shenzhen.webp` + `-400w` `-720w`

## 4. Contact Us: premises photo

- [ ] `Contact-Us.html` ([dev](https://china-fulfillment.borufashions.workers.dev/Contact-Us)), line 423: add the photo above the address block.
- Images from `images/site/`: `pfc-express-truck-shenzhen-warehouse-entrance.webp` + `-400w` `-720w`

## 5. "220+ countries" → "200+ countries"

Production still says 220+ on these pages. Change every instance to **200+** (the repo is already correct):

- [ ] `about-us.html` (5)
- [ ] `dropshipping-fulfillment.html` (5)
- [ ] `express-international-shipping-china.html` (3)
- [ ] `express-international-shipping.html` (2)
- [ ] `news-shenzhen-vs-yiwu-3pl-warehouse.html` (2)
- [ ] `faq.html` (1, in a small stats label)
- [ ] `ddp-shipping-from-china-explained-2026.html` (1 left)
- [ ] `tiktok-shop-fulfillment-from-china-2026.html` (1 left)

Do **not** change the "220+" in `best-china-3pl-companies-2026.html`. That number is a competitor's own claim, quoted on purpose.

## 6. Homepage: missing meta description

The live homepage has no meta description. Add this inside `<head>`:

```html
<meta name="description" content="China 3PL and eCommerce fulfillment from our own Shenzhen warehouse. $0.99 pick and pack, zero inbound fees, DDP included. 6-10 days to the US. Est. 2010."/>
```

Everything else on the homepage (title, images, free-storage wording) already matches the repo.

## 7. Clean-up: remove authoring notes from three live posts

These live pages contain an HTML comment saying "paste into page head". Visitors cannot see it, but anyone who views the page source can. Delete the comment:

- [ ] `avoid-amazon-fba-prep-rejections-china.html`
- [ ] `how-to-fulfil-kickstarter-orders-from-china.html`
- [ ] `china-3pl-vs-self-fulfilling-shopify.html`

---

## Quick check after publishing

- Open each new URL on a phone. The hero and infographic should load, and nothing should run off the side of the screen.
- Paste one new URL into https://search.google.com/test/rich-results. It should find the Article and FAQ data.

Image briefs and style guide, for reference: `IMAGE-BRIEFS-tier10.md`, `IMAGE-STYLE-GUIDE.md`.
