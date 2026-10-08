# China Fulfillment website: notes for Claude

Static HTML source for china-fulfillment.com. Read `README.md` for the build and layout.

- **Production** (www.china-fulfillment.com) is an IIS/ASP.NET CMS. It is **not** deployed from this repo. Noel's team copies changes in by hand, working from `CMS-UPDATE-CHECKLIST.md`.
- **Dev site** (https://china-fulfillment.borufashions.workers.dev/) builds from `main` automatically. It is noindexed (`_headers`), and `.assetsignore` keeps repo internals off it.
- **Branch:** `claude/blog-serp-keyword-analysis-j26pym`. Each batch goes PR → Vercel check passes → merge → sync the branch with main.
- **Generated pages:** blog posts come from `data/content/drafts/*.md` via `scripts/build_blog.py` (template: `news-shopify-fulfillment-china.html`). The three freight pages come from `scripts/build_freight_pages.py` (template: `our-pricing.html`). Edit the source, not only the built HTML, or the next build reverts it.

# Compact instructions

When summarising this conversation, always keep:

1. **Where the site stands.** Which version is live on production and on the dev site, the latest commit and PR numbers on `main`, which `CMS-UPDATE-CHECKLIST.md` sections the team has or hasn't done, and anything half-done (files edited but not committed, PRs open, posts held with noindex).
2. **Noel's decisions, word for word.** Prices, shipping, free storage, returns, the legal, tax and VAT position, product and company facts, and copy approvals. Quote numbers and policies exactly as decided. Never paraphrase them. `## Standing decisions` below is the record; add new decisions to it.
3. **Open questions and steps waiting on Noel or his team.** Who owns each and what it blocks. For example: Cara's own freight rates, confirming the old freight prices (checklist §15), the WeChat ID, production porting.
4. **Actions that were blocked or declined.** Anything a safety rule stopped (writing secrets, bulk deletes, force pushes) and any tool call Noel rejected, with the reason. Do not retry them without asking.
5. **Errors and their fixes,** so the same dead ends aren't repeated. Examples:
   - The build reverts edits made only to built HTML.
   - Fixed line numbers in a generator break when the template changes.
   - The local server on port 8911 dies, so restart it with `setsid`.
   - Chromium needs the proxy CA in NSS, added with certutil.
6. **The hard rules** below.
7. **Standing preferences:** always give the GitHub links to the image brief MD files when images or prompts come up, and give the team GitHub and dev-site links for anything they need to copy.

Drop: long file contents, test and render logs that passed, and step-by-step accounts of finished work. Keep file paths, commit hashes and PR numbers instead.

# Hard rules

- **Never commit private files:** `.env*`, `.dev.vars*`, `.mcp.json`, `data/leads/`, `data/clients/`, `data/conversations/inbox/` (see `.gitignore`). The repo is **public** on GitHub.
- **Secrets never go in the repo, a commit message, a PR or a page.** They go into environment variables, Cloudflare secrets (`wrangler secret put`) or a gitignored `.dev.vars`. Never echo a secret back in chat.
- **No invented claims.** Every number on the site needs a source and a date, or must already be one of Noel's published prices. Market rates are labelled as market references, not our prices. Hedge and date volatile facts. If something can't be verified, leave it out and say so.
- **Never reference Portless** (a competitor).
- **Editorial style:** no em dashes in prose, no AI filler. Image people follow `IMAGE-STYLE-GUIDE.md`: Chinese staff aged 22 to 27 in orange polos, green floor, blue racking, no invented logos.
- **Commit trailer:** end commit messages with the `Co-Authored-By` and `Claude-Session` lines from the current session's attribution reminder.

## Standing decisions

Recorded as Noel decided them, with dates where known.

**Prices** (`our-pricing.html`, checked 3 Oct 2026)
- Pick and pack: **$0.99 per order** for D2C. **Standard packaging (mailers, small boxes) is included** (Noel, 3 Oct 2026). Packing in the customer's own branded materials has no surcharge.
- FBA prep pick and pack: **$0.99 per carton**.
- Storage: **$0.49 per CBM per day**.
- Receiving: free. Standard visual inspection: free.
- FNSKU labelling from **$0.15/unit**. Poly bagging from **$0.30/unit**. Bubble wrap from **$0.30/unit**. Kitting and bundling from **$0.50/unit**.
- No setup fees, account fees, minimum volumes or lock-in contracts.
- Shipping is quoted per shipment.
- The D2C Consolidation cost example uses the **$0.99** rate: 600 cartons × $0.99 ≈ $594, total ~$3,200 (Noel: "0.99 is the rate").

**Free storage** (8 Oct 2026): "30 days free storage for new customers **when their first order or shipment leaves within those 30 days**. If nothing ships, the standard rate applies from the day the goods arrived." Offer bar wording: **"New customers: 30 days FREE storage when you ship in your first month"**. Never claim "no conditions".

**Best fit** (8 Oct 2026): "brands shipping **300+ orders a month**, and bulk cargo from **100 kg or 1 CBM** per shipment". There are no minimum volumes.

**Freight minimums** (8 Oct 2026, pending Cara's confirmation)

| Mode | Minimum |
|---|---|
| Sea LCL | 1 CBM |
| Sea FCL | one 20ft |
| Air freight | 100 kg |
| Express | 21 kg |
| Rail | 1 CBM |
| Truck | 1 pallet |

**Company facts**
- China Fulfillment International is the trading name of **PFC Express Ltd**.
- Founded 2010 in Longhua, Shenzhen, by Noel Murphy and Ouyang Ke.
- Shipping coverage is **"200+ countries"**, never 220+. The competitor quote of "220+" in `best-china-3pl-companies-2026` stays.
- Amazon SPN service provider: **current** (confirmed 8 Oct 2026).
- AAAA rating: keep the About page wording ("stick with - AAAA rating the 'highest rating'"). New content does not call it "highest".
- Contact email on the site: **support@china-fulfillment.com**.
- Delivery times: **6–10 days to the US, 5–8 days to the UK, 6–14 days to the EU**.

**Legal, tax and VAT position**
- Tax, VAT and IOSS registration, importer of record, customs bonds, FDA, MoCRA and FSVP, and dangerous-goods certification are the **seller's or manufacturer's** responsibility, not the 3PL's.
- On DDP shipments, duty is paid within the shipping price, but the importer's obligations stay with the seller.
- EU importer for distance sales: **1 July 2028** ("go with what is the most widely published").

**Scope**
- "IGNORE factory-direct sourcing."
- Strategy since Oct 2026: prioritise bulk and FBA freight (sea, air, rail, truck) and FBA prep over small parcel leads.
