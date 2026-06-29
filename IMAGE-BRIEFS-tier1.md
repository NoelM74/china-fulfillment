# Image Briefs — Tier 1 Blog Posts (H2 2026)

Production checklist for the imagery in the four Tier 1 drafts. Each post references a hero image at `/images/blog/{slug}.webp` that **must be generated before publishing** (the build embeds the path; the file does not exist yet). Optional in-body infographics are listed where they would lift comprehension and dwell time.

## House image conventions (match existing posts)
- **Format / size:** `.webp`, hero rendered at `1200×440` (the template sets `width="1200" height="440"`). Export at 2× (2400×880) then compress to WebP, target under ~150 KB.
- **Path / naming:** hero = `/images/blog/{slug}.webp`. Infographics follow the existing pattern `/images/blog/infographic-{topic}.webp`.
- **Palette:** brand navy + orange (the site's `--ink` navy / orange accent), white space, clean. Avoid stocky "global business handshake" clichés.
- **Style:** photographic-realist for heroes (real Shenzhen-warehouse feel), flat vector for infographics. No fake logos, no fabricated brand names, no real couriers' trademarks rendered as if endorsing.
- **Alt text:** already written into each draft's frontmatter (`hero_alt`) and the in-body `![alt]` — keep it; it is the SEO/accessibility text.
- **Mobile-first:** heroes are wide (1200×440) and crop on small screens — keep the subject centred and avoid edge text. Infographics should read top-to-bottom (single column) so they don't shrink illegibly on a phone; avoid wide multi-column layouts.

---

## 1. US De Minimis Is Gone — `us-de-minimis-ended-2026-china-sellers-guide`

**Hero** (`/images/blog/us-de-minimis-ended-2026-china-sellers-guide.webp`)
- *Alt (set):* "Parcels from China being held for formal US customs entry after the $800 de minimis exemption was suspended in 2026"
- *Prompt:* "Photorealistic wide banner, a US customs inspection area at a parcel hub, a conveyor of small brown e-commerce parcels paused behind a red 'HOLD — FORMAL ENTRY REQUIRED' sign, a customs officer with a tablet scanning a package, soft warehouse daylight, muted navy and orange accent tones, shallow depth of field, centred composition, no readable brand logos, no text overlays. 2400×880, cinematic, documentary style."

**Optional in-body infographic** — *"The per-parcel trap"* (`/images/blog/infographic-de-minimis-cost-stack.webp`)
- A single-column vertical bar comparison for one $25 order: **Before** (Product $25, Duty $0, Entry $0) vs **After** (Product $25, Duty ~$8–9, Entry/broker $4–25). Title: "Why direct small parcels to the US stopped paying." Navy bars, orange highlight on the new costs.
- *Prompt:* "Clean flat vector infographic, vertical single-column layout for mobile, two stacked bar comparisons labelled 'Before de minimis' and 'After de minimis', showing product cost plus duty plus per-parcel customs entry fee, navy bars with one orange highlighted segment, large legible sans-serif numbers, white background, no clutter. 1200×1500."

---

## 2. TikTok Shop Fulfillment from China — `tiktok-shop-fulfillment-from-china-2026`

**Hero** (`/images/blog/tiktok-shop-fulfillment-from-china-2026.webp`)
- *Alt (set):* "TikTok Shop cross-border orders being picked and packed for US buyers in a Shenzhen 3PL warehouse in 2026"
- *Prompt:* "Photorealistic wide banner, a modern Shenzhen fulfilment warehouse, a worker at a packing bench scanning and boxing small consumer-product orders, a phone on a ring-light tripod nearby suggesting social commerce, bright clean lighting, navy and orange brand accents on shelving labels, centred subject, no readable third-party logos, no text overlays. 2400×880, documentary product-ops style."

**Optional in-body infographic** — *"Local vs Cross-border (CBT)"* (`/images/blog/infographic-tiktok-local-vs-cbt.webp`)
- Two-row comparison: **Local store** (dispatch inside US → must use TikTok logistics) vs **Cross-border / CBT** (dispatch from declared overseas warehouse → fulfil from China, ship DDP, match origin tracking). Mirror the draft's table.
- *Prompt:* "Flat vector comparison infographic, single-column stacked for mobile, two cards titled 'Local store' and 'Cross-border (CBT) store', each with 3 short bullet rows and a simple icon (a US pin vs a globe/warehouse), navy headers, orange accent on the CBT card, generous whitespace, legible at phone size. 1200×1500."

---

## 3. Hybrid Fulfillment Model — `china-us-hybrid-fulfillment-model-2026`

**Hero** (`/images/blog/china-us-hybrid-fulfillment-model-2026.webp`)
- *Alt (set):* "Diagram of a hybrid fulfillment model with bestselling SKUs in a US warehouse and long-tail SKUs shipping from a Shenzhen warehouse in 2026"
- *Prompt:* "Clean conceptual banner, a stylised world map showing two warehouse icons — one labelled 'China (long-tail + global)' over Shenzhen, one labelled 'US (bestsellers, 2–4 day)' over the United States — connected by a freight arrow from China to the US warehouse and direct-to-consumer arrows fanning out from China, navy and orange palette, flat modern vector, centred, minimal text, mobile-safe central composition. 2400×880."

**Optional in-body infographic** — *"Split-by-velocity decision"* (`/images/blog/infographic-hybrid-split.webp`)
- Render the draft's table as a visual: left column 'Keep in China' (slow / unproven / new launch / global), right column 'Move to US' (fast / steady / proven / US buyers), with a central velocity arrow. (The HTML already has the table; this is an optional richer visual for social/OG sharing.)
- *Prompt:* "Flat vector decision infographic, a horizontal velocity arrow from 'Slow / long-tail' to 'Fast / bestseller', two grouped lists beneath labelled 'Keep in China' and 'Move to US warehouse', navy and orange, clean sans-serif, single-column friendly, white background. 1200×1400."

---

## 4. DDP Shipping Explained — `ddp-shipping-from-china-explained-2026`

**Hero** (`/images/blog/ddp-shipping-from-china-explained-2026.webp`)
- *Alt (set):* "DDP parcel from China being delivered to a customer's door with all duties and taxes already paid in 2026"
- *Prompt:* "Photorealistic wide banner, a courier handing a small parcel to a smiling customer at a home doorway, a subtle green 'Duties & taxes paid' check badge motif, warm natural light, navy and orange accent, centred subjects, no readable courier logos, no on-image text. 2400×880, lifestyle-realist."

**Optional in-body infographic** — *"DDP vs DAP at the door"* (`/images/blog/infographic-ddp-vs-dap.webp`)
- Two delivery scenes side by side: **DDP** = customer receives parcel, pays nothing (green tick); **DAP** = courier presents a surprise duty bill (red exclamation). Reinforces the draft's comparison table.
- *Prompt:* "Flat vector infographic, single-column stacked for mobile, two scenes: top 'DDP — nothing to pay' with a parcel and green check, bottom 'DAP — surprise duty bill' with a parcel and red alert, navy and orange palette, simple line icons, short captions, white background, legible on a phone. 1200×1400."

---

## Notes for production
- **Generate heroes first** — they are referenced by the live build; the four pages will show a broken image until the WebP files exist at the paths above.
- Infographics are optional but recommended for the two most-shared posts (#1 US de minimis and #4 DDP) because they earn featured-snippet/image-pack visibility and improve mobile dwell time.
- If embedding the infographics in-body later, add them with descriptive markdown alt text (`![alt](/images/blog/infographic-....webp)`) in the draft and re-run `scripts/build_blog.py`. The build leaves in-body images in place (it only strips the first image as the hero).
- Do **not** render real courier or platform trademarks (DHL/FedEx/UPS/TikTok/Amazon) as logos inside generated images — describe the action instead, to avoid trademark issues.
