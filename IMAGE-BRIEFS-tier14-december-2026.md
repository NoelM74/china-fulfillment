# Image record: Tier 14 / posts of 26 November 2026

**Images for the January 2027 US import changes post and the Valentine's Day 2027 post, plus a corrected Christmas infographic. No AI-generated images in this batch.**

> **Status: complete.** Installed 26 November 2026. Heroes are free stock photographs from Pexels; infographics are rendered from HTML. All live on the dev site.

> **Read `IMAGE-STYLE-GUIDE.md` first.** Where this file and the guide disagree, the guide wins.

## Rules applied

**Order of preference** (Noel, 24 October 2026): "Use real photos from file or from free image services like pexels and other before using ai generated content." Our own photos do not show a gift box or a calendar.

**Logos and people.** Neither hero shows a logo or a person.

## Heroes (2070×760, plus -760w, -1140w and -1520w copies)

| File in `images/blog/` | Post | Source | Photographer |
|---|---|---|---|
| `us-import-changes-january-2027-china-sellers.webp` | US import changes in January 2027 | [Pexels 6408282](https://www.pexels.com/photo/clipboard-with-calendar-placed-on-desk-amidst-stationery-6408282/), "Clipboard with calendar placed on desk amidst stationery" | Marko Klaric |
| `valentines-day-2027-shipping-deadlines-from-china.webp` | Valentine's Day 2027 shipping deadlines | [Pexels 4397835](https://www.pexels.com/photo/red-gift-box-with-red-ribbon-on-a-white-surface-4397835/), "Red Gift Box With Red Ribbon on a White Surface" | Kaboompics (Pexels profile @karola-g) |

**Licence.** Both pages show the Pexels "Free" licence, checked 26 November 2026: free for commercial use, attribution not required, modification allowed. See the [Pexels licence](https://www.pexels.com/license/).

**Processing.** Cropped to 2070×760 (the calendar from the top, to keep "January" in frame; the gift box shifted up to keep the lid), light denoise, WebP at quality 78.

## Infographics (1200×1500, plus -600w and -900w copies)

Rendered from HTML in the site font (Outfit), navy and orange on white. Source: `scripts/infographics/2026-11/make_infographics.py`; `bash scripts/infographics/2026-11/build.sh` rebuilds them. **Edit the script, not the images.**

| File | Figures and their sources |
|---|---|
| `infographic-valentines-2027-dispatch-dates.webp` (item 10, new) | Dispatch dates counted back from Fri 12 February 2027 from our standard delivery times (US 6–10, UK 5–8, EU 6–14 days; Canada 9–12 and Australia 8–12 days, Noel, 26 November 2026); express 2–5 business days; warehouse closed 6–14 February (Noel, 26 November 2026) |
| `infographic-christmas-2026-dispatch-dates.webp` (item 5, corrected) | Canada and Australia delivery times changed to 9–12 and 8–12 days; cut-off dates unchanged |

**Renderer note.** `render.mjs` now defaults to `/opt/pw-browsers/chromium`, the path that stays valid when the environment's Chromium is updated.
