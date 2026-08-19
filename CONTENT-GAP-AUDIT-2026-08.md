# Content Gap Audit & SERP Research — Next 5 Posts

**Date:** August 2026
**Scope:** Full content audit of 58 indexable pages (36 articles + 18 service/commercial pages), plus SERP research to identify unserved search demand.
**Purpose:** Find the holes in the blog that people are actively searching for, and prioritise the next 5 posts.

---

## Part 1 — Site audit findings

### 1.1 What is already strong

Technical SEO is in good shape after the August optimisation pass: every page has one H1, a canonical, a meta description inside 110–160 chars, a title inside 60 chars, Twitter Card and og:image, and valid Article/Service/FAQPage JSON-LD with a matching visible FAQ. There are no duplicate titles or metas, no orphan pages, and no external image hotlinks.

**Coverage is genuinely broad:**

| Dimension | Covered |
|---|---|
| **Corridors** | US, UK, EU/Germany, Australia, Canada |
| **Channels** | Amazon FBA (deep), TikTok Shop, Temu/Shein, Walmart WFS, Shopify, Kickstarter/Indiegogo, dropshipping, COD (SE Asia) |
| **Verticals** | Beauty/skincare, supplements, apparel/fashion, batteries/electronics |
| **Operations** | Returns, kitting, QC, consolidation, Q4 peak, CNY, DDP, pricing, hybrid model, 3PL-vs-self, tariffs/landed cost, air-vs-sea, prep rejections |

### 1.2 The structural problem: articles do not link to each other

This is the highest-impact finding in the audit, and it is invisible in a page-by-page check.

Internal links currently flow **blog → service pages** (good for conversion) but almost never **blog → blog** (essential for topical authority).

| Metric | Value |
|---|---|
| Article pages | 36 |
| Total blog-to-blog links | 44 (**avg 1.2 per article**) |
| Articles receiving **zero** links from other articles | **20 of 36** |
| Articles sending **zero** links to other articles (dead ends) | **16 of 36** |
| **Of the 15 posts published in August, receiving zero inbound article links** | **12 of 15** |

**Why this matters.** Google infers topical clusters largely from internal linking. Right now the corridor posts (UK, Germany, Canada, Australia) do not reference each other, the vertical posts (beauty, supplements, apparel, batteries) do not reference each other, and nothing older points forward to the 15 posts just published. Each post therefore competes as an isolated page rather than as part of an authoritative cluster, and the new posts inherit almost no internal link equity from the established pages.

**The existing hubs are the right ones** — DDP (10 inbound), US de minimis (8), hybrid model (8). The problem is that the long tail is not wired into them, and they are not wired back out.

**Recommended fix (do this before or alongside the next 5 posts):** a dedicated internal-linking pass adding roughly 4–6 contextual blog-to-blog links per article, built around four clusters:

- **Corridors:** UK ↔ Germany/EU ↔ Canada ↔ Australia ↔ (Japan), all pointing to DDP as the hub
- **Verticals:** beauty ↔ supplements ↔ apparel ↔ batteries, all pointing to returns and kitting
- **Channels:** TikTok ↔ Temu/Shein ↔ Walmart ↔ FBA-direct-vs-3PL
- **Duty/customs:** US de minimis ↔ EU de minimis ↔ tariffs/landed cost ↔ DDP

This is a low-effort, high-return change: it lifts the whole library rather than adding to it, and it is the single fastest way to get the 15 new posts ranking.

### 1.3 Smaller technical items still open

- In-body infographic images have no `width`/`height` attributes (minor CLS/layout-shift cost). Fixable in `scripts/build_blog.py`.
- `robots.txt` carries `Crawl-delay: 1`, which Google ignores. Harmless but removable.
- Four utility pages (login, register, privacy, terms) have no OG tags. Near-zero SEO value; two are noindex.
- **Build caveat:** `scripts/build_blog.py` regenerates every post and re-adds every blog card on each run. Any held/unpublished post must be re-staged (noindex + card removal) after a rebuild.

---

## Part 2 — The 5 recommended posts

Each was validated against live SERP research, checked against the existing 36 articles for cannibalisation, and chosen to span the funnel rather than pile into one stage.

### 1. Incoterms for China Imports: EXW vs FOB vs CIF vs DDP

| | |
|---|---|
| **Target keyword** | `fob vs exw vs ddp china` / `incoterms importing from china` |
| **Funnel stage** | Top / mid (informational) |
| **Audience / geo** | All buyers, global |
| **Priority** | **P0** |

**The gap.** The DDP post is one of the strongest assets on the site (10 inbound links, the natural hub). But DDP is only one of four terms buyers compare, and the site says nothing about EXW, FOB or CIF. Every importer hits this decision before they ever think about a fulfilment partner, and the query has very high, durable volume.

**Why it wins.** It converts the existing DDP page from a standalone explainer into the anchor of a proper Incoterms cluster, and it is a strong AI-Overview/AEO citation candidate because the answer is definitional and structured. It also sets up an honest, differentiated take: most freight-forwarder content pushes FOB because that is what suits the forwarder; the useful angle is *which term suits the seller at which stage*, and why DDP is the right answer for direct-to-consumer parcels specifically.

**Grounded hooks.** FOB is the most common term for China imports and gives cost predictability; EXW shifts export clearance onto the buyer and often costs more than FOB once origin charges land; DDP covers duty and delivery and is the practical choice for D2C and direct-to-FBA. Post-de-minimis, DDP matters more than it did.

---

### 2. How to Choose a China 3PL: The Questions to Ask and the Red Flags

| | |
|---|---|
| **Target keyword** | `how to choose a china 3pl` / `china 3pl questions to ask` |
| **Funnel stage** | **Bottom (commercial)** |
| **Audience / geo** | Shopify + Amazon sellers, global |
| **Priority** | **P0 — highest commercial value** |

**The gap.** Someone searching this is actively shopping for exactly what the business sells, and the site has nothing for them. The closest pages are `china-3pl-vs-self-fulfilling-shopify` (a different decision: whether to outsource at all) and the pricing post (cost, not selection). This is the single clearest bottom-funnel hole.

**Why it wins.** It is the highest-conversion query in the set, and it can be won on honesty rather than volume. The credible version names the red flags candidly — vague "it depends" pricing, long contracts with high monthly minimums, saying yes to everything without explaining how, jumping to a quote before understanding the operation, no verifiable client results — and then answers each one with the company's own published position ($0.99 pick-and-pack with no minimums, $0.49/CBM/day, zero receiving fees, no lock-in). The post sells by being useful, not by claiming superiority.

**Grounded hooks.** Total cost per order commonly runs $5–$20+ once size, complexity and shipping are counted, so a headline pick-and-pack rate is a poor comparison basis. A provider quoting before understanding the operation is the most reliable early warning sign.

---

### 3. Product Compliance for Importing from China: CPC/CPSIA, FCC, CE and UKCA

| | |
|---|---|
| **Target keyword** | `product compliance importing from china` / `cpc certificate amazon china` |
| **Funnel stage** | Mid (informational, high pain) |
| **Audience / geo** | Amazon + Shopify sellers, US/UK/EU |
| **Priority** | **P1** |

**The gap.** Compliance has been handled twice, but only inside verticals: MoCRA in the beauty post, FDA/FSVP in the supplements post. There is no general guide, so anyone selling toys, electronics, or any gated category finds nothing. Amazon's category gating makes this an urgent, blocking problem rather than an academic one.

**Why it wins.** It generalises an angle already proven on the site and extends it to a much larger audience. It also fits the established honesty guardrail perfectly: testing and certification are the **brand's and manufacturer's** responsibility, carried out by accredited third-party labs, and a fulfilment provider cannot certify a product for you. That boundary is a trust signal and a genuine differentiator against providers who imply otherwise.

**Grounded hooks.** Children's products need a Children's Product Certificate based on CPSC-accepted third-party lab testing. Wireless electronics need FCC certification. Amazon generally requires ISO/IEC 17025-accredited lab reports and accepts Chinese labs, since accreditation matters rather than location. US testing does not transfer to the EU or UK — CE and UKCA are separate conformity routes.

---

### 4. Cut Your Shipping Bill: DIM Weight and Packaging Optimisation (2026)

| | |
|---|---|
| **Target keyword** | `dimensional weight shipping cost` / `reduce shipping costs ecommerce 2026` |
| **Funnel stage** | Mid (operational, timely) |
| **Audience / geo** | Shopify + Amazon sellers, US-led, global |
| **Priority** | **P1 — time-sensitive** |

**The gap.** There are pages on branded packaging and source-side kitting, both framed around presentation and assembly cost. Nothing covers the thing sellers actually search for: how box size drives billable weight and how to cut it. Dimensional weight is never explained anywhere on the site.

**Why it wins.** There is a live 2026 news hook, and it maps directly onto services already sold. Right-sizing and repacking are decided at the point of packing — in the Shenzhen warehouse — which makes this a commercially useful topic rather than generic advice.

**Grounded hooks.** From **12 July 2026** USPS changed its DIM divisor from 166 to 139 and began rounding fractional dimensions up to the next whole inch, raising billable weight on lightweight bulky parcels and aligning USPS with UPS and FedEx. Right-sizing (for example, box to poly mailer where protection allows) is reported to cut per-package cost substantially. Pair with the existing kitting and packaging pages.

---

### 5. China to Japan Fulfilment (2026): JCT, Platform Tax and Delivery Times

| | |
|---|---|
| **Target keyword** | `china to japan fulfillment` / `shipping from china to japan ecommerce` |
| **Funnel stage** | Mid (geo/corridor) |
| **Audience / geo** | Shopify + marketplace sellers, JP |
| **Priority** | **P1** |

**The gap.** The corridor cluster covers US, UK, EU/Germany, Australia and Canada. Japan is the largest developed e-commerce market missing, and it is a natural fit for a Shenzhen operation on transit time alone.

**Why it wins.** It completes the corridor set, and it lands on the same story the site already owns twice (US de minimis, EU de minimis) — now playing out in a third major market. That thematic consistency is exactly what builds topical authority, and it gives the Japan post a genuine news hook rather than being a generic corridor page.

**Grounded hooks.** Japan is moving to apply its 10% consumption tax to imported low-value consignments that previously sat under the de minimis threshold, so small parcels no longer arrive tax-free. Under the FY2026 reform, JCT liability shifts to large platform operators (intermediary sales above ¥5bn). JCT is calculated on CIF value plus import duty. Transit from China is short — air roughly 1–2 days, sea roughly 3–7 days — which supports a strong delivery-time story.

---

## Part 3 — Runners-up (validated, not in the top 5)

Each of these has real demand and would be a reasonable substitution:

| Topic | Target keyword | Why it ranked below the top 5 |
|---|---|---|
| **Global de minimis tracker** (US, EU, Mexico, Thailand, Türkiye, Japan, UK 2029) | `de minimis by country 2026` | Excellent authority-consolidating pillar, but overlaps the existing US and EU posts. Best built as an evergreen hub *after* the internal-linking pass. |
| **My shipment is stuck at customs: what to do** | `shipment held by customs` | Strong pain-driven intent (holds typically clear in 1–5 days, exams 2–4 weeks, $1,500–3,000 in charges). Slightly narrower volume. |
| **Switching 3PLs without downtime** | `how to switch 3pl providers` | High-value competitor-displacement content (90-day migration, parallel-run method), but overlaps topic 2's decision journey. Strong follow-up to it. |
| **HS codes and classification** | `hs code for imports from china` | Good intent, but partially served by the tariffs/landed-cost post and tariff-management service page. |
| **Vetting Alibaba suppliers** | `how to verify alibaba supplier` | Large volume, but heavily saturated by sourcing agents, and adjacent to the supplier-management page and QC post. |
| **B2B / wholesale retail fulfilment** (EDI, routing guides, chargebacks) | `b2b retail fulfillment edi chargebacks` | A completely uncovered *audience*, not just a topic. Only worth building if the business actually services retail distribution — confirm capability first. |

---

## Part 4 — Recommended sequence

1. **Internal-linking pass first.** It lifts all 36 existing articles, rescues the 12 isolated new posts, and makes every subsequent post rank faster. Highest return per hour of work in this document.
2. **Post 2 (choose a China 3PL)** — bottom-funnel, fastest commercial payback.
3. **Post 1 (Incoterms)** — biggest informational volume; strengthens the DDP hub.
4. **Post 4 (DIM weight)** — time-sensitive while the USPS change is current.
5. **Post 3 (compliance)** and **Post 5 (Japan)** — durable evergreen assets.

All external claims above are drawn from live SERP research and should be re-verified at drafting time, since rates, thresholds and platform rules move quickly. Anything volatile should be hedged and date-stamped in the published copy, per the standing editorial rule.
