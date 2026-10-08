# Image Briefs: Tier 11 / Bulk freight pages

**Three images for the new freight landing pages.**

> **Status: complete.** All three were generated, cropped to 1200×670 and installed on 8 October 2026, each with 400w and 720w copies, and they are now the `og:image` for their pages. Image 1 came back as a box truck at the warehouse door rather than a 40ft container, so it was installed as `fba-freight-pallet-loading-shenzhen-dock.webp`, a name that matches what it shows. The port aerial stays on the FBA page as the second image.

> **Read `IMAGE-STYLE-GUIDE.md` first. It overrides anything here.**

## Why these three

The three new pages went live in the repo on 8 October 2026 with stand-in images:

| Page | Stand-in now | Problem |
|---|---|---|
| `fba-freight-from-china.html` | `china-to-amazon-fba-container-shipping-sea-freight` (port aerial) | Fine, but no people. A loading shot at our own dock proves we do the work |
| `china-europe-rail-freight.html` | `fba-prep-carton-label-pallet-building-dispatch` | No train anywhere on a rail page |
| `china-europe-truck-freight.html` | `fba-prep-carton-label-pallet-building-dispatch` | No truck anywhere on a road freight page |

> **Check for real photos first.** If the team has a photo of a container being loaded at our dock, or a truck at the warehouse for a Europe road shipment, use it instead of image 1 or 3. A real photo beats a generated one every time.

## Conventions

| | |
|---|---|
| **Generate** | 16:9 at 2K |
| **Deliver** | **exactly 1200×670**, `.webp`, sRGB |
| **Upload to** | `images/site/`, with the filenames below |
| **After upload** | I make the 400w and 720w copies and swap them into the pages, the `og:image` tags and `sitemap.xml` |

The images sit in a full-width figure and as the social share card, so the subject must read clearly at thumbnail size. Keep it in the middle horizontal band.

Append the global negative prompt from `IMAGE-STYLE-GUIDE.md` §8 to every generation.

---

## 1. `fba-freight-container-loading-shenzhen-dock.webp`

**Page:** FBA freight from China

**Alt:** "Two warehouse staff in orange polo shirts loading shrink-wrapped pallets of Amazon-bound cartons into a 40ft container at the Shenzhen warehouse dock"

```
SCENE: The loading dock of a fulfilment warehouse in Shenzhen. Green epoxy resin floor with yellow demarcation lines inside, white painted walls, a raised roller-shutter door open onto the yard. The open rear doors of a plain grey 40ft shipping container are backed up to the dock.

SUBJECT: Two Chinese warehouse staff in their mid twenties, one man and one woman, both in orange polo shirts with a small logo on the left breast. The man steers a hand pallet truck carrying a shrink-wrapped pallet of kraft cartons into the container. The woman stands beside the doors holding a clipboard, checking the pallet against a list.

DETAILS: Three more shrink-wrapped pallets of kraft cartons wait on the dock floor. Each carton has a plain white shipping label, no readable text.

STYLE: Documentary workplace photography, 35mm, eye level, from about five metres back inside the warehouse looking out to the container. Natural and unposed. Bright overcast daylight outside, even fluorescent light inside.

COMPOSITION: Both people in the middle horizontal band, the container doors centred.

EXCLUDE: no readable text or labels, no carrier or shipping-line logos on the container, no Amazon logos, no hard hats, no hi-vis vests, no forklifts, no Western workers, no stock-photo smiling at camera.
```

---

## 2. `china-europe-rail-freight-container-train.webp`

**Page:** China–Europe rail freight

**Alt:** "A long container freight train crossing open steppe at golden hour on the rail route from China to Europe"

```
SCENE: Open, flat Central Asian steppe at golden hour. Dry grassland, a low line of distant hills, a wide pale sky with a few high clouds.

SUBJECT: A long freight train of 40ft shipping containers on flat wagons, travelling left to right along a single straight track, pulled by a plain modern diesel locomotive. The train stretches across most of the frame.

DETAILS: The containers are a mix of plain colours, mostly grey, blue and rust red, with no logos. Warm low sunlight catches the sides of the containers.

STYLE: Documentary landscape photography, 85mm, from a slight rise about 200 metres from the track, so the whole train reads as one clean line. Natural colour, no heavy grading.

COMPOSITION: The train sits in the middle horizontal band, entering from the left third. Plenty of sky above, grassland below, both safe to crop.

EXCLUDE: no people, no readable text, no logos or carrier names on containers or locomotive, no national flags, no railway signage, no stations, no lens flare, no motion blur on the train.
```

---

## 3. `china-europe-road-freight-truck-loading.webp`

**Page:** Truck freight to Europe

**Alt:** "Warehouse staff in orange polo shirts loading pallets of cartons onto a curtain-sided articulated truck at the Shenzhen warehouse for road freight to Europe"

```
SCENE: The yard and loading dock of a fulfilment warehouse in Shenzhen in the early morning. A white curtain-sided articulated truck is reversed up to the dock, its side curtain pulled back to show the empty trailer bed.

SUBJECT: Two Chinese warehouse staff in their mid twenties, one man and one woman, in orange polo shirts with a small logo on the left breast. The man lifts a shrink-wrapped pallet of kraft cartons into the trailer with a hand pallet truck. The woman fastens a cargo strap over pallets already loaded.

DETAILS: Two pallets already secured in the trailer. A third waits on the dock edge.

STYLE: Documentary workplace photography, 35mm, eye level, from about six metres to the side of the trailer. Soft early-morning daylight. Natural and unposed.

COMPOSITION: Both people and the open trailer in the middle horizontal band. The truck cab can be partly out of frame on the right.

EXCLUDE: no readable text, no number plates with readable characters, no logos or company names on the truck or curtain, no hard hats, no hi-vis vests, no forklifts, no Western workers, no stock-photo smiling at camera.
```

---

## Status

- [x] 1. FBA freight loading at the dock, installed as `fba-freight-pallet-loading-shenzhen-dock.webp` (box truck, not a container)
- [x] 2. China–Europe container train, installed as `china-europe-rail-freight-container-train.webp`
- [x] 3. Road freight truck loading, installed as `china-europe-road-freight-truck-loading.webp`
