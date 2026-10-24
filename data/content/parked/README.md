# Parked drafts

Finished posts taken off the site, kept here so nothing is lost. This folder is **outside** the build glob (`data/content/drafts/*.md`), so `scripts/build_blog.py` ignores it.

| Draft | Parked | Why |
|---|---|---|
| `sea-freight-to-amazon-fba-from-china-2026.md` | 24 Oct 2026 | Bulk FBA freight, not the blog's D2C audience |
| `lcl-vs-fcl-from-china-2026.md` | 24 Oct 2026 | Bulk freight, not the blog's D2C audience |
| `shipping-china-to-europe-sea-rail-truck-air-2026.md` | 24 Oct 2026 | Bulk freight, not the blog's D2C audience |

Noel, 24 October 2026: "remember this is china fulfillment focused content - we are looking for b2c ecom sellers or crowdfunning platform sellers wheo want to ship d2c from china".

These three were written for the October bulk-freight push and published to the dev site only, never to production. Their figures are dated 24 October 2026 and need refreshing before any reuse. They may suit the PFC Express site or the freight landing pages.

**To restore one:** move it back to `data/content/drafts/`, refresh the dated figures, run `python3 scripts/build_blog.py`, and add its `sitemap.xml` and `llms.txt` entries. Its images are still in `images/blog/`.
