# Image Briefs — Tier 6 / Content-Gap Posts (5 new posts, filling the audit gaps)

**Ten images: 5 heroes + 5 infographics.** These prompts are written for **GPT Image 2**, which responds better to descriptive natural-language scene direction than to keyword lists, and which renders in-image text reliably. That changes two things versus Tier 1–5:

- **Heroes** get full scene direction: subject, camera position, lens feel, lighting, palette, mood, and an explicit negative list. Still **no on-image text** and no real trademarks.
- **Infographics** now specify **exact text strings in quotes**. Set them verbatim. GPT Image 2 will render them accurately if you do not overload the canvas, so each layout is capped at a handful of short lines.

## Conventions (unchanged from Tier 1–5)

| | |
|---|---|
| **Format** | `.webp`, sRGB |
| **Hero size** | displayed 1200×440; generate at 2×, **2400×880**, target under ~150 KB |
| **Infographic size** | **1200×1500** (4:5 portrait, single column, phone-legible) |
| **Palette** | brand navy `#0F1E3D`, brand orange `#F26B21`, warm neutral greys, white |
| **Hero style** | photographic realism, documentary logistics, natural light |
| **Infographic style** | flat vector, generous whitespace, no gradients, no 3D, no drop shadows |
| **Alt text** | already baked into the drafts, repeated below so you can check the render matches |
| **Upload to** | `images/blog/` on branch `claude/blog-serp-keyword-analysis-j26pym`, exact lowercase filenames |

**All 5 posts are staged `noindex`, are out of `sitemap.xml`, and have no blog card.** Generating these images completes them. Nothing goes live until you say so.

**Global negative prompt** (append to every generation): *no readable brand logos, no courier or marketplace trademarks, no national flags rendered as logos, no watermarks, no stock-photo lens flare, no distorted hands, no gibberish text, no signage in Chinese or English other than the text specified.*

---

## 1. How to Choose a China 3PL — `how-to-choose-a-china-3pl`

### Hero — `/images/blog/how-to-choose-a-china-3pl.webp`

**Alt:** "A seller comparing China fulfilment providers against a Shenzhen warehouse operation, weighing pricing, integrations and quality control before signing"

**Prompt:**
> A photorealistic wide banner image, shot as if on a 35mm lens at eye level from about three metres back. In the foreground, slightly left of centre and softly out of focus, a pair of hands rests over an open notebook and a tablet on a clean grey desk, mid-comparison, one finger paused against a line on the page. The desk edge runs along the bottom third. Behind it, in sharp focus and filling the upper two thirds, is a working fulfilment warehouse seen through a wide interior opening: neat steel shelving racks receding into depth, plain unmarked brown cartons stacked with military tidiness, a packing bench with a barcode scanner resting on it, one warehouse worker in a plain navy polo shirt at the far bench, small in frame and turned away. Light is cool industrial daylight from high clerestory windows, falling in soft diagonal shafts, with a warm amber pool of light over the desk in the foreground to separate the two planes. Colour grade toward deep navy shadows and warm neutral greys, with a single restrained orange accent appearing naturally on a safety line painted across the warehouse floor. Calm, considered, professional mood. The composition must keep its subject centred and readable when cropped to a narrow mobile strip. 2400×880 pixels, approximately 27:10 ultra-wide. No on-image text of any kind.

### Infographic — `/images/blog/infographic-china-3pl-evaluation-checklist.webp` *(embedded in body)*

**Alt:** "How to compare China 3PLs: ask for the complete rate card in writing, ask what happens when an order goes wrong and who pays, check native integrations and live inventory visibility, test marketplace prep knowledge, and confirm which customs and compliance duties stay with you"

**Prompt:**
> A clean flat-vector infographic on a pure white background, single column, designed to be legible on a phone screen. At the top, a deep navy header bar with the title in bold white sans-serif: **"5 questions before you sign"**. Below it, five evenly spaced rows stacked vertically, each row a rounded-corner white card with a thin light-grey border, a large orange numeral on the left, a simple two-colour line icon beside it, and short navy text. The five rows read exactly: **"1. Show me the whole rate card, in writing"**, **"2. What happens when it goes wrong, and who pays?"**, **"3. How does it connect to my store?"**, **"4. Describe my marketplace's prep spec"**, **"5. Which parts will you not handle?"**. Icons in order: a document with line items, a warning triangle, two interlocking plugs, a barcode label, a dotted boundary line. At the bottom, a full-width orange band with bold white text reading **"Then run a 1-3 SKU pilot"**. Modern geometric sans-serif throughout, generous whitespace, no gradients, no drop shadows, no 3D. 1200×1500 pixels, 4:5 portrait.

---

## 2. Incoterms — `incoterms-china-imports-exw-fob-cif-ddp`

### Hero — `/images/blog/incoterms-china-imports-exw-fob-cif-ddp.webp`

**Alt:** "The handover points for EXW, FOB, CIF and DDP mapped across a China export journey from factory gate to port to the buyer's door"

**Prompt:**
> A photorealistic wide banner image of a Chinese container port at the blue hour just after sunset, shot from an elevated position roughly two hundred metres back with a long lens that compresses the layers. Read the frame left to right as a journey: at the far left, a factory loading bay with its roller door open and warm interior light spilling onto a waiting flatbed truck; in the centre, stacked shipping containers in muted navy, rust red and slate grey, with two gantry cranes rising above them, one crane arm lowered mid-lift; at the right, a container vessel at berth, its deck lights on, bow pointing out of frame. The sky is a deep gradient from navy overhead to a thin band of warm orange at the horizon, reflected on wet quayside concrete. Everything is real and grounded, no diagrams or overlays. Cinematic, quiet, industrial-epic mood. Deep navy shadows, warm orange highlights only from artificial light sources. Keep the central crane and containers as the visual anchor so the image survives a narrow mobile crop. 2400×880 pixels, approximately 27:10 ultra-wide. No on-image text, no readable shipping-line names or container markings.

### Infographic — `/images/blog/infographic-incoterms-handover-points.webp` *(embedded in body)*

**Alt:** "Incoterms for China imports: EXW hands over at the factory gate, FOB hands over loaded on the vessel with export cleared, CIF adds freight and minimum insurance to the destination port with risk still passing at origin, and DDP delivers to your door with duty paid"

**Prompt:**
> A clean flat-vector infographic on a pure white background, portrait orientation, built as a single vertical journey line. A thick vertical spine runs down the centre-left of the canvas, coloured deep navy at the top and transitioning to orange at the bottom. Four large circular nodes sit on that spine, evenly spaced, each numbered and paired with a simple two-colour line icon to its left and a text block to its right. Reading top to bottom, the icons are: a factory building, a ship with a crate being loaded, a ship at sea with a small shield symbol, and a house with a parcel on the step. The four text blocks read exactly, with the bold term on the first line and the plain description beneath: **"EXW — you take over at the factory gate"**, **"FOB — supplier loads the vessel, export cleared"**, **"CIF — freight and minimum insurance paid, risk still passes at origin"**, **"DDP — delivered to your door, duty paid"**. At the very bottom, below the spine, a slim navy footer bar with white text reading **"Incoterms 2020 · sets cost and risk, not who is importer of record"**. Bold geometric sans-serif for the terms, lighter weight for descriptions, generous whitespace, no gradients other than the spine, no shadows, no 3D. 1200×1500 pixels, 4:5 portrait.

---

## 3. DIM Weight & Packaging — `dim-weight-packaging-optimisation-2026`

### Hero — `/images/blog/dim-weight-packaging-optimisation-2026.webp`

**Alt:** "Right-sizing a parcel at the packing bench so billable dimensional weight drops, after the July 2026 USPS divisor change from 166 to 139"

**Prompt:**
> A photorealistic wide banner image shot straight on at bench height with a 50mm lens and a shallow depth of field. The centre of the frame is a packing bench in a bright warehouse. Side by side, deliberately compared, sit two versions of the same shipment: on the left an oversized plain brown carton with a small product sitting lost inside it surrounded by obvious empty air and a few crumpled paper voids, its flaps open; on the right the identical product snugly enclosed in a compact right-sized carton and a flat kraft poly mailer, both closed and neat. A steel tape measure lies extended across the bench between them. Behind, softly blurred, a roll of kraft paper, a stack of flat-packed cartons and a floor scale. Lighting is clean, bright, even daylight from a large window to camera left, with soft shadows and no glare, giving an honest documentary product-operations feel rather than a styled advertisement. Palette of warm kraft brown, cool white, neutral grey, with one small orange accent on the tape measure casing. Keep both cartons within the central third so the comparison survives a narrow mobile crop. 2400×880 pixels, approximately 27:10 ultra-wide. No on-image text, no printed labels, no brand marks on the boxes.

### Infographic — `/images/blog/infographic-dim-weight-2026.webp` *(embedded in body)*

**Alt:** "Dimensional weight after the July 2026 USPS change: divide length by width by height by the divisor, USPS moved from 166 to 139 on 12 July 2026 and now rounds fractional inches up, dimensional pricing applies above one cubic foot, and the fix is right-sizing at the packing bench"

**Prompt:**
> A clean flat-vector infographic on a pure white background, portrait orientation, four stacked sections separated by thin light-grey rules. Section one: a deep navy panel containing a large centred formula in white monospace type reading exactly **"L × W × H ÷ divisor = DIM weight"**, with a smaller white line beneath reading **"you pay the greater of DIM or actual weight"**. Section two: a bold before-and-after comparison, two large numerals side by side, the left in muted grey reading **"166"** with a small grey label **"USPS before"**, an orange arrow pointing right between them, the right in large bold orange reading **"139"** with a navy label **"USPS from 12 Jul 2026"**. Section three: two short navy bullet lines each with a small orange square marker, reading exactly **"Fractional inches now round UP"** and **"Applies above 1 cubic foot (1,728 in³)"**. Section four: a full-width orange footer band with bold white text reading **"The fix is a smaller box, chosen at the packing bench"**. Modern geometric sans-serif, very large type sizes so every figure is readable at phone width, generous whitespace, no gradients, no shadows, no 3D. 1200×1500 pixels, 4:5 portrait.

---

## 4. Product Compliance — `product-compliance-importing-from-china-2026`

### Hero — `/images/blog/product-compliance-importing-from-china-2026.webp`

**Alt:** "Compliance documents and test reports checked alongside China-made goods before export, covering CPC, FCC, CE and UKCA requirements in 2026"

**Prompt:**
> A photorealistic wide banner image shot from a high three-quarter angle looking down onto a clean light-grey inspection table, as if standing over it. Laid out across the surface with deliberate order: a small stack of printed test-report documents with visible printed paragraphs and a table of results but no legible words, held by a black bulldog clip; a pair of white cotton inspection gloves; a digital calliper resting beside a small unbranded consumer electronic device with its back cover off; a plain white product box with a blank rectangular label area; and at the right edge, partially in frame, the corner of a sealed brown carton. Lighting is bright, cool, even and clinical from directly above, the light of a laboratory bench rather than a warehouse, with crisp short shadows. Palette of white, cool grey and pale blue, with a single navy folder and one small orange tab marking a page in the document stack. Precise, careful, quietly serious mood. Keep the document stack and the device centred for mobile cropping. 2400×880 pixels, approximately 27:10 ultra-wide. No legible text anywhere in the image, no certification marks, no logos.

### Infographic — `/images/blog/infographic-compliance-by-market.webp` *(embedded in body)*

**Alt:** "Product compliance by market for China-made goods in 2026: US children's products need a CPC from CPSC-accepted third-party lab testing with mandatory eFiling from 8 July 2026, wireless electronics need FCC Certification and non-wireless usually SDoC, the EU needs CE marking and a declaration of conformity, and Great Britain recognises CE indefinitely with UKCA required only for excluded categories"

**Prompt:**
> A clean flat-vector infographic on a pure white background, portrait orientation, structured as three stacked market cards plus a footer. Each card is a rounded-corner white panel with a thin grey border, a deep navy header strip across its top containing the market name in bold white, and two or three short navy text lines beneath with small orange square bullet markers. Card one header reads **"UNITED STATES"**, with lines reading exactly **"Kids' products: CPC, from CPSC-accepted lab testing"**, **"Wireless: FCC Certification · non-wireless: SDoC"**, and **"eFiling mandatory from 8 Jul 2026"**. Card two header reads **"EUROPEAN UNION"**, with lines reading exactly **"CE marking + EU Declaration of Conformity"** and **"US testing does not transfer to the EU"**. Card three header reads **"GREAT BRITAIN"**, with lines reading exactly **"CE recognised indefinitely for most goods"** and **"UKCA only for excluded categories"**. Below all three, a full-width orange footer band with bold white text reading **"Labs test. You certify. Your 3PL does neither."**. Use a simple two-colour line icon in the corner of each card: a shield for the US, a circle of stars motif abstracted as plain dots for the EU, and a plain rounded square for GB. Modern geometric sans-serif, generous whitespace, no gradients, no shadows, no 3D, no official certification marks reproduced. 1200×1500 pixels, 4:5 portrait.

---

## 5. China to Japan — `china-to-japan-fulfillment-2026`

### Hero — `/images/blog/china-to-japan-fulfillment-2026.webp`

**Alt:** "Parcels dispatched from a Shenzhen warehouse to Japanese customers on short sea and air lanes as the consumption tax treatment of low-value imports changes"

**Prompt:**
> A photorealistic wide banner image of a coastal container terminal at dawn, shot from a slightly elevated position on the quay with a wide lens. In the near foreground at bottom left, a neat pallet of plain small parcels wrapped in clear stretch film, sharply focused, catching the first warm light. The middle distance holds a short row of containers and a low terminal building. The far distance is a calm sea with a container feeder vessel, small in frame and already under way, heading right toward a horizon where soft blue mountains rise, deliberately suggesting a short crossing rather than an ocean voyage. A thin band of pale gold sits on the water. Mist softens the middle ground. Light is early, cool and clean, with long low shadows. Palette of pale blue, soft grey, white and a warm gold horizon, with one restrained orange accent on a quayside bollard. Serene, efficient, early-morning mood, the visual argument being proximity and speed. Keep the parcel pallet and the vessel roughly on the horizontal centre line for mobile cropping. 2400×880 pixels, approximately 27:10 ultra-wide. No on-image text, no flags, no readable shipping-line markings.

### Infographic — `/images/blog/infographic-japan-jct-2026.webp` *(embedded in body)*

**Alt:** "Fulfilling Japan from China in 2026: the 10,000 yen consumption tax exemption is being withdrawn, JCT is charged on CIF value plus duty at 10 percent, liability moves to the overseas seller or to platform operators above a 5 billion yen annual threshold, and transit runs one to three days by air or three to seven days by sea"

**Prompt:**
> A clean flat-vector infographic on a pure white background, portrait orientation, three stacked sections plus a footer. Section one, headed by a navy bar with white bold text reading **"What's changing"**: a large struck-through grey figure reading **"¥10,000"** with a small grey caption **"tax-free threshold"**, and beside it a bold orange **"10%"** with a navy caption **"consumption tax on low-value imports"**. Section two, headed by a navy bar reading **"How it's calculated"**: a centred formula in navy monospace reading exactly **"(CIF + duty) × 10% = import JCT"**, with a smaller navy line beneath reading **"CIF includes freight, so shipping is taxed"**. Section three, headed by a navy bar reading **"Transit from China"**: two side-by-side stat blocks, the left with a simple aeroplane line icon and bold navy text **"Air: 1-3 days"**, the right with a simple ship line icon and bold navy text **"Sea: 3-7 days"**. Full-width orange footer band with bold white text reading **"Liability moves to the seller, or the platform above ¥5bn"**. Modern geometric sans-serif, very large figures, generous whitespace, no gradients, no shadows, no 3D, no flags. 1200×1500 pixels, 4:5 portrait.

---

## Generation notes for GPT Image 2

1. **Generate heroes and infographics in separate batches.** The two styles pull the model in different directions and mixing them in one session degrades both.
2. **For infographics, paste the prompt verbatim including the bold text strings.** If a line renders with a typo, regenerate that single image rather than editing the prompt; GPT Image 2 is inconsistent per-seed rather than systematically wrong.
3. **Keep the text budget low.** These layouts are already near the limit at which in-image text stays clean. Do not add lines.
4. **Check every rendered figure against the alt text below the prompt** before converting to WebP. The numbers (`139`, `166`, `1,728`, `8 Jul 2026`, `¥10,000`, `¥5bn`, `10%`) are load-bearing, and a hallucinated digit in an image is harder to spot later than one in copy.
5. **Convert to WebP after approval**, quality 82 for heroes and 90 for infographics, then confirm heroes land under roughly 150 KB.
6. **Filenames are exact and lowercase.** The drafts and the built HTML already reference them.
