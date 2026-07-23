# Image Briefs — Tier 2 Blog Posts (H2 2026)

Same conventions as `IMAGE-BRIEFS-tier1.md`: `.webp`, hero `1200×440` exported at 2× and compressed under ~150 KB; brand navy + orange; photographic-realist heroes, flat-vector infographics; alt text already written into the drafts; mobile-safe centred composition; infographics single-column so they stay legible on a phone. **Heroes must be generated before publishing** (the build references the path). Do not render real platform/courier trademarks (Temu, Shein, Amazon, DHL) as logos — depict the action instead.

Four images needed: 2 heroes + 2 infographics.

---

## 5. Temu/Shein Semi-Managed — `temu-shein-semi-managed-fulfillment-china`

**Hero** (`/images/blog/temu-shein-semi-managed-fulfillment-china.webp`)
- *Alt (set):* "Temu and Shein semi-managed orders being picked, packed and labelled for dispatch in a Shenzhen 3PL warehouse in 2026"
- *Prompt:* "Photorealistic wide banner, a busy Shenzhen fulfilment warehouse, workers at packing stations picking and labelling small fashion and consumer-goods orders for fast dispatch, a wall clock and a 'same-day dispatch' motif suggesting tight SLAs, bright clean lighting, navy and orange accents on shelving and tape, centred subjects, no readable brand logos, no on-image text. 2400×880, documentary product-ops style."

**In-body infographic** (`/images/blog/infographic-semi-managed-routes.webp`) — *already embedded in the draft*
- *Alt (set):* "Two compliant routes for semi-managed fulfilment from China: DDP express direct from Shenzhen versus consolidate and bulk-ship to an in-market warehouse for local fulfilment"
- *Prompt:* "Flat vector infographic, single-column stacked for mobile, two route cards: top 'Route 1 — DDP express direct from Shenzhen' showing a parcel flying from China to a customer with a green duty-paid tick; bottom 'Route 2 — consolidate and bulk-ship to an in-market warehouse' showing pallets going China→US/EU warehouse then short local hops to customers. Navy headers, orange accents, simple line icons, short captions, generous whitespace, legible at phone size. 1200×1500."

---

## 6. Amazon FBA Direct vs US 3PL First — `amazon-fba-direct-vs-us-3pl-first-2026`

**Hero** (`/images/blog/amazon-fba-direct-vs-us-3pl-first-2026.webp`)
- *Alt (set):* "Decision between shipping inventory direct from China to Amazon FBA versus staging at a US 3PL transload warehouse first in 2026"
- *Prompt:* "Photorealistic wide banner, a conceptual fork-in-the-road logistics scene: on one side a container moving straight from a ship to a fulfilment centre, on the other side a container being unloaded and split into several smaller trucks at a transload warehouse near a port, soft daylight, navy and orange accents, balanced centred composition, no readable brand logos, no on-image text. 2400×880, cinematic documentary style."

**In-body infographic** (`/images/blog/infographic-fba-staging-routes.webp`) — *already embedded in the draft*
- *Alt (set):* "Comparison of two routes for China inventory in 2026: direct to Amazon FBA versus staging at a US 3PL transload warehouse first, showing placement fees, drip-feed and reserve stock"
- *Prompt:* "Flat vector comparison infographic, single-column stacked for mobile, two columns/cards 'Direct to FBA' vs 'Stage at a US 3PL first', each with 4 short rows (placement fee, drip-feed, reserve stock, handling steps) using simple check/cross and arrow icons, navy headers with orange accent on the staged-route advantages, white background, legible on a phone. 1200×1500."

---

## Production notes
- Generate the two heroes first; the pages reference them and will show a broken image until the files exist.
- The two infographics are already embedded in-body in the drafts, so they also need to exist at the paths above before publish (or the in-body image will 404). If you'd rather hold them, remove the `![...](...)` line from the relevant draft and re-run `scripts/build_blog.py`.
- After adding images, no rebuild is needed unless you change the markdown; the paths are already wired.
