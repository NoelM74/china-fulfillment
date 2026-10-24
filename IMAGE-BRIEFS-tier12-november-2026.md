# Image record: Tier 12 / November 2026 posts

**Eight images for the four November posts. No AI-generated images in this batch.**

> **Status: complete.** Installed 24 October 2026. Heroes are free stock photographs from Pexels; infographics are rendered from HTML using real data, with no image generator involved. All eight are live on the dev site.

> **Read `IMAGE-STYLE-GUIDE.md` first.** Where this file and the guide disagree, the guide wins.

## Order of preference used

Noel's instruction for this round (24 October 2026): **real photos from our files first, then free stock (Pexels and similar), and AI-generated images only as a last resort.**

1. **Our own photos.** Checked `images/site/` first. The genuine company photographs are the office team, the warehouse team, Noel with the PFC van, the PFC delivery van and the blue PFC truck. None shows a container, port, train or a customer's desk, and all are already used on service pages, so none fitted these four heroes.
2. **Free stock.** Pexels, licence checked for each photo. Unsplash and Pixabay were not reachable from the build environment; Wikimedia Commons photos are mostly CC BY-SA, which needs attribution and share-alike, so Pexels was used.
3. **AI.** Not needed.

Photos with **readable carrier or shipping-line logos** (COSCO, Maersk, Evergreen, Hapag-Lloyd, Yang Ming, SeaCo) were rejected, in line with §8 of the style guide.

## Heroes (2070×760, plus -760w, -1140w and -1520w copies)

| File in `images/blog/` | Post | Source | Photographer | Size |
|---|---|---|---|---|
| `sea-freight-to-amazon-fba-from-china-2026.webp` | Sea freight to Amazon FBA | [Pexels 1554646](https://www.pexels.com/photo/aerial-view-of-cargo-ship-1554646/), "Aerial View of Cargo Ship", Jakarta | Tom Fisk | 219 KB |
| `lcl-vs-fcl-from-china-2026.webp` | LCL vs FCL | [Pexels 28438334](https://www.pexels.com/photo/container-terminal-with-straddle-carriers-28438334/), "Container Terminal with Straddle Carriers" | Simon R. Minshall | 159 KB |
| `shipping-china-to-europe-sea-rail-truck-air-2026.webp` | China to Europe | [Pexels 14776383](https://www.pexels.com/photo/cargo-wagons-on-station-14776383/), "Cargo Wagons on Station" | Quang Nguyen Vinh | 196 KB |
| `ieepa-tariff-refunds-china-sellers-2026.webp` | IEEPA refunds | [Pexels 5900074](https://www.pexels.com/photo/woman-sitting-behind-the-desk-and-looking-at-receipts-5900074/), "Woman Sitting Behind the Desk and Looking at Receipts" | Karolina Grabowska (Kaboompics) | 69 KB |

**Licence.** All four are under the [Pexels licence](https://www.pexels.com/license/): free for commercial use, attribution not required, modification allowed. Not allowed: selling unaltered copies, implying the people or brands shown endorse us, or showing identifiable people in a bad light. None of these photos shows an identifiable face.

**Processing.** Centre crop of the original to 2070×760 (the middle band, as §6 of the style guide requires), WebP at quality 76 with light denoising. The three detailed photos are 159–219 KB, within the range of existing heroes (median 98 KB, largest 277 KB); visitors are served the 760–1520 copies through `srcset`, 35–146 KB.

**Notes.**
- The China–Europe photo shows a **CRCT (China Railway Container Transport) container on an X70 container flat wagon**. The markings are in-world, real-world railway markings on a documentary photo, not an overlay, and they are why the alt text can say it is a Chinese railway container. The photo's location is not stated, so the alt text does not name one.
- The refund post shows a **customer at their own desk**, which §2 of the style guide allows: the action in that article happens at the seller's desk, not in our warehouse.
- The sea freight photo is of Jakarta, not Shenzhen. The alt text describes a container terminal without naming the port.

## Infographics (1200×1500, plus -600w and -900w copies)

Rendered from HTML in the site font (Outfit) and brand navy and orange, flat on white, per §6. Source: `scripts/infographics/2026-11/` (`make_infographics.py` holds the wording and figures; `build.sh` rebuilds all four into `images/blog/`). **Edit the script, not the images.**

| File | Figures and their sources |
|---|---|
| `infographic-sea-freight-fba-timeline.webp` | ISF 24 hours before loading (CBP); 15–25 days port to port and about 25–35 days to an Amazon warehouse (our FBA freight page); CNY 6 February 2027 |
| `infographic-lcl-vs-fcl-break-even.webp` | Container volumes ~33 / ~68 / ~76 m³ (representative carrier figures); 12–18 CBM typical 20ft crossover (forwarder guidance); break-even formula |
| `infographic-china-europe-four-modes.webp` | Sea $3,632/40ft (Drewry WCI, 22 Oct 2026); rail ~$10,000/40ft (Index1520, Aug 2026); air $4.80/kg (TAC Index, Sep 2026); transit times as in the article |
| `infographic-ieepa-refund-who-gets-paid.webp` | CBP pays CAPE refunds by ACH to the importer of record; Section 122 and 301 not covered |

**When a figure changes** (for example the monthly rate refresh), update `make_infographics.py` and the matching article together, then run `bash scripts/infographics/2026-11/build.sh`.

## Shot list: real photos to replace the stock heroes

Real photographs of our own operation beat stock every time (§6). If the team can shoot these at the Shenzhen dock, save them over the same filenames at 2070×760 (keep the subject in the middle band) and no HTML needs to change. Update the alt text in the draft frontmatter, then rebuild.

1. **Sea freight to Amazon FBA.** Two staff in orange polos loading shrink-wrapped pallets of FNSKU-labelled kraft cartons into a 20ft or 40ft container at our dock. Suggested alt: *"Warehouse staff in orange polo shirts loading pallets of Amazon-labelled cartons into a shipping container at the Shenzhen warehouse dock"*.
2. **LCL vs FCL.** A handful of wrapped pallets for different customers, labelled and staged by the door for the consolidation warehouse, next to a part-loaded container. Suggested alt: *"Pallets for several customers staged at the Shenzhen dock beside a part-loaded container, ready for shared and full container shipments"*.
3. **China to Europe.** Pallets labelled for Amazon EU being loaded onto a truck bound for the rail terminal. Suggested alt: *"Staff loading pallets labelled for Amazon Europe onto a truck at the Shenzhen warehouse for the China–Europe rail service"*.
4. **IEEPA refunds.** Keep the stock photo. It shows the customer's side of the task, which our staff should not appear in.

Same people rules as always: Chinese staff aged 22 to 27, both men and women, orange polos with the small chest logo, no hard hats or hi-vis.
