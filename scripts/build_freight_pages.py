"""Build the three bulk-freight landing pages from the our-pricing.html template.

Run from anywhere: python3 scripts/build_freight_pages.py
Writes fba-freight-from-china.html, china-europe-rail-freight.html and
china-europe-truck-freight.html into the repo root.

The template sections are found by marker, so edits to our-pricing.html
(menus, footer, offer bar) flow through on the next run. To refresh the
monthly market rates, edit RATES_DATE and the figures in the page bodies,
then run this script."""
import json, html, re, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.china-fulfillment.com/"
T = open(os.path.join(REPO, "our-pricing.html"), encoding="utf-8").read().split("\n")

SRC = "\n".join(T)
def between(a, b):
    i = SRC.index(a); j = SRC.index(b, i)
    return SRC[i:j].rstrip("\n")

# Template sections found by marker, so edits to the template never shift them.
HEAD_START = SRC[:SRC.index("<title>")].rstrip("\n")
SHARED_HEAD = between('<link rel="preconnect" href="https://fonts.googleapis.com"/>', "</head>")
NAV = SRC[SRC.index("<body>") + len("<body>"):SRC.index("<!-- ═══ HERO ═══ -->")].strip("\n")
FOOTER = SRC[SRC.index("<footer>"):]

EXTRA_CSS = """<style>/* freight pages */
.hero .sl{margin-bottom:12px}
.rate-note{font-size:.88rem;color:var(--mu);line-height:1.6;margin-top:12px}
.ptbl td.src{font-size:.82rem;color:var(--mu);white-space:normal}
.callout{background:#fff7ed;border:1px solid #fed7aa;border-left:4px solid #c25205;border-radius:10px;padding:16px 18px;margin-top:22px;color:#334155;font-size:.95rem;line-height:1.65}
.callout strong{color:var(--ink)}
.fig{margin:26px 0 0}
.fig img{border-radius:12px;border:1px solid var(--bd);width:100%;height:auto}
.fig figcaption{font-size:.86rem;color:var(--mu);margin-top:8px}
.steps{list-style:none;counter-reset:s;display:grid;gap:12px;margin-top:22px;padding:0}
.steps li{counter-increment:s;display:grid;grid-template-columns:38px minmax(0,1fr);gap:14px;background:var(--w);border:1px solid var(--bd);border-radius:12px;padding:16px 18px}
.steps li::before{content:counter(s);font-family:'Outfit',sans-serif;font-weight:900;color:#fff;background:#0d2144;border-radius:9px;width:38px;height:38px;display:flex;align-items:center;justify-content:center}
.steps h3{font-size:1rem;font-weight:800;margin-bottom:4px}
.steps p{font-size:.93rem;color:#334155;line-height:1.6}
.xlinks{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:22px}
.xlinks a{display:block;background:var(--w);border:1px solid var(--bd);border-radius:12px;padding:16px 18px;font-family:'Outfit',sans-serif;font-weight:800;color:var(--ink)}
.xlinks a span{display:block;font-family:'Mulish',sans-serif;font-weight:400;font-size:.88rem;color:var(--mu);margin-top:4px}
.xlinks a:hover{border-color:#c25205}
.prsec ul.plain{padding-left:18px;color:#334155;display:flex;flex-direction:column;gap:8px;margin-top:14px;font-size:.96rem;line-height:1.6}
.prsec ul.plain a{color:#1d4ed8;text-decoration:underline;text-underline-offset:2px}
.pcard .amt{white-space:nowrap}
@media(max-width:600px){.pcard .amt{font-size:1.5rem}}
@media(max-width:960px){.xlinks{grid-template-columns:1fr}}
</style>"""

PROVIDER = {"@type": "Organization", "name": "China Fulfillment International", "legalName": "PFC Express Ltd",
            "url": BASE, "foundingDate": "2010",
            "address": {"@type": "PostalAddress", "streetAddress": "3rd Floor, Building D, Minle Industrial Park, Meiban Road, Longhua",
                        "addressLocality": "Shenzhen", "addressRegion": "Guangdong", "addressCountry": "CN"}}

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def build(p):
    url = BASE + p["slug"] + ".html"
    ld = [
        {"@context": "https://schema.org", "@type": "WebPage", "url": url, "name": strip_tags(p["h1"]),
         "description": p["desc"], "dateModified": p["modified"], "inLanguage": "en",
         "isPartOf": {"@type": "WebSite", "name": "China Fulfillment International", "url": BASE}},
        {"@context": "https://schema.org", "@type": "Service", "name": p["service_name"], "serviceType": p["service_type"],
         "areaServed": p["area"], "provider": PROVIDER, "url": url},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": html.unescape(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in p["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]},
    ]
    img = BASE + "images/site/" + p["og_image"] + ".webp"
    t = html.escape(p["title"], quote=True)
    d = html.escape(p["desc"], quote=True)
    head = f"""<title>{t}</title>
<meta name="description" content="{d}"/>
<link rel="canonical" href="{url}"/>
<link rel="alternate" hreflang="en" href="{url}"/>
<link rel="alternate" hreflang="x-default" href="{url}"/>
<meta name="author" content="China Fulfillment International, Shenzhen 3PL since 2010"/>
<meta property="og:title" content="{t}"/>
<meta property="og:description" content="{d}"/>
<meta property="og:type" content="website"/>
<meta property="og:image" content="{img}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="{img}"/>
<meta property="og:url" content="{url}"/>
""" + "\n".join('<script type="application/ld+json">\n' + json.dumps(x, ensure_ascii=False) + "\n</script>" for x in ld) + "\n"
    faq_html = "\n".join(f' <details><summary>{html.escape(html.unescape(q))}</summary><div class="fans">{a}</div></details>' for q, a in p["faq"])
    body = p["body"].replace("{{FAQ}}", faq_html)
    out = "\n".join([HEAD_START, head, SHARED_HEAD, EXTRA_CSS, "</head>", "<body>", "", NAV, "", body, "", FOOTER])
    open(os.path.join(REPO, p["slug"] + ".html"), "w", encoding="utf-8").write(out)
    return p["slug"] + ".html"

def figure(name, w, h, alt, cap):
    return (f'<figure class="fig"><img src="images/site/{name}.webp" srcset="images/site/{name}-400w.webp 400w, '
            f'images/site/{name}-720w.webp 720w, images/site/{name}.webp 1200w" sizes="(max-width: 1020px) 90vw, 980px" '
            f'alt="{html.escape(alt, quote=True)}" width="{w}" height="{h}" loading="lazy" decoding="async"/>'
            f'<figcaption>{cap}</figcaption></figure>')

FIT = ('<p class="fit"><strong>Best fit:</strong> bulk cargo from 100 kg or 1 CBM per shipment, and brands shipping 300+ orders a month. '
       'Smaller first shipments are welcome; we will tell you honestly which mode makes sense.</p>')

CTA = """<section class="ctaf">
 <div class="w">
 <div class="sl">Get Your Freight Quote</div>
 <h2>Send us your cartons, weights and destination.<br/><span class="hi" style="color:var(--ac)">We'll quote every mode within 24 hours.</span></h2>
 <p class="lead">Tell us the number of cartons, their size and weight, the Amazon warehouse or address, and when the goods are ready. We'll come back with the options side by side.</p>
 <p class="micro">Free receiving. Free visual inspection. 30 days free storage for new customers who start shipping within the month.</p>
 <div class="ctabtns">
 <a class="bp" href="Contact-Us.html">Get My Freight Quote &rarr;</a>
 <a class="bg" href="our-pricing.html">See Our Price List</a>
 </div>
 <div class="trow">
 <div class="tri">Est. 2010 in Shenzhen</div>
 <div class="tri">Sea, air, express, rail, truck</div>
 <div class="tri">FBA prep before it ships</div>
 <div class="tri">US, UK and EU Amazon</div>
 </div>
 </div>
</section>"""

XLINKS = """ <div class="xlinks">
 <a href="fba-freight-from-china.html">FBA freight from China<span>Sea, air and express to Amazon in the US, UK and EU.</span></a>
 <a href="china-europe-rail-freight.html">China&#8211;Europe rail freight<span>14 to 25 days by train, then on to Amazon EU.</span></a>
 <a href="china-europe-truck-freight.html">Truck freight to Europe<span>Pallets by road to Poland, Germany and beyond.</span></a>
 </div>"""

PREP_BUNDLE = """<!-- ═══ PREP + FREIGHT ═══ -->
<section class="prsec" id="prep-freight">
 <div class="w">
 <div class="sl">Prep + Freight</div>
 <h2 class="st">One quote from factory to Amazon</h2>
 <p class="lead2">Your suppliers deliver to our Shenzhen warehouse. We check, prep and pack everything to Amazon's rules, then ship it on the mode you choose. One contact, one quote, one invoice.</p>
 <div class="ptw"><table class="ptbl">
 <caption>What the bundle includes</caption>
 <thead><tr><th scope="col">Step</th><th scope="col">Price</th><th scope="col">What happens</th></tr></thead>
 <tbody>
 <tr><td>Receiving</td><td class="pr free">Free</td><td>Deliveries from any number of suppliers, counted against your purchase orders.</td></tr>
 <tr><td>Visual inspection</td><td class="pr free">Free</td><td>Every batch checked against your spec, with photos of any defect or short shipment.</td></tr>
 <tr><td>FNSKU labelling</td><td class="pr">from $0.15 / unit</td><td>Amazon barcodes applied in Shenzhen. Amazon stopped doing US prep on 1 January 2026.</td></tr>
 <tr><td>Poly bagging</td><td class="pr">from $0.30 / unit</td><td>Suffocation-warning bags where Amazon requires them.</td></tr>
 <tr><td>Carton prep and labels</td><td class="pr">$0.99 / carton</td><td>Cartons packed to Amazon's size and weight limits, with an FBA box label on every carton.</td></tr>
 <tr><td>Storage while you wait</td><td class="pr">$0.49 / CBM / day</td><td>Hold stock in Shenzhen until the sailing or restock date. First 30 days free for new customers who start shipping within the month.</td></tr>
 <tr><td>Freight and delivery to Amazon</td><td class="pr">Quoted</td><td>Priced on your cartons' real weight and volume, mode and destination.</td></tr>
 </tbody></table></div>
 <div class="callout"><strong>Example:</strong> 4,000 units in 200 cartons, each unit FNSKU-labelled and poly-bagged. Prep comes to $1,998 at our published "from" rates (200 &times; $0.99 + 4,000 &times; $0.15 + 4,000 &times; $0.30). Freight is then quoted on the cartons' measured volume and weight, so you see the full cost to Amazon before anything ships. See the <a href="our-pricing.html">full price list</a>.</div>
 </div>
</section>"""

RATES_DATE = "8 October 2026"

# ───────────────────────── Page 1: FBA freight ─────────────────────────
fba_faq = [
 ("How much does it cost to ship to Amazon FBA from China?",
  "It depends on the mode, the volume and the destination. As market references: a 40ft container from Shanghai to Los Angeles was $7,835 on Drewry's World Container Index of 1 October 2026, shared-container (LCL) space to the US West Coast was quoted at roughly $60 to $120 per CBM before port charges, and air freight from Hong Kong to North America averaged $7.02 per kg in September 2026 (TAC Index). We quote the full cost to the Amazon warehouse within 24 hours."),
 ("Should I use LCL or a full container?",
  "Shared space (LCL) is charged per cubic metre, with a 1 CBM minimum, and suits planned restocks of a few cubic metres. As a rule of thumb, once a shipment passes about 15 CBM, a 20ft container usually costs less than the same volume in LCL, and it is handled less on the way. We price both when you are close to the line."),
 ("How long does sea freight to Amazon FBA take?",
  "To the US West Coast, the voyage is typically 15 to 25 days port to port, and about 25 to 35 days to an Amazon warehouse once customs, trucking and the delivery appointment are included. The East Coast takes longer. To Europe, most sailings still go around the Cape of Good Hope, so allow 30 to 45 days or more at sea."),
 ("What are your minimum shipment sizes?",
  "Shared container (LCL): 1 CBM. Full container: one 20ft. Air freight: 100 kg chargeable weight. Express: 21 kg. Below those sizes, our parcel fulfilment service is usually the better fit."),
 ("Can you prep my goods and ship them to Amazon in one go?",
  "Yes. Suppliers deliver to our Shenzhen warehouse, we inspect, label, bag and carton everything to Amazon's rules, and the same team books the freight and the delivery to Amazon. You get one quote and one invoice."),
 ("Do you handle customs and import duty?",
  "We handle export clearance in China and arrange import clearance at destination, and we can ship DDP so the duty is paid within the shipping price. The legal duties of the importer still sit with you or the importer you appoint; Amazon will not act as your importer of record. Our <a href=\"importer-of-record-china-fulfillment-2026.html\">importer of record guide</a> explains how this works in the US, EU and UK."),
]
fba_body = f"""<!-- ═══ HERO ═══ -->
<section class="hero">
 <div class="w">
 <div class="sl">FBA Freight from China</div>
 <h1>Freight to Amazon FBA from China, <span class="hi">with the rates on the page</span></h1>
 <p>Sea, air and express from our Shenzhen warehouse to Amazon fulfilment centres in the US, UK and EU, with the prep done before it leaves. Below are this month's market rates, typical transit times and our minimums, so you can plan before you ask for a quote.</p>
 <p class="asof">Market rates checked {RATES_DATE}. They move every week; your written quote states how long it is valid.</p>
 {FIT}
 <div class="pcards">
 <div class="pcard"><span class="amt">$7,835</span><span class="per">per 40ft container</span><p>Shanghai to Los Angeles by sea. Drewry World Container Index, 1 October 2026.</p></div>
 <div class="pcard"><span class="amt">$60&#8211;120</span><span class="per">per CBM, shared container</span><p>China to the US West Coast, base ocean rate before port charges. Forwarder quotes, early October 2026.</p></div>
 <div class="pcard"><span class="amt">$7.02</span><span class="per">per kg by air</span><p>Hong Kong to North America, September 2026 average. To Europe: $4.80 per kg. TAC Index.</p></div>
 <div class="pcard"><span class="amt">2&#8211;5</span><span class="per">days by express</span><p>DHL, FedEx and UPS from 21 kg, priced at carrier weight breaks. For urgent restocks.</p></div>
 </div>
 </div>
</section>

<!-- ═══ RATES ═══ -->
<section class="prsec" id="rates">
 <div class="w">
 <div class="sl">Rates &amp; Transit Times</div>
 <h2 class="st">This month's market rates, by mode</h2>
 <p class="lead2">These are the rates the market paid on each lane on the date shown, so you know where a fair quote should land. They are not our price list. Your quote adds origin handling, export and import customs, delivery to Amazon and, if you ship DDP, the duty.</p>
 <div class="ptw"><table class="ptbl">
 <caption>Sea freight</caption>
 <thead><tr><th scope="col">Lane</th><th scope="col">Market rate</th><th scope="col">Typical transit</th></tr></thead>
 <tbody>
 <tr><td>Shanghai &rarr; Los Angeles, full container</td><td class="pr">$7,835 / 40ft</td><td>15&#8211;25 days port to port; about 25&#8211;35 days to an Amazon warehouse. <span class="src">Drewry WCI, 1 Oct 2026.</span></td></tr>
 <tr><td>Shanghai &rarr; New York, full container</td><td class="pr">$10,428 / 40ft</td><td>Longer than the West Coast, via the Panama Canal or Suez. <span class="src">Drewry WCI, 1 Oct 2026.</span></td></tr>
 <tr><td>Shanghai &rarr; Rotterdam, full container</td><td class="pr">$3,399 / 40ft</td><td>30&#8211;45+ days; most Asia&#8211;Europe sailings still go around the Cape. <span class="src">Drewry WCI, 1 Oct 2026; transit: Forto, Oct 2026.</span></td></tr>
 <tr><td>China &rarr; US West Coast, shared container (LCL)</td><td class="pr">$60&#8211;120 / CBM</td><td>15&#8211;25 days port to port. Base ocean rate; port and handling charges are extra. <span class="src">Forwarder quotes, early Oct 2026.</span></td></tr>
 <tr><td>China &rarr; Northern Europe, shared container (LCL)</td><td class="pr">$60&#8211;150 / CBM</td><td>30&#8211;45+ days. Base ocean rate, before port and handling charges. <span class="src">Forwarder quotes, 2026.</span></td></tr>
 </tbody></table></div>
 <div class="ptw"><table class="ptbl">
 <caption>Air and express</caption>
 <thead><tr><th scope="col">Lane</th><th scope="col">Market rate</th><th scope="col">Typical transit</th></tr></thead>
 <tbody>
 <tr><td>Hong Kong &rarr; North America, air freight</td><td class="pr">$7.02 / kg</td><td>About 5&#8211;10 days to an Amazon warehouse. Airport to airport average, spot and contract combined. <span class="src">TAC Index, September 2026.</span></td></tr>
 <tr><td>Hong Kong &rarr; Europe, air freight</td><td class="pr">$4.80 / kg</td><td>4&#8211;7 days airport to airport. <span class="src">TAC Index, September 2026; transit: Forto, Oct 2026.</span></td></tr>
 <tr><td>China &rarr; US, UK, EU, express courier</td><td class="pr">Per kg, by weight break</td><td>2&#8211;5 days door to door. Carriers price at 21, 45, 71 and 100 kg breaks, and bulky boxes are charged on volume.</td></tr>
 </tbody></table></div>
 <p class="rate-note">Shanghai is the index port. Rates from Shenzhen's Yantian and Shekou ports follow the same market but are not identical. Air rates are running above last year: TAC put Hong Kong to North America up 31% year on year in September 2026, with jet fuel a large part of the rise.</p>
 {figure("china-to-amazon-fba-container-shipping-sea-freight", 1200, 670, "Aerial view of a container terminal in Shenzhen at sunset, with a container ship alongside and stacked containers waiting for export", "Container terminals in Shenzhen sit minutes from our warehouse, so full containers and shared-container cargo leave without a long inland haul.")}
 </div>
</section>

<!-- ═══ WHICH MODE ═══ -->
<section class="prsec" id="modes">
 <div class="w">
 <div class="sl">Choosing a Mode</div>
 <h2 class="st">Which mode for which shipment</h2>
 <div class="ptw"><table class="ptbl">
 <caption>Rules of thumb and our minimums</caption>
 <thead><tr><th scope="col">Mode</th><th scope="col">Our minimum</th><th scope="col">Use it when</th></tr></thead>
 <tbody>
 <tr><td>Full container (FCL)</td><td class="pr">One 20ft</td><td>You ship more than about 15 CBM at a time. Above that, a container usually beats shared space on cost and is handled less on the way.</td></tr>
 <tr><td>Shared container (LCL)</td><td class="pr">1 CBM</td><td>Planned restocks of roughly 1 to 15 CBM, where 4 to 6 weeks door to door is fine.</td></tr>
 <tr><td>Air freight</td><td class="pr">100 kg</td><td>Launches, stock-outs and Q4 top-ups. Charged on actual or volume weight, whichever is higher; one CBM counts as 167 kg.</td></tr>
 <tr><td>Express courier</td><td class="pr">21 kg</td><td>Urgent restocks of a few cartons, or samples to Amazon.</td></tr>
 <tr><td>Rail or truck (Europe)</td><td class="pr">1 CBM / 1 pallet</td><td>Amazon EU restocks that are too urgent for sea and too heavy for air. See the rail and truck pages below.</td></tr>
 </tbody></table></div>
 {figure("fba-freight-pallet-loading-shenzhen-dock", 1200, 670, "Two warehouse staff in orange polo shirts loading a shrink-wrapped pallet of cartons into a box truck at the Shenzhen warehouse door", "Every mode starts at our dock. Pallets are built, wrapped and loaded in Shenzhen, then trucked to the port, the airport, the rail terminal or straight on to Europe.")}
 {XLINKS}
 </div>
</section>

{PREP_BUNDLE}

<!-- ═══ AMAZON RULES ═══ -->
<section class="prsec" id="amazon-rules">
 <div class="w">
 <div class="sl">At Amazon's Dock</div>
 <h2 class="st">What Amazon expects when your freight arrives</h2>
 <ul class="plain">
 <li><strong>Prep before it ships.</strong> Amazon stopped prepping and labelling US inbound stock on 1 January 2026, so FNSKU labels, poly bags and bundles must be done before the cargo leaves China. See <a href="avoid-amazon-fba-prep-rejections-china.html">how to avoid prep rejections</a>.</li>
 <li><strong>A label on every carton.</strong> Each carton needs its own FBA box label from your shipping plan. Copies are not accepted.</li>
 <li><strong>Carton and pallet limits.</strong> In the US the standard carton limit is 50 lb, and pallets are 40 &times; 48 inch. In the EU, standard cartons stay under 23 kg with no side over 63.5 cm, and cartons from 15 kg need heavy-package labels. We pack to the current limits in Seller Central for each marketplace.</li>
 <li><strong>Booked delivery.</strong> Pallet and container deliveries need an appointment at the Amazon warehouse, which can add two or three days at the end of the journey.</li>
 <li><strong>An importer of record.</strong> Amazon will not act as your importer. In the US every shipment from China now needs a formal customs entry and duty, including the <a href="section-301-forced-labor-tariff-china-2026.html">Section 301 duties</a>. See <a href="importer-of-record-china-fulfillment-2026.html">who is the importer of record</a>.</li>
 </ul>
 </div>
</section>

<!-- ═══ FAQ ═══ -->
<section class="faq-cat" id="faq">
 <div class="w">
 <div class="sl">FBA Freight Questions</div>
 <h2>Common questions about shipping to Amazon FBA</h2>
 <p class="cat-desc">If yours isn't here, send it with your quote request. We answer within 24 hours.</p>
{{{{FAQ}}}}
 </div>
</section>

<!-- ═══ CTA ═══ -->
{CTA}"""

# ───────────────────────── Page 2: rail ─────────────────────────
rail_faq = [
 ("How long does rail freight from China to Europe take?",
  "Typically 14 to 25 days depending on the route, against 30 to 45 days or more by sea. The fastest fixed-timetable trains, such as Xi'an to Duisburg, have run in as little as 11 days. Allow a few extra days for the truck to the Amazon warehouse and the delivery appointment."),
 ("How much does China to Europe rail freight cost?",
  "There is no public weekly index for rail. Monitoring by Index1520 put the average China&#8211;Europe rail rate at about $10,000 per 40ft container in August 2026, and forwarders quoted shared-container space at roughly $160 to $210 per CBM in early 2026. For comparison, a 40ft container by sea from Shanghai to Rotterdam was $3,399 on 1 October 2026. We quote rail and sea side by side."),
 ("Is China&#8211;Europe rail reliable in 2026?",
  "It is busy and growing: 5,460 trains ran in the first quarter of 2026, up 29% on a year earlier. The main risk is the Poland&#8211;Belarus border, where most trains enter the EU. Poland closed it from 12 to 25 September 2025, stranding more than 130 trains, and has closed several road crossings in 2026. We tell you the current border situation before you book."),
 ("Can rail freight go straight to an Amazon warehouse?",
  "The train runs to a European rail terminal. From there the cargo is cleared through customs and trucked to the Amazon fulfilment centre on your shipping plan, with a booked delivery appointment. We plan that last leg as part of the quote."),
 ("What is the minimum for rail?",
  "1 CBM for shared-container space, or a full 20ft or 40ft container."),
 ("Who clears customs in the EU?",
  "The importer does: you or a representative you appoint, with an EU EORI number. Amazon will not act as importer. On DDP shipments the duty and import VAT are paid within the price, but the importer's obligations stay with you. From 2028 the EU customs reform makes the seller the importer on distance sales; see our <a href=\"eu-customs-reform-importer-distance-sales-2026.html\">EU customs reform guide</a>."),
]
rail_body = f"""<!-- ═══ HERO ═══ -->
<section class="hero">
 <div class="w">
 <div class="sl">China&#8211;Europe Rail Freight</div>
 <h1>China&#8211;Europe rail freight, <span class="hi">in about half the time of sea</span></h1>
 <p>Rail moves containers from China to Europe in about 14 to 25 days, against 30 to 45 days or more by sea. It costs more than sea and far less than air, which makes it a strong option for Amazon EU restocks that cannot wait six weeks. Here is what the market is charging, how the routes work, and the risks to plan for.</p>
 <p class="asof">Market information checked {RATES_DATE}. Rail rates are not published weekly; your written quote states how long it is valid.</p>
 {FIT}
 <div class="pcards">
 <div class="pcard"><span class="amt">14&#8211;25</span><span class="per">days by rail</span><p>Typical China to Europe transit, depending on route. Forto, October 2026.</p></div>
 <div class="pcard"><span class="amt">~$10,000</span><span class="per">per 40ft by rail</span><p>Average China&#8211;Europe rail rate, August 2026, carrier-owned container. Index1520.</p></div>
 <div class="pcard"><span class="amt">$160&#8211;210</span><span class="per">per CBM, shared</span><p>Rail groupage quoted by forwarders in early 2026. Minimum 1 CBM.</p></div>
 <div class="pcard"><span class="amt">$3,399</span><span class="per">per 40ft by sea</span><p>Shanghai to Rotterdam for comparison, 30 to 45+ days. Drewry WCI, 1 Oct 2026.</p></div>
 </div>
 </div>
</section>

<!-- ═══ COMPARE ═══ -->
<section class="prsec" id="compare">
 <div class="w">
 <div class="sl">Rail vs Sea vs Air</div>
 <h2 class="st">How rail compares on cost and time</h2>
 <div class="ptw"><table class="ptbl">
 <caption>China to Europe, market references</caption>
 <thead><tr><th scope="col">Mode</th><th scope="col">Market rate</th><th scope="col">Typical transit and source</th></tr></thead>
 <tbody>
 <tr><td>Sea, full container</td><td class="pr">$3,399 / 40ft</td><td>30&#8211;45+ days; most sailings still route around the Cape. <span class="src">Drewry WCI Shanghai&#8211;Rotterdam, 1 Oct 2026.</span></td></tr>
 <tr><td>Rail, full container</td><td class="pr">~$10,000 / 40ft</td><td>14&#8211;25 days terminal to terminal. <span class="src">Index1520, August 2026 average; transit: Forto, Oct 2026.</span></td></tr>
 <tr><td>Rail, shared container</td><td class="pr">$160&#8211;210 / CBM</td><td>Similar to full-container rail, plus consolidation time at each end. <span class="src">Forwarder rates, early 2026.</span></td></tr>
 <tr><td>Truck</td><td class="pr">Quoted</td><td>About 12&#8211;20 days to Poland and Germany. See <a href="china-europe-truck-freight.html">truck freight to Europe</a>.</td></tr>
 <tr><td>Air freight</td><td class="pr">$4.80 / kg</td><td>4&#8211;7 days. <span class="src">TAC Index Hong Kong&#8211;Europe, September 2026.</span></td></tr>
 </tbody></table></div>
 <p class="rate-note">Quotes for rail vary widely by Chinese departure city, destination terminal and whether the container belongs to the carrier or the shipper. Rates on most routes eased by about $200 between July and August 2026 (Index1520).</p>
 <div class="callout"><strong>When rail makes sense:</strong> high-value goods where three weeks saved is worth paying for, Q4 restocks for Amazon EU that would miss the sea window, and cargo you would rather keep off the Red Sea and Cape routes. <strong>When it doesn't:</strong> heavy, low-value goods, where sea is far cheaper. Batteries and other dangerous goods need approval in advance, and not every train accepts them.</div>
 {figure("china-europe-rail-freight-container-train", 1200, 670, "A long container freight train crossing open steppe at golden hour, with hills on the horizon", "Most China&#8211;Europe trains cross Kazakhstan before they reach the EU border in Poland.")}
 </div>
</section>

<!-- ═══ HOW IT WORKS ═══ -->
<section class="prsec" id="how">
 <div class="w">
 <div class="sl">How It Works</div>
 <h2 class="st">From our Shenzhen dock to Amazon's European warehouses</h2>
 <ol class="steps">
 <li><div><h3>Consolidate and prep in Shenzhen</h3><p>Your suppliers deliver to us. We inspect, apply FNSKU labels, bag and carton everything to Amazon EU's limits, and build the pallets.</p></div></li>
 <li><div><h3>Truck to the rail departure</h3><p>Trains leave from several Chinese rail hubs, such as Xi'an, Chongqing, Chengdu, Wuhan and Yiwu. We match the departure to your destination and date.</p></div></li>
 <li><div><h3>Across Eurasia by train</h3><p>Most trains run through Kazakhstan, change rail gauge at the borders, and enter the EU at Ma&#322;aszewicze in Poland. Southern routes via the Caspian Sea and T&uuml;rkiye are slower, with more transfers.</p></div></li>
 <li><div><h3>EU customs clearance</h3><p>Your goods are cleared at the EU border or the destination terminal under your EORI number, or through the importer you appoint.</p></div></li>
 <li><div><h3>Delivery to Amazon</h3><p>A truck takes the pallets to the Amazon fulfilment centre on your shipping plan, on a booked delivery appointment.</p></div></li>
 </ol>
 {figure("fba-prep-carton-label-pallet-building-dispatch", 1200, 670, "A warehouse worker scanning Amazon FBA carton labels on stacked pallets of brown cartons ready for dispatch", "Cartons are labelled and palletised in Shenzhen before they leave, so nothing needs reworking in Europe.")}
 </div>
</section>

<!-- ═══ RISKS ═══ -->
<section class="prsec" id="risks">
 <div class="w">
 <div class="sl">Routes &amp; Risks</div>
 <h2 class="st">What to plan for on the rail route in 2026</h2>
 <ul class="plain">
 <li><strong>One main gateway.</strong> Estimates put 85 to 90% of China&#8211;Europe trains entering the EU at Ma&#322;aszewicze, on the Poland&#8211;Belarus border, so any disruption there affects most services.</li>
 <li><strong>Border closures.</strong> Poland closed the Belarus border from 12 to 25 September 2025, and more than 130 trains were held in Belarus. In 2026 Poland has closed several road crossings with Belarus. We check the border situation on the day you book.</li>
 <li><strong>Congestion.</strong> In July 2026, terminal congestion, maintenance work and heat added three to four days to rail transit through Poland and Germany (Index1520).</li>
 <li><strong>Demand is rising.</strong> 5,460 trains carried 546,000 TEU in the first quarter of 2026, up 29% and 22% on a year earlier (China State Railway Group), which keeps capacity tight in peak months.</li>
 </ul>
 <p class="rate-note">If the main route is disrupted, the alternatives are the southern Middle Corridor, rail-sea via Baltic ports, or switching the shipment to sea or truck. We quote the fallback when we quote the train.</p>
 </div>
</section>

{PREP_BUNDLE}

<!-- ═══ MORE OPTIONS ═══ -->
<section class="prsec" id="options">
 <div class="w">
 <div class="sl">Other Ways to Ship</div>
 <h2 class="st">Compare every route to Amazon</h2>
 {XLINKS}
 </div>
</section>

<!-- ═══ FAQ ═══ -->
<section class="faq-cat" id="faq">
 <div class="w">
 <div class="sl">Rail Freight Questions</div>
 <h2>Common questions about China&#8211;Europe rail</h2>
 <p class="cat-desc">If yours isn't here, send it with your quote request. We answer within 24 hours.</p>
{{{{FAQ}}}}
 </div>
</section>

<!-- ═══ CTA ═══ -->
{CTA}"""

# ───────────────────────── Page 3: truck ─────────────────────────
truck_faq = [
 ("How long does truck freight from China to Europe take?",
  "Forwarders quote about 12 to 18 days to Poland and 14 to 20 days to Germany. Destinations further west and south take longer, and southern routes through Central Asia, the Caucasus and T&uuml;rkiye can take considerably longer. Border queues can add days, so we quote the route and transit together."),
 ("How much does road freight from China to Europe cost?",
  "No public index tracks road freight on this lane, so there is no honest market average to publish. We quote per pallet, per cubic metre or per full truck, with the route and transit stated. As a guide, road usually costs more than rail and much less than air for the same cargo."),
 ("When should I choose truck over rail or air?",
  "Truck suits a few pallets to a few tonnes that are too heavy for air and too urgent for sea, especially to Central and Eastern Europe. It moves door to door with fewer handovers than rail, which helps with fragile or high-value goods. For full containers, rail is usually cheaper."),
 ("Can the truck deliver straight to an Amazon warehouse?",
  "Yes. After EU customs clearance, the pallets are delivered to the Amazon fulfilment centre on your shipping plan, on a booked delivery appointment. Pallets and cartons are built to Amazon EU's limits in Shenzhen before departure."),
 ("What is the minimum for truck freight?",
  "One pallet or 1 CBM for shared truck space, up to a full truck."),
 ("Is road freight affected by the Poland&#8211;Belarus border?",
  "It can be. Poland closed several road crossings with Belarus in January and April 2026, and trucks queued for days at the remaining ones in June. Routes that avoid Belarus run through Central Asia, the Caucasus and T&uuml;rkiye and take longer. We confirm the current route before booking."),
]
truck_body = f"""<!-- ═══ HERO ═══ -->
<section class="hero">
 <div class="w">
 <div class="sl">Truck Freight to Europe</div>
 <h1>Truck freight from China to Europe, <span class="hi">door to door</span></h1>
 <p>Road freight runs from China across Central Asia into Europe in about 12 to 20 days to Poland and Germany. Cargo travels under TIR customs seals with fewer handovers than rail, and it costs far less than air. It fits a few pallets that are too heavy to fly and too urgent to sail.</p>
 <p class="asof">Market information checked {RATES_DATE}. Road freight has no public rate index; your written quote states the route, transit and how long it is valid.</p>
 {FIT}
 <div class="pcards">
 <div class="pcard"><span class="amt">12&#8211;20</span><span class="per">days by road</span><p>Typical transit to Poland and Germany, from forwarders' 2026 transit tables.</p></div>
 <div class="pcard"><span class="amt">1</span><span class="per">pallet minimum</span><p>Shared truck space from one pallet or 1 CBM, up to a full truck.</p></div>
 <div class="pcard"><span class="amt">3,700+</span><span class="per">TIR trucks from China</span><p>Running on more than 120 routes into Central and Eastern Europe. IRU, 2026.</p></div>
 <div class="pcard"><span class="amt">Quoted</span><span class="per">per pallet or truck</span><p>With the route and transit in writing, within 24 hours.</p></div>
 </div>
 </div>
</section>

<!-- ═══ COMPARE ═══ -->
<section class="prsec" id="compare">
 <div class="w">
 <div class="sl">Truck vs Rail vs Sea vs Air</div>
 <h2 class="st">Where road freight fits</h2>
 <div class="ptw"><table class="ptbl">
 <caption>China to Europe, market references</caption>
 <thead><tr><th scope="col">Mode</th><th scope="col">Market rate</th><th scope="col">Typical transit and source</th></tr></thead>
 <tbody>
 <tr><td>Sea, full container</td><td class="pr">$3,399 / 40ft</td><td>30&#8211;45+ days. <span class="src">Drewry WCI Shanghai&#8211;Rotterdam, 1 Oct 2026.</span></td></tr>
 <tr><td>Rail, full container</td><td class="pr">~$10,000 / 40ft</td><td>14&#8211;25 days. <span class="src">Index1520, August 2026; see <a href="china-europe-rail-freight.html">rail freight</a>.</span></td></tr>
 <tr><td>Truck, per pallet or full truck</td><td class="pr">Quoted</td><td>About 12&#8211;18 days to Poland, 14&#8211;20 to Germany. <span class="src">Forwarder transit tables, 2026.</span></td></tr>
 <tr><td>Air freight</td><td class="pr">$4.80 / kg</td><td>4&#8211;7 days. <span class="src">TAC Index Hong Kong&#8211;Europe, September 2026.</span></td></tr>
 </tbody></table></div>
 <div class="callout"><strong>Truck is the right call when:</strong> you have roughly 1 to 15 pallets for Amazon EU or a European warehouse, the goods are too heavy or bulky to fly, and six weeks at sea is too long. <strong>Choose rail instead</strong> for full containers, and <strong>sea</strong> when time is not the constraint.</div>
 </div>
</section>

<!-- ═══ HOW IT WORKS ═══ -->
<section class="prsec" id="how">
 <div class="w">
 <div class="sl">How It Works</div>
 <h2 class="st">From Shenzhen to a European warehouse by road</h2>
 <ol class="steps">
 <li><div><h3>Consolidate and prep in Shenzhen</h3><p>Suppliers deliver to us. We inspect, label and palletise to Amazon EU's carton and pallet limits.</p></div></li>
 <li><div><h3>Seal and depart under TIR</h3><p>The cargo leaves under a TIR customs transit document, which lets sealed loads cross borders on the way with fewer inspections.</p></div></li>
 <li><div><h3>Across Central Asia</h3><p>Northern routes run through Kazakhstan towards Poland. Southern routes cross Central Asia, the Caucasus and T&uuml;rkiye into the EU and take longer.</p></div></li>
 <li><div><h3>EU customs clearance</h3><p>Cleared at the EU entry point or the destination under your EORI number, or through the importer you appoint.</p></div></li>
 <li><div><h3>Delivery to Amazon or your warehouse</h3><p>Delivered on a booked appointment to the Amazon fulfilment centre on your shipping plan, or to your own European address.</p></div></li>
 </ol>
 {figure("china-europe-road-freight-truck-loading", 1200, 670, "Two warehouse staff in orange polo shirts loading and strapping shrink-wrapped pallets of cartons into a curtain-sided trailer at the Shenzhen warehouse dock", "Pallets are wrapped, loaded and strapped at our Shenzhen dock before the truck leaves.")}
 </div>
</section>

<!-- ═══ RISKS ═══ -->
<section class="prsec" id="risks">
 <div class="w">
 <div class="sl">Routes &amp; Risks</div>
 <h2 class="st">What to plan for on the road in 2026</h2>
 <ul class="plain">
 <li><strong>Border crossings.</strong> Poland closed several road crossings with Belarus in January and April 2026. In late June, Belarus's border committee reported hundreds of trucks queuing at Kukuryki, the busiest crossing into the EU.</li>
 <li><strong>Route choice.</strong> Routes avoiding Belarus run through the Caucasus and T&uuml;rkiye. They avoid that border but add distance and time.</li>
 <li><strong>Paperwork.</strong> TIR carnets, export declarations and EU import entries all have to match. We prepare the export side in Shenzhen and coordinate the import entry with your importer.</li>
 </ul>
 <p class="rate-note">We confirm the route, the expected border crossing and the transit in writing before the truck is loaded.</p>
 </div>
</section>

{PREP_BUNDLE}

<!-- ═══ MORE OPTIONS ═══ -->
<section class="prsec" id="options">
 <div class="w">
 <div class="sl">Other Ways to Ship</div>
 <h2 class="st">Compare every route to Amazon</h2>
 {XLINKS}
 </div>
</section>

<!-- ═══ FAQ ═══ -->
<section class="faq-cat" id="faq">
 <div class="w">
 <div class="sl">Truck Freight Questions</div>
 <h2>Common questions about road freight to Europe</h2>
 <p class="cat-desc">If yours isn't here, send it with your quote request. We answer within 24 hours.</p>
{{{{FAQ}}}}
 </div>
</section>

<!-- ═══ CTA ═══ -->
{CTA}"""

pages = [
 dict(slug="fba-freight-from-china", crumb="FBA Freight from China",
      title="FBA Freight from China: Sea, Air & Express Rates (2026)",
      desc="Ship from Shenzhen to Amazon FBA in the US, UK and EU: October 2026 market rates, transit times, minimums, and prep plus freight in one quote.",
      h1="Freight to Amazon FBA from China", service_name="Amazon FBA freight from China (sea, air and express)",
      service_type="Freight forwarding to Amazon FBA", area=["United States", "United Kingdom", "European Union"],
      og_image="fba-freight-pallet-loading-shenzhen-dock", modified="2026-10-08", faq=fba_faq, body=fba_body),
 dict(slug="china-europe-rail-freight", crumb="China-Europe Rail Freight",
      title="China–Europe Rail Freight to Amazon EU: 2026 Rates & Times",
      desc="Rail freight from China to Europe in about 14 to 25 days. October 2026 market rates, routes, border risks, minimums and delivery to Amazon EU warehouses.",
      h1="China–Europe rail freight", service_name="China to Europe rail freight", service_type="Rail freight forwarding",
      area="European Union", og_image="china-europe-rail-freight-container-train", modified="2026-10-08", faq=rail_faq, body=rail_body),
 dict(slug="china-europe-truck-freight", crumb="Truck Freight to Europe",
      title="Truck Freight from China to Europe: 2026 Road Freight Guide",
      desc="Road freight from China to Poland, Germany and beyond in about 12 to 20 days: when trucking beats rail or air, routes, minimums and Amazon EU delivery.",
      h1="Truck freight from China to Europe", service_name="China to Europe road freight (TIR)", service_type="Road freight forwarding",
      area="European Union", og_image="china-europe-road-freight-truck-loading", modified="2026-10-08", faq=truck_faq, body=truck_body),
]
for p in pages:
    print(build(p))
