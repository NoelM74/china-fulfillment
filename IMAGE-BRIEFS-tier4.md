# Image Briefs — Group A / September Posts (Tier 4, H2 2026)

Same conventions as Tier 1–3: `.webp`, hero `1200×440` at 2× under ~150 KB; brand navy + orange; photographic-realist heroes, flat-vector single-column infographics; alt text already in the drafts; mobile-safe centred composition. **These 3 posts are staged `noindex` and out of the sitemap/blog index** — generate the images to complete them; nothing goes live until you say so. No real courier/retailer/agency trademarks as logos.

Six images: 3 heroes + 3 infographics.

---

## 1. China to Australia — `china-to-australia-fulfillment-2026`

**Hero** (`/images/blog/china-to-australia-fulfillment-2026.webp`)
- *Alt:* "Parcels shipped DDP from a Shenzhen warehouse to Australian customers with GST collected at checkout in 2026"
- *Prompt:* "Photorealistic wide banner, a parcel arriving at a sunny Australian suburban doorway with a subtle 'GST paid' green check motif, warm daylight, navy and orange accents, centred subject, no readable courier logos, no on-image text. 2400×880, lifestyle-realist."

**Infographic** (`/images/blog/infographic-australia-gst-threshold.webp`) — *embedded in draft*
- *Alt:* "How Australia's A$1,000 GST threshold works: for orders at or under A$1,000 a GST-registered seller charges 10% GST at checkout with no duty, while orders above A$1,000 have GST and duty assessed at the border, all prepaid under DDP"
- *Prompt:* "Flat vector infographic, single column for mobile, a threshold split: top card '≤ A$1,000 → 10% GST at checkout, no duty'; bottom card '> A$1,000 → GST + duty at the border'; footer band 'DDP = all prepaid, customer pays nothing'; navy headers, orange accents, phone-legible, white background. 1200×1500."

---

## 2. China to Canada — `china-to-canada-fulfillment-2026`

**Hero** (`/images/blog/china-to-canada-fulfillment-2026.webp`)
- *Alt:* "Parcels shipped DDP from a Shenzhen warehouse to Canadian customers clearing customs with duty and GST prepaid under CARM in 2026"
- *Prompt:* "Photorealistic wide banner, a parcel delivered to a Canadian doorstep in cool daylight (subtle maple-leaf cue, no flag rendered as a logo), a 'duty & tax paid' green check motif, navy and orange accents, centred subject, no readable courier logos, no on-image text. 2400×880, lifestyle-realist."

**Infographic** (`/images/blog/infographic-canada-carm-duty.webp`) — *embedded in draft*
- *Alt:* "Canada import reality for goods from China: CAD$20 de minimis, above which GST 5% plus provincial tax and duty apply; importers of record must be CARM-registered; DDP prepays everything so the customer pays nothing at the door"
- *Prompt:* "Flat vector infographic, single column for mobile: top card '< CAD$20 → duty & tax free'; middle card '> CAD$20 → GST 5% + provincial tax + duty'; a callout 'Commercial importers: register on CARM'; footer band 'DDP = all prepaid'; navy headers, orange accents, phone-legible, white background. 1200×1500."

---

## 3. Supplements & Nutraceuticals — `china-fulfillment-supplements-nutraceutical-brands`

**Hero** (`/images/blog/china-fulfillment-supplements-nutraceutical-brands.webp`)
- *Alt:* "Supplement and nutraceutical products being lot-tracked, batch-controlled and packed in a Shenzhen warehouse for DDP shipping to US customers in 2026"
- *Prompt:* "Photorealistic wide banner, a clean warehouse bench with supplement bottles and blister packs being scanned for lot/batch numbers, a subtle 'lot • expiry' label motif, bright clinical lighting, navy and orange accents, centred, no readable brand names on labels, no on-image text. 2400×880, documentary product-ops style."

**Infographic** (`/images/blog/infographic-supplement-compliance-split.webp`) — *embedded in draft*
- *Alt:* "What the brand and importer own versus what the 3PL owns for China-to-US supplement fulfilment: FDA facility registration, FSVP, GMP manufacturing and labelling on the brand side; lot and expiry control, storage and DDP shipping on the fulfilment side"
- *Prompt:* "Flat vector two-column responsibility infographic, single-column stacked on mobile, left 'The brand & importer own' (FDA facility registration, FSVP + DUNS, GMP manufacturing, labelling), right 'Your 3PL owns' (lot & batch control, first-expiry-first-out, storage, DDP shipping), each row a short label + icon, navy headers with orange accent on the 3PL side, white background, phone-legible. 1200×1500."

---

## Production notes
- These 3 pages are `noindex` and out of the sitemap/blog index (staged, not published). Generating the images completes them.
- The 3 infographics are embedded in-body, so they must exist at the paths above before publish or the in-body image will 404.
- Upload to `images/blog/` on the `claude/blog-serp-keyword-analysis-j26pym` branch (exact lowercase filenames, `.webp`).
- To publish later: delete each page's `noindex` line (tagged `UNPUBLISHED: remove this line to publish`), add the 3 sitemap entries (dates Sep 2 / 4 / 9), restore the 3 blog cards (re-run `scripts/build_blog.py`), then merge.
