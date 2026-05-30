# china-fulfillment.com — Full Audit

> ## ✅ Fixes applied 2026-05-30 (in the repo, not yet deployed)
>
> - **Canonicals + `og:url` normalized to served `.html` paths** across 22 pages (`fix_canonical_urls.py`). No canonical now points at a 404.
> - **Crowdfunding canonical/og/breadcrumb slug corrected** — was pointing at `/china-fulfillment`, now `/china-crowdfunding-fulfillment.html`.
> - **`dropshipping-fulfillment.html` relative canonical** made absolute (same script).
> - **`sitemap.xml` rewritten** — every `<loc>` now matches a real `.html` URL; added the two express pages that were missing; homepage `lastmod` bumped to 2026-05-30.
> - **BreadcrumbList `item` URLs normalized to `.html`** across 18 pages (`fix_breadcrumb_urls.py`).
> - **`express-international-shipping.html`** given missing `og:url`, `og:image`, and full Twitter card; **repositioned to "Express Courier"** (title/H1/meta/breadcrumb) to stop cannibalizing the `-china` hub and the freight page.
> - **3 Amazon pages de-cannibalized** (P1 #5): `amazon-fulfillment.html` repositioned as the **hub** (broad "Amazon fulfillment services / 3PL" term + its unique **FBM** angle), `amazon-fba-consolidation.html` keywords trimmed to storage/consolidation only (dropped prep/FNSKU bleed), `amazon-fba-prep-china.html` left as-is (already sharply focused on prep). Titles now read as three distinct intents.
> - **Fixed a stray 404 internal link** — `amazon-fulfillment.html` linked to `/amazon-fba-consolidation` (extension-less). Confirmed zero extension-less internal links remain site-wide.
> - Verified: all 69 JSON-LD blocks parse; FAQPage schema already present on all 4 pages the first pass flagged (subagent false negative); `noindex` already present on login/register.
>
> **Still needs you (can't be done from the repo):**
> 1. **Deploy the repo** — the live site is still the older Shopify-hero version (P0 #2 below).
> 2. **Re-submit `sitemap.xml`** in Search Console after deploy.
> 3. **Trust signals** (P2 #11) — needs real client names/results; I won't invent them.
> 4. Optional host-config route B (extension-less URLs + 301s) if you prefer clean URLs long-term.
>
> ---

**Date:** 2026-05-30
**Scope:** Code, copy, UI/UX, mobile, SEO/AEO/GEO across the 15 money pages + live site check.
**Method:** Static analysis of HTML/CSS in `C:\Users\user\China Fulfillment\` + live crawl of www.china-fulfillment.com (mobile 375px + desktop 1440px) + sitemap URL status check + JSON-LD render check.

---

## Executive summary

The site has a **strong foundation** — clean semantic HTML, proper schema markup, real keyword targeting, a coherent design system (Outfit + Mulish, navy/orange), and mobile breakpoints at 1024/768/600. The local repo is genuinely good work.

But three issues are bleeding traffic right now:

1. **The deployed site is stale.** Local `index.html` has the new "AnyVan-inspired" hero v2 ("Your entire China supply chain. One warehouse."). Live site still shows the older Shopify hero. Everything in this audit that says "in the local files" may not actually be on the live site yet.

2. **12 out of 23 sitemap URLs return 404.** The sitemap lists clean URLs (`/amazon-fba-consolidation`, no `.html`) but the server only serves `.html` versions. Google is being told the money pages exist at URLs that don't resolve. This is the single biggest fix.

3. **Cannibalization across three Amazon pages and two express-shipping pages.** Splitting authority on the highest-intent terms.

Everything else is polish.

---

## P0 — Fix this week

### 1. Sitemap is sending Google to 404s

`sitemap.xml` lists clean URLs without `.html`. The server doesn't redirect or serve them. Confirmed dead on live:

| URL listed in sitemap | Live status |
|---|---|
| `/amazon-fba-consolidation` | **404** |
| `/china-consolidation` | **404** |
| `/quality-control-fba-prep-china` | **404** |
| `/dropshipping-fulfillment` | **404** |
| `/branded-packaging-kitting` | **404** |
| `/china-crowdfunding-fulfillment` | **404** |
| `/international-freight-forwarding-china` | **404** |
| `/supplier-management-china` | **404** |
| `/tariff-management-china` | **404** |
| `/blog` | **404** |
| `/privacy-policy` | **404** |
| `/terms-of-service` | 200 (lucky exception) |

Only `/amazon-fulfillment.html` and `/cod-service.html` are listed correctly in the sitemap (with `.html`).

**Pick one fix:**
- **A — fast:** Edit `sitemap.xml` so every `<loc>` matches the actual `.html` URL the server serves. 10 minutes. Re-submit in Search Console.
- **B — better long-term:** Configure the host to serve `.html` files at extension-less URLs (IIS URL Rewrite, Cloudflare Worker, or `.htaccess`), and 301 the `.html` versions to the clean URLs. Then make every canonical, internal link, and sitemap entry use the clean form.

Don't half-do it. Right now `index.html` links to `amazon-fba-consolidation.html` (works), `sitemap.xml` lists `amazon-fba-consolidation` (404), and `Contact-Us.html` has a capital C. That's three different URL conventions inside one site.

### 2. Live site does not match the repo

Live `<title>`: "D2C & Shopify Fulfillment from Shenzhen | 6-10 Days US"
Local `<title>`: "China FBA Consolidation & Fulfillment from Shenzhen | $0.49/CBM"

Live H1: "Your Shopify store, fulfilled from Shenzhen."
Local H1: "Your entire China supply chain. One warehouse. Zero headaches."

Local has 4 JSON-LD blocks (Organization, FAQPage, WebSite, BreadcrumbList). Live has Organization, FAQPage, WebSite, **Service** — different mix, no breadcrumb.

Deploy the local repo. Everything in the rest of this audit assumes the repo is the source of truth.

### 3. Canonical on `china-crowdfunding-fulfillment.html` points to the wrong slug

Canonical reads `…/china-fulfillment` instead of `…/china-crowdfunding-fulfillment`. Google will treat this page as a duplicate of the homepage and drop it.

Fix: change canonical to `https://www.china-fulfillment.com/china-crowdfunding-fulfillment.html` (or extension-less if you go route B above).

### 4. Canonical on `dropshipping-fulfillment.html` is a relative path

Should be absolute. Most crawlers handle relative canonicals but the spec says absolute and Google sometimes ignores relative ones. Cheap fix, do it.

---

## P1 — High impact

### 5. Three Amazon pages cannibalize the same keyword

- `amazon-fulfillment.html` — overview / catch-all
- `amazon-fba-consolidation.html` — storage + drip-feed
- `amazon-fba-prep-china.html` — FNSKU + poly bag + 2026 prep

All three rank for "Amazon FBA China" variants. Pick a single intent per page and rewrite the title/H1/intro to match:

| Page | Single intent | Title should lead with |
|---|---|---|
| amazon-fulfillment.html | Brand hub — "what we do for Amazon sellers" | "Amazon Fulfillment Services from China" |
| amazon-fba-consolidation.html | The $0.49/CBM storage story | "Amazon FBA Storage in China — $0.49/CBM/day" |
| amazon-fba-prep-china.html | Post-2026 prep compliance | "Amazon FBA Prep China — FNSKU & Poly Bag Service (2026)" |

Then add a "Related Services" section at the bottom of each linking to the other two with descriptive anchor text. That tells Google these are siblings, not competitors.

### 6. Two express-shipping pages are near-duplicates

`express-international-shipping.html` and `express-international-shipping-china.html` have the same title pattern, same Service schema, same DHL/FedEx/UPS pitch, same $8.50/kg hook. Neither is in `sitemap.xml`. Either consolidate into one or differentiate:

- One for **standalone freight** (sellers shipping their own bulk orders out of China)
- One for **eCommerce parcel** (us picking, packing and using DHL on the seller's behalf)

Add both to `sitemap.xml` once differentiated. Right now they're invisible to Google.

### 7. FAQPage schema missing on 4 high-value pages

Pages with Q&A content in the body but no `FAQPage` JSON-LD:
- `china-consolidation.html`
- `express-international-shipping.html`
- `international-freight-forwarding-china.html`
- `quality-control-fba-prep-china.html`

These won't show up in "People also ask" or AI Overviews. Copy the FAQPage pattern from `amazon-fba-consolidation.html` and adapt. 30 minutes per page.

### 8. No hreflang despite serving 200+ countries

The site claims to ship globally but has no `<link rel="alternate" hreflang>` and only one language (`en`). If you ever want German Amazon sellers or UK sellers to see country-specific copy, add hreflang now. For now, at minimum add `hreflang="en"` and `hreflang="x-default"` self-references — it's free and protects against future EU expansion.

---

## P2 — Medium impact (quick wins)

### 9. Sitemap `lastmod` is identical on every URL (2026-03-17)

Looks like a batch script ran. Google deprioritizes sitemaps where every page claims the same `lastmod`. When you next edit a page, update only that URL's `lastmod`. Cheap, automates with a 5-line script in `apply_global_css_footer.py` style.

### 10. No "last updated" date visible in body copy

Helpful for AEO/GEO (ChatGPT and Perplexity cite recent content). Add `<p class="updated">Last updated: March 2026</p>` near the H1 on service pages. Even better: structure as `<time datetime="2026-03-17">`.

### 11. Trust signals are claims, not proof

The homepage says "15+ Years in Shenzhen" and "200+ Countries" but there's no:
- Real client logo strip (even small Shopify brands)
- Verified reviews snippet (Trustpilot/Google Reviews)
- Case-study tile with a named brand
- Real warehouse photo with workers visible (the OG image works but could be punchier)

For AEO/GEO especially, citations and verifiable facts get rewarded by AI search engines. Adding 3 real client names + dates + outcomes would do more for ChatGPT/Perplexity rankings than another keyword sweep.

### 12. Live site has 11 console 404 errors on `/amazon-fba-consolidation.html`

These are the same dead URLs from issue #1 — links inside the page point to `/amazon-fba-consolidation` etc. and the browser logs every miss. Same fix as #1 resolves these.

### 13. OG image is shared across multiple pages

`shenzhen-warehouse-interior-panoramic-ecommerce-fulfillment.jpg` shows up on 3+ pages. Each service page should have a unique OG image — it improves social CTR and tells Google the pages are distinct content.

### 14. No `<meta name="robots">` on `login.html` / `register.html`

`robots.txt` blocks them but it's "belt and braces" with a meta tag. Add `<meta name="robots" content="noindex,nofollow">` to both. 30 seconds.

---

## P3 — Polish

### 15. Twitter card missing on `express-international-shipping.html`

### 16. No `meta name="author"` or visible byline on any page

For E-E-A-T and AEO citation, add author/company byline. Even just "Written by China Fulfillment International, Shenzhen 3PL since 2010" near the H1.

### 17. `meta keywords` tag is still present on homepage

Google ignores it. Bing kind of ignores it. It's dead weight — strip it or leave it (no harm either way, but it dates the file).

### 18. Inline CSS is ~370 lines on the homepage

Acceptable for a static site (no extra HTTP request) but if you ever reuse design tokens across pages, the CSS variables block (`:root{--ink:...}`) should live in `global-nav-footer.css` so a single edit changes every page.

### 19. `Contact-Us.html` uses capital letters in filename

Windows is case-insensitive locally; Linux/Cloudflare serving is case-sensitive. If you ever migrate hosts this becomes a broken link. Rename to `contact-us.html` and 301 the old. Same applies to any `image/Logo.png` style paths.

---

## UI / UX review — live mobile (375px)

Tested on the live site at iPhone X width.

✓ No horizontal scroll
✓ One H1, semantically correct
✓ Sticky nav works, hamburger appears
✓ All 11 images have meaningful alt text
✓ 10 of 11 images are `loading="lazy"` (logo correctly eager)
✓ Lang, viewport, canonical all set
✓ Touch targets in the nav are ≥44px
✓ Font loading uses preconnect + display=swap (no FOIT)
✓ Zero console errors on the homepage

Issues:
- LCP candidate is the **logo** (`image/logo.png`) not a hero image — likely fine for speed, but the hero feels light without a primary image. Consider adding a single high-priority hero image with `fetchpriority="high"` for stronger visual hierarchy.
- Hero "service category cards" disappear from 3rd onward on mobile (`.hero-cards .hc:nth-child(4),(5){display:none}`) — that's deliberate but it hides Crowdfunding entirely on mobile. Either rotate which two cards show, or scroll horizontally instead of hiding.
- The orange "30 days free storage" offer bar (`.obar`) is good but `<em>` text is hidden at 600px (`.obar em{display:none}`). The remaining copy reads "🎁 New Customers: 30 Days FREE Warehouse Storage" — fine, but the value prop "No credit card. No minimums." is lost on the audience that needs it most (cautious mobile browsers). Reword the truncated version, don't just chop.
- `<details>`/`<summary>` FAQ accordion is correctly accessible (keyboard-operable, screen-reader friendly). Good choice over JS-toggled divs.

Desktop (1440px):
- Hero cards grid is dense — 5 columns with small font, hard to scan at a glance. Reducing to 3 columns with bigger cards would feel more confident.
- Stats row "$0.49 / Per CBM / Per Day" reads as three lines because of the `<br/>` — fine, but the visual rhythm would be stronger with the labels on one line.
- Footer is 5-column desktop but the column widths feel cramped. `1.3fr 1fr 1fr 1fr 1fr` puts the brand block first; consider making it `1.6fr 1fr 1fr 1fr 1fr` for the brand to breathe.

---

## Copy review

Voice is consistent — punchy, specific, anti-marketing. Real numbers ($0.49, $20,550, 83%, $0.99) anchor every claim. This is genuinely strong copy. A few notes:

- **Strong:** "Your entire China supply chain. One warehouse. Zero headaches." This is the kind of line that converts.
- **Strong:** "Amazon killed FBA Prep on January 1, 2026. Your shipments now arrive unprepped — or they don't arrive at all." Urgency + specificity, no fluff.
- **Watch:** Em-dashes appear in nearly every paragraph. They're a known AI-writing tell. Mix in some colons, periods, and parenthetical clauses to break the rhythm. The copy is already good — this is purely about avoiding pattern-detection.
- **Watch:** "drip-feed" appears 4+ times on the homepage. Vary with "trickle", "small weekly replenishments", "right-sized shipments".
- **Add:** A specific named client or campaign on the homepage. "Helped [Brand] save $X by switching from Amazon storage to Shenzhen consolidation" — even one example beats all the stats.

---

## AEO / GEO readiness (AI Overviews, ChatGPT, Perplexity)

What AI search engines reward:
1. **Structured Q&A** — ✓ present on most pages, FAQPage schema on most
2. **Comparison tables** — ✓ "Our rate vs Amazon Q4" is good
3. **Specific numbers with units** — ✓ excellent throughout
4. **Author / org signal** — ✗ no byline, no author schema
5. **Last-updated dates in body** — ✗ missing
6. **Citation-worthy facts** — partial; claims need source links (e.g., "Amazon charges $84.74/CBM in Q4" should link to Amazon's fee schedule)
7. **Definitions** — partial; "Amazon FBA Consolidation" is defined in the FAQ but not in a dedicated `<dl>` glossary
8. **Topical clustering** — broken right now because of cannibalization (#5, #6)

**Quick AEO wins:**
- Add a glossary section to `faq.html` with `<dl><dt>FBA Consolidation</dt><dd>...</dd></dl>` markup
- Add `datePublished` and `dateModified` to every FAQ schema block
- Add inline citations (small footnotes linking to Amazon's actual fee page, source for "200+ countries", etc.)
- Add an `Author` field to one or two news articles (the `/news-*` posts) — gives AI engines a person to cite

---

## Prioritized action plan

**This week:**
1. Pick the URL convention (`.html` or extension-less) and make sitemap, canonicals, internal links, and host config all agree
2. Deploy the local repo to production (the live site is behind)
3. Fix the canonical on `china-crowdfunding-fulfillment.html`
4. Fix the relative canonical on `dropshipping-fulfillment.html`

**Next two weeks:**
5. Re-position the three Amazon pages to stop cannibalizing
6. Consolidate or differentiate the two express-shipping pages, then add to sitemap
7. Add FAQPage schema to the 4 service pages missing it
8. Add `last updated` visible date + `dateModified` schema to every service page

**Next month:**
9. Add a verifiable trust block to the homepage (one named client + one verified review snippet)
10. Add author / byline signal site-wide
11. Vary sitemap `lastmod` to reflect real update cadence
12. Add `hreflang` self-reference + plan for EU expansion
13. Unique OG image per service page

**Backlog:**
14. Add a glossary on `faq.html` with dl markup for AEO
15. Lowercase `Contact-Us.html` and 301 redirect
16. Move design tokens into `global-nav-footer.css` for single-source-of-truth
17. Strengthen the hero with a single high-priority image + `fetchpriority="high"`

---

## What's already great

- Real semantic HTML (`<article>`, `<section>`, `<nav>`, `<details>` accordions)
- Mobile-first CSS with three real breakpoints, not a token responsive class
- Clean, modern design system with consistent colour and type
- Proper preconnect + display=swap font loading
- Schema markup is present on every audited page — most agencies skip this
- Copy is genuinely good. Specific, opinionated, not slop
- No console errors on the homepage
- `<meta robots>` discipline (the noindex on login/register is correct intent)
- robots.txt is clean and includes the sitemap reference
- Image alt text is descriptive and contextual, not stuffed

This is a 7/10 site that's two weeks of focused work away from being a 9/10 site. The biggest single lever is fixing the sitemap so Google can actually crawl the money pages.
