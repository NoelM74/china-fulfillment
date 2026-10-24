#!/usr/bin/env python3
"""Write the four November 2026 infographics as HTML (rendered to 1200x1500 by render.mjs).

House style (IMAGE-STYLE-GUIDE.md section 6): flat vector, navy and orange, on white.
Every figure here is taken from the matching article, with its source and date.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY, ORANGE, LINE, GREY = "#0d2144", "#d9650b", "#d5dbe6", "#4a6178"

BASE_CSS = """
<link rel="stylesheet" href="outfit-local.css">
<style>
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{width:1200px;height:1500px;background:#fff;font-family:'Outfit',sans-serif;color:NAVY;-webkit-font-smoothing:antialiased}
.wrap{width:1200px;height:1500px;padding:44px 48px;display:flex;flex-direction:column;gap:22px}
.fill{flex:1;display:flex;flex-direction:column;gap:22px}
.fill>.card{flex:1}
.title{background:NAVY;color:#fff;font-weight:800;font-size:62px;letter-spacing:.5px;text-transform:uppercase;text-align:center;padding:26px 18px;border-radius:8px;line-height:1.05}
.card{border:3px solid LINE;border-radius:10px;display:flex;align-items:center;gap:30px;padding:24px 30px;background:#fff}
.card svg{flex:0 0 auto}
.lbl{font-weight:800;font-size:50px;text-transform:uppercase;line-height:1.04;letter-spacing:.3px}
.sub{font-weight:700;font-size:37px;line-height:1.2;margin-top:6px}
.small{font-weight:600;font-size:26px;color:GREY;margin-top:6px;line-height:1.25}
.or{background:ORANGE;border-color:ORANGE;color:#fff}
.or .small{color:#fff;opacity:.92}
.nv{background:NAVY;border-color:NAVY;color:#fff}
.foot{border-radius:8px;text-align:center;font-weight:800;font-size:46px;text-transform:uppercase;padding:26px 18px;line-height:1.1;letter-spacing:.3px}
.foot .small{font-size:26px;text-transform:none;font-weight:600;margin-top:8px;color:#fff;opacity:.92}
.grow{flex:1}
.arrow{color:ORANGE;font-weight:800}
.nc{text-transform:none}
</style>
""".replace("NAVY", NAVY).replace("ORANGE", ORANGE).replace("LINE", LINE).replace("GREY", GREY)


def svg(body, size=96):
    return ('<svg width="%d" height="%d" viewBox="0 0 96 96" fill="none" stroke="%s" '
            'stroke-width="5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % (size, size, NAVY, body))


def white(s):
    return s.replace('stroke="%s"' % NAVY, 'stroke="#ffffff"')


ICON = {
    "box": svg('<path d="M48 10 82 28v40L48 86 14 68V28z"/><path d="M14 28l34 18 34-18M48 46v40"/><path d="M31 19l34 18"/>'),
    "doc": svg('<path d="M24 8h34l16 16v64H24z"/><path d="M58 8v16h16M34 44h30M34 56h30M34 68h20"/>'),
    "ship": svg('<path d="M8 60h80l-10 20H20z"/><rect x="22" y="40" width="16" height="20"/><rect x="40" y="40" width="16" height="20"/><rect x="58" y="40" width="16" height="20"/><rect x="40" y="22" width="16" height="18"/>'),
    "train": svg('<rect x="10" y="26" width="76" height="34" rx="3"/><path d="M24 26v34M38 26v34M52 26v34M66 26v34"/><path d="M6 66h84"/><circle cx="24" cy="76" r="7"/><circle cx="72" cy="76" r="7"/>'),
    "truck": svg('<rect x="6" y="26" width="54" height="40" rx="3"/><path d="M60 40h16l14 14v12H60z"/><circle cx="24" cy="74" r="8"/><circle cx="74" cy="74" r="8"/>'),
    "plane": svg('<path d="M48 8c5 0 7 6 7 12v16l31 18v9L55 54v16l11 8v7l-18-5-18 5v-7l11-8V54L10 63v-9l31-18V20c0-6 2-12 7-12z"/>'),
    "clear": svg('<rect x="14" y="22" width="68" height="56" rx="6"/><path d="M30 50l12 12 24-26"/>'),
    "shelf": svg('<path d="M12 84V14M84 84V14M12 36h72M12 60h72M12 84h72"/><rect x="22" y="40" width="18" height="16"/><rect x="46" y="16" width="18" height="16"/><rect x="50" y="64" width="22" height="16"/>'),
    "person": svg('<circle cx="48" cy="30" r="16"/><path d="M16 86c4-20 18-30 32-30s28 10 32 30"/>'),
    "van": svg('<path d="M6 30h52v38H6z"/><path d="M58 42h18l14 14v12H58z"/><circle cx="24" cy="74" r="8"/><circle cx="74" cy="74" r="8"/><path d="M16 44h30"/>'),
}


def page(name, inner):
    html = "<!doctype html><html><head><meta charset='utf-8'>%s</head><body><div class='wrap'>%s</div></body></html>" % (BASE_CSS, inner)
    path = os.path.join(OUT, name + ".html")
    open(path, "w", encoding="utf-8").write(html)
    print("wrote", path)


# 1. Sea freight to Amazon FBA: the run, step by step -----------------------
steps = [
    ("box", "Prep and label", "Before it sails: FNSKU labels, cartons to Amazon's limits"),
    ("doc", "Hand over and file ISF", "At least 24 hours before loading"),
    ("ship", "Ocean to US West Coast", "About 15&ndash;25 days port to port"),
    ("clear", "Customs and delivery", "Entry, duty, booked Amazon appointment"),
    ("shelf", "Checked in at Amazon", "About 25&ndash;35 days from sailing"),
]
rows = ""
for i, (ic, lbl, sub) in enumerate(steps, 1):
    rows += ("<div class='card' style='padding:20px 30px'>"
             "<div style='flex:0 0 112px;height:112px;border-radius:50%%;background:%s;color:#fff;font-weight:800;font-size:60px;"
             "display:flex;align-items:center;justify-content:center'>%d</div>%s"
             "<div><div class='lbl' style='font-size:48px'>%s</div><div class='sub'><span class='arrow'>&rarr;</span> %s</div></div></div>"
             % (NAVY, i, ICON[ic].replace('width="96" height="96"', 'width="104" height="104"'), lbl, sub))
page("infographic-sea-freight-fba-timeline",
     "<div class='title'>Shenzhen to Amazon by sea</div><div class='fill'>" + rows + "</div>"
     "<div class='foot or'>CNY 2027: sail in December<div class='small'>for stock you need selling through February. Chinese New Year is 6 February 2027.</div></div>")

# 2. LCL or FCL ---------------------------------------------------------------
def container(w, label, h=118):
    return ("<div style='display:flex;align-items:center;gap:22px'>"
            "<div style='width:%dpx;height:%dpx;border:4px solid %s;border-radius:6px;"
            "background:repeating-linear-gradient(90deg,#eef1f7 0 22px,#dfe4ee 22px 26px)'></div>"
            "<div class='lbl' style='font-size:42px;white-space:nowrap'>%s</div></div>" % (w, h, NAVY, label))

page("infographic-lcl-vs-fcl-break-even",
     "<div class='title'>LCL or FCL?</div>"
     "<div class='card' style='flex-direction:column;align-items:flex-start;gap:18px'>"
     "<div class='lbl' style='font-size:36px;color:%s'>Container space (internal)</div>" % GREY +
     container(290, "20ft &middot; <span class='nc'>~33 m&sup3;</span>") + container(592, "40ft &middot; <span class='nc'>~68 m&sup3;</span>") +
     container(592, "40ft HC &middot; <span class='nc'>~76 m&sup3;</span>", h=136) +
     "</div>"
     "<div class='card nv' style='flex-direction:column;align-items:flex-start;gap:4px;padding:38px 40px'>"
     "<div class='lbl' style='font-size:56px'>Break-even CBM =</div>"
     "<div class='sub' style='font-size:44px'>(FCL all-in price &minus; LCL fixed charges)</div>"
     "<div class='sub' style='font-size:44px'>&divide; LCL rate per CBM</div></div>"
     "<div style='display:flex;gap:14px'>"
     "<div class='card' style='flex:1;flex-direction:column;align-items:flex-start;gap:4px;padding:30px 24px'><div class='lbl' style='font-size:52px'>LCL</div><div class='sub' style='font-size:34px'>under ~12 CBM</div></div>"
     "<div class='card or' style='flex:1.25;flex-direction:column;align-items:flex-start;gap:4px;padding:30px 24px'><div class='lbl' style='font-size:52px'>Run the sum</div><div class='sub' style='font-size:34px'>~12&ndash;18 CBM</div></div>"
     "<div class='card nv' style='flex:1;flex-direction:column;align-items:flex-start;gap:4px;padding:30px 24px'><div class='lbl' style='font-size:52px'>FCL</div><div class='sub' style='font-size:34px'>over ~18 CBM</div></div>"
     "</div>"
     "<div class='small' style='font-size:28px;margin-top:-6px;text-align:center'>Typical 20ft crossover, China to US. It moves with rates, so compare same-day quotes.</div>"
     "<div class='grow'></div>"
     "<div class='foot or'>LCL closes first before CNY<div class='small'>Book all sea freight by mid-January 2027.</div></div>")

# 3. China to Europe, four modes ---------------------------------------------
modes = [
    ("ship", "Sea", "30&ndash;45+ days", "$3,632 / 40ft", "Shanghai&ndash;Rotterdam, Drewry WCI, 22 Oct 2026"),
    ("train", "Rail", "14&ndash;25 days", "~$10,000 / 40ft", "China&ndash;Europe average, Index1520, Aug 2026"),
    ("truck", "Truck", "12&ndash;20 days", "Quoted per load", "To Poland and Germany"),
    ("plane", "Air", "4&ndash;7 days", "$4.80 / kg", "Hong Kong&ndash;Europe, TAC Index, Sep 2026"),
]
cards = ""
for ic, lbl, days, cost, src in modes:
    cards += ("<div class='card' style='padding:22px 32px'>%s"
              "<div style='flex:1'><div class='lbl' style='font-size:48px'>%s</div><div class='sub' style='font-size:56px;font-weight:800'>%s</div></div>"
              "<div style='text-align:right;max-width:440px'><div class='lbl' style='font-size:46px;color:%s;text-transform:none'>%s</div><div class='small' style='font-size:26px'>%s</div></div></div>"
              % (ICON[ic], lbl, days, ORANGE, cost, src))
page("infographic-china-europe-four-modes",
     "<div class='title'>China to Europe: 4 ways</div><div class='fill'>" + cards + "</div>"
     "<div class='foot nv'>Same EU customs, whichever mode<div class='small'>Duty, import VAT and the importer's obligations follow the goods, not the mode.</div></div>")

# 4. IEEPA refund: who gets paid ---------------------------------------------
page("infographic-ieepa-refund-who-gets-paid",
     "<div class='title'>Who gets the refund?</div>"
     "<div class='card nv' style='flex-direction:column;align-items:flex-start;gap:6px;padding:36px 40px'>"
     "<div class='small' style='color:#fff;font-size:30px;opacity:.9'>Check the US entry summary for each shipment</div>"
     "<div class='lbl' style='font-size:56px'>Whose name is on it as importer of record?</div></div>"
     "<div style='text-align:center;font-size:60px;line-height:.6;color:%s;font-weight:800'>&darr;</div>" % ORANGE +
     "<div class='fill'><div class='card or'>%s<div><div class='lbl'>You</div><div class='sub'>You or your broker file in CAPE. Paid to you by ACH.</div></div></div>" % white(ICON["person"]) +
     "<div class='card'>%s<div><div class='lbl'>A courier</div><div class='sub'>Refund goes to the carrier, then to whoever paid, under its policy.</div></div></div>" % ICON["van"] +
     "<div class='card'>%s<div><div class='lbl'>A DDP forwarder</div><div class='sub'>Refund goes to the forwarder. Your contract decides what reaches you.</div></div></div></div>" % ICON["ship"] +
     ""
     "<div class='foot nv'>CAPE pays the importer of record only<div class='small'>Section 122 and Section 301 duties are not part of CAPE.</div></div>")
