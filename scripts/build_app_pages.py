#!/usr/bin/env python3
"""Build the Worker-backed app pages (shipping calculator + order tracking).

Both pages reuse the head, nav and footer from our-pricing.html so the site
chrome stays identical. The dynamic parts talk to the /api/* Worker routes
(worker/index.js). Edit this script, not the built HTML, or the next build
reverts your change (same rule as the blog and freight builders).

Usage:  python3 scripts/build_app_pages.py
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = open(os.path.join(REPO, "our-pricing.html"), encoding="utf-8").read()

# --- slices shared with the freight builder -------------------------------
HEAD_START = SRC[:SRC.index("<title>")]
SHARED_HEAD = SRC[SRC.index('<link rel="preconnect" href="https://fonts.googleapis.com"/>'):SRC.index("</head>")]
NAV = SRC[SRC.index("<body>") + 6:SRC.index("<!-- ═══ HERO ═══ -->")]
FOOTER = SRC[SRC.index("<footer>"):]

ORIGIN = "https://www.china-fulfillment.com/"

# --- page-specific CSS (uses the site's existing custom properties) --------
APP_CSS = """
<style>
.app-hero .w{max-width:1100px}
.apibadge{display:inline-flex;align-items:center;gap:7px;font-size:.78rem;font-weight:700;letter-spacing:.02em;
  padding:5px 12px;border-radius:999px;margin-bottom:14px;text-transform:uppercase}
.apibadge::before{content:"";width:8px;height:8px;border-radius:50%;background:currentColor}
.apibadge[data-state="live"]{background:rgba(16,185,129,.14);color:#0b7a55}
.apibadge[data-state="preview"]{background:rgba(249,115,22,.14);color:#b24c05}
.apibadge[data-state="checking"]{background:#eef1f7;color:#4a6178}
.app-wrap{max-width:1100px;margin:0 auto;padding:30px 5% 72px}
.app-form{display:grid;grid-template-columns:1.4fr .8fr auto;gap:18px;align-items:end;
  background:var(--w);border:1px solid var(--bd);border-radius:16px;padding:22px;box-shadow:0 1px 3px rgba(12,26,46,.05)}
.app-form .fld{display:flex;flex-direction:column;gap:6px}
.app-form label{font-size:.82rem;font-weight:700;color:var(--ink)}
.app-form select,.app-form input{font:inherit;padding:11px 12px;border:1px solid var(--bd);border-radius:10px;
  background:var(--off);color:var(--ink);width:100%}
.app-form select:focus,.app-form input:focus{outline:2px solid var(--blue);outline-offset:1px;background:var(--w)}
.dims{grid-column:1 / -1;border:1px dashed var(--bd);border-radius:12px;padding:12px 14px;margin:0}
.dims legend{font-size:.82rem;font-weight:700;color:var(--ink);padding:0 6px}
.dims .opt{font-weight:500;color:var(--mu)}
.dimrow{display:flex;gap:12px;flex-wrap:wrap}
.dimrow label{display:flex;align-items:center;gap:7px;font-size:.82rem;color:var(--mu);font-weight:700}
.dimrow input{width:84px}
.hint{font-size:.78rem;color:var(--mu);margin:8px 0 0}
.app-form .ncta,.trk-form .ncta{white-space:nowrap}
.trk-form{display:flex;gap:14px;background:var(--w);border:1px solid var(--bd);border-radius:16px;padding:22px;
  box-shadow:0 1px 3px rgba(12,26,46,.05);flex-wrap:wrap}
.trk-form input{flex:1 1 320px;font:inherit;padding:12px 14px;border:1px solid var(--bd);border-radius:10px;background:var(--off)}
.app-result{margin-top:26px}
.app-msg{padding:16px 18px;border-radius:12px;font-size:.92rem;line-height:1.5}
.app-msg.err{background:rgba(208,34,34,.08);color:#9a1414;border:1px solid rgba(208,34,34,.25)}
.app-msg.info{background:#eef1f7;color:#334b63;border:1px solid var(--bd)}
.sample-banner{display:flex;gap:10px;align-items:flex-start;background:rgba(249,115,22,.1);border:1px solid rgba(249,115,22,.35);
  color:#8a3d04;border-radius:12px;padding:12px 16px;font-size:.88rem;line-height:1.5;margin-bottom:16px;font-weight:600}
.rate-table,.trk-wrap{background:var(--w);border:1px solid var(--bd);border-radius:14px;overflow:hidden}
table.rates{width:100%;border-collapse:collapse;font-size:.92rem}
table.rates th,table.rates td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--bd)}
table.rates th{background:var(--navy);color:#fff;font-size:.76rem;text-transform:uppercase;letter-spacing:.03em}
table.rates tbody tr:last-child td{border-bottom:0}
table.rates tbody tr:nth-child(even){background:#fafbfe}
table.rates .svc{font-weight:700;color:var(--ink)}
table.rates .amt{font-weight:800;color:var(--navy);white-space:nowrap;text-align:right}
table.rates .usd{color:var(--mu);font-weight:600;font-size:.82rem}
.rate-best{display:inline-block;font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em;
  background:var(--acl);color:var(--acd);padding:2px 7px;border-radius:999px;margin-left:8px;vertical-align:middle}
.rate-cta{padding:16px 18px;background:var(--off);display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.rate-cta p{margin:0;color:var(--mu);font-size:.86rem}
.app-note{margin-top:30px;background:var(--off);border:1px solid var(--bd);border-radius:14px;padding:22px 24px}
.app-note h3{margin:0 0 10px;font-size:1.02rem}
.app-note ul{margin:0;padding-left:20px;color:var(--mu);font-size:.9rem;line-height:1.7}
.trk-header{padding:18px 20px;border-bottom:1px solid var(--bd);display:flex;gap:10px 26px;flex-wrap:wrap}
.trk-header .k{font-size:.72rem;text-transform:uppercase;letter-spacing:.03em;color:var(--mu);font-weight:700}
.trk-header .v{font-weight:700;color:var(--ink)}
.trk-timeline{list-style:none;margin:0;padding:22px 24px}
.trk-timeline li{position:relative;padding:0 0 22px 28px;border-left:2px solid var(--bd)}
.trk-timeline li:last-child{border-left-color:transparent;padding-bottom:0}
.trk-timeline li::before{content:"";position:absolute;left:-8px;top:2px;width:14px;height:14px;border-radius:50%;
  background:var(--bd);border:3px solid var(--w)}
.trk-timeline li:first-child::before{background:var(--ac)}
.trk-timeline .desc{font-weight:700;color:var(--ink)}
.trk-timeline .time{font-size:.82rem;color:var(--mu);margin-top:2px}
.app-sub{margin-top:16px;color:var(--mu);font-size:.88rem}
.spin{display:inline-block;width:16px;height:16px;border:2px solid var(--bd);border-top-color:var(--blue);
  border-radius:50%;animation:sp .7s linear infinite;vertical-align:-3px;margin-right:8px}
@keyframes sp{to{transform:rotate(360deg)}}
@media(max-width:760px){
  .app-form{grid-template-columns:1fr}
  table.rates .cn,table.rates .trk{display:none}
}
</style>
"""


def meta(title, desc, slug, og):
    return (
        f"<title>{title}</title>\n"
        f'<meta name="description" content="{desc}"/>\n'
        f'<link rel="canonical" href="{ORIGIN}{slug}"/>\n'
        f'<meta property="og:type" content="website"/>\n'
        f'<meta property="og:title" content="{title}"/>\n'
        f'<meta property="og:description" content="{desc}"/>\n'
        f'<meta property="og:url" content="{ORIGIN}{slug}"/>\n'
        f'<meta property="og:image" content="{ORIGIN}images/site/{og}"/>\n'
        f'<meta name="twitter:card" content="summary_large_image"/>\n'
    )


def page(title, desc, slug, og, hero, body, script):
    return (
        HEAD_START
        + meta(title, desc, slug, og)
        + SHARED_HEAD
        + APP_CSS
        + "</head>\n<body>"
        + NAV
        + hero
        + body
        + FOOTER.rstrip().rsplit("</body>", 1)[0]
        + script
        + "\n</body>\n</html>\n"
    )


# ───────────────────────── Shipping calculator ─────────────────────────
CALC_HERO = """
<section class="hero app-hero">
 <div class="w">
  <span class="apibadge" id="apiBadge" data-state="checking">Checking status</span>
  <h1>Shipping rate <span class="hi">calculator</span></h1>
  <p>Compare carrier services from our Shenzhen warehouse. Enter a destination, weight and parcel size to see delivery windows and guide prices side by side.</p>
  <p class="asof"><strong>Guide prices only.</strong> We confirm the final price once our team has checked the actual weight and dimensions of your shipment. Prices exclude duties, VAT and remote-area surcharges.</p>
 </div>
</section>
"""

CALC_BODY = """
<section class="app-wrap">
 <form id="rateForm" class="app-form" autocomplete="off">
  <div class="fld">
   <label for="country">Destination country</label>
   <select id="country" name="country" required><option value="">Loading countries</option></select>
  </div>
  <div class="fld">
   <label for="weight">Weight (kg)</label>
   <input id="weight" name="weight" type="number" min="0.01" step="0.01" value="0.5" required/>
  </div>
  <button type="submit" class="ncta" id="calcBtn">Calculate rates</button>
  <fieldset class="dims">
   <legend>Parcel size in cm <span class="opt">optional, improves accuracy</span></legend>
   <div class="dimrow">
    <label>L <input id="l" type="number" min="0" max="400" step="1" placeholder="10"/></label>
    <label>W <input id="w" type="number" min="0" max="400" step="1" placeholder="10"/></label>
    <label>H <input id="h" type="number" min="0" max="400" step="1" placeholder="10"/></label>
   </div>
   <p class="hint">Carriers charge on volumetric weight when it is higher than the actual weight.</p>
  </fieldset>
 </form>

 <div id="result" class="app-result" aria-live="polite"></div>

 <div class="app-note">
  <h3>How to read these rates</h3>
  <ul>
   <li>Every total is a guide for comparing services. We confirm the final price after checking the actual weight and dimensions of your goods.</li>
   <li>Each total includes the carrier base fee and fuel surcharge.</li>
   <li>It excludes export declaration, pickup, remote-area surcharges, and destination duties and VAT.</li>
   <li>Delivery times are working days after dispatch and can move with customs, weather and holidays.</li>
   <li>Batteries, liquids and other restricted goods ship on specific services only. <a href="Contact-Us.html">Ask our team</a> if you are unsure.</li>
  </ul>
 </div>
</section>
"""

# Representative sample used only when the API key is not yet wired in.
# Real figures captured from the back-office rate tool: United States, 0.5 kg, 10x10x10 cm.
CALC_SCRIPT = r"""
<script>
(function(){
  var SAMPLE = {currency:"RMB", services:[
    {name:"UNIUNI 6000", code:"UNIUNI", days:"1-6", total:22.23},
    {name:"USPS-P", code:"USPS-P", days:"2-4", total:68.41},
    {name:"PFCEXPRESS", code:"PFCEXPRESS", days:"7-16", total:74.50},
    {name:"PFCGL", code:"PFCGL", days:"6-10", total:77.50},
    {name:"USPS", code:"USPS", days:"8-12", total:110.50},
    {name:"USUPS", code:"USUPS", days:"4-7", total:210.70},
    {name:"HKDHL", code:"HKDHL", days:"3-6", total:304.09},
    {name:"SZFEDEX-IP", code:"SZFEDEX-IP", days:"3-6", total:485.43}
  ]};
  var badge=document.getElementById("apiBadge");
  var sel=document.getElementById("country");
  var form=document.getElementById("rateForm");
  var out=document.getElementById("result");
  var btn=document.getElementById("calcBtn");
  var LIVE=false;

  function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function money(n){return Number(n).toFixed(2);}

  fetch("/api/health").then(function(r){return r.json();}).then(function(h){
    LIVE=!!h.configured;
    badge.dataset.state=LIVE?"live":"preview";
    badge.textContent=LIVE?"Live guide prices":"Preview, rates not connected yet";
  }).catch(function(){badge.dataset.state="preview";badge.textContent="Preview";});

  fetch("/api/countries").then(function(r){
    if(!r.ok) throw 0; return r.json();
  }).then(function(d){
    sel.innerHTML='<option value="">Select a country</option>';
    (d.countries||[]).forEach(function(c){
      var o=document.createElement("option");o.value=c.code;o.textContent=c.name;sel.appendChild(o);
    });
  }).catch(function(){
    // Preview fallback so the form is usable before the key lands.
    sel.innerHTML='<option value="221">United States (sample)</option>';
  });

  function renderTable(data,isSample){
    var s=data.services||[];
    if(!s.length){out.innerHTML='<div class="app-msg info">No services returned for that destination and weight.</div>';return;}
    var fx=data.fx_usd;
    var h="";
    if(isSample){h+='<div class="sample-banner"><span>⚠</span><span><strong>Sample data, not a live quote.</strong> These are example figures for the United States at 0.5&nbsp;kg so you can see the layout. Live carrier rates appear here once the PFC API key is added.</span></div>';}
    h+='<div class="rate-table"><table class="rates"><thead><tr><th>Service</th><th class="cn">Carrier code</th><th>Delivery</th><th style="text-align:right">Guide total ('+esc(data.currency||"RMB")+')</th></tr></thead><tbody>';
    s.forEach(function(x,i){
      h+='<tr><td class="svc">'+esc(x.name)+(i===0?'<span class="rate-best">Cheapest</span>':'')+'</td>'+
         '<td class="cn">'+esc(x.code)+'</td>'+
         '<td>'+esc(x.days)+' days</td>'+
         '<td class="amt">'+(data.currency==="RMB"?"¥":"")+money(x.total)+
            (fx&&x.usd?'<div class="usd">≈ $'+money(x.usd)+'</div>':'')+'</td></tr>';
    });
    h+='</tbody></table><div class="rate-cta"><p>Guide prices only. We confirm the final price once we have checked the actual weight and dimensions. Excludes duties, VAT and remote-area surcharges.</p><a class="ncta" href="Contact-Us.html">Get a firm quote</a></div></div>';
    out.innerHTML=h;
  }

  form.addEventListener("submit",function(e){
    e.preventDefault();
    var country=sel.value, weight=document.getElementById("weight").value;
    if(!country){out.innerHTML='<div class="app-msg err">Please choose a destination country.</div>';return;}
    if(!(parseFloat(weight)>0)){out.innerHTML='<div class="app-msg err">Please enter a weight in kilograms.</div>';return;}
    var q=new URLSearchParams({country:country,weight:weight});
    ["l","w","h"].forEach(function(id){var v=document.getElementById(id).value;if(v)q.set(id,v);});
    out.innerHTML='<div class="app-msg info"><span class="spin"></span>Fetching rates</div>';
    btn.disabled=true;
    fetch("/api/rate?"+q.toString()).then(function(r){
      return r.json().then(function(j){return {status:r.status,body:j};});
    }).then(function(res){
      btn.disabled=false;
      if(res.status===200){renderTable(res.body,false);return;}
      if(res.status===503){renderTable(SAMPLE,true);return;}
      if(res.status===400){out.innerHTML='<div class="app-msg err">Please check the destination and weight and try again.</div>';return;}
      out.innerHTML='<div class="app-msg err">The rate service is temporarily unavailable. Please <a href="Contact-Us.html">contact us</a> for a quote.</div>';
    }).catch(function(){
      btn.disabled=false;
      out.innerHTML='<div class="app-msg err">Could not reach the rate service. Please try again shortly.</div>';
    });
  });
})();
</script>
"""

# ───────────────────────────── Order tracking ─────────────────────────────
TRK_HERO = """
<section class="hero app-hero">
 <div class="w">
  <span class="apibadge" id="apiBadge" data-state="checking">Checking status</span>
  <h1>Track your <span class="hi">shipment</span></h1>
  <p>Enter your tracking number or order number to see the latest scan events on your parcel or freight.</p>
 </div>
</section>
"""

TRK_BODY = """
<section class="app-wrap">
 <form id="trkForm" class="trk-form">
  <input id="trkNo" name="no" type="text" placeholder="e.g. RT209114500HK or R800001411160002" required aria-label="Tracking or order number"/>
  <button type="submit" class="ncta">Track shipment</button>
 </form>
 <div id="trkResult" class="app-result" aria-live="polite"></div>
 <p class="app-sub">Tracking usually appears 24 to 48 hours after dispatch. Need help? <a href="Contact-Us.html">Contact our team</a> with your order number.</p>
</section>
"""

TRK_SCRIPT = r"""
<script>
(function(){
  var SAMPLE={number:"RT209114500HK (sample)",header:{status:"In transit",destination:"United Kingdom",channel:"GBPOST"},events:[
    {description:"LONDON - UK: Arrived at delivery depot",time:"2026-10-18 09:12:04"},
    {description:"HONG KONG: Departed origin facility, in transit to destination",time:"2026-10-16 22:40:11"},
    {description:"SHENZHEN - CHINA: Departed facility in PFC",time:"2026-10-16 16:32:09"},
    {description:"SHENZHEN - CHINA: Shipment picked up",time:"2026-10-16 16:19:55"}
  ]};
  var badge=document.getElementById("apiBadge");
  var form=document.getElementById("trkForm");
  var input=document.getElementById("trkNo");
  var out=document.getElementById("trkResult");
  var LIVE=false;
  function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}

  fetch("/api/health").then(function(r){return r.json();}).then(function(h){
    LIVE=!!h.configured;badge.dataset.state=LIVE?"live":"preview";
    badge.textContent=LIVE?"Live tracking":"Preview, tracking not connected yet";
  }).catch(function(){badge.dataset.state="preview";badge.textContent="Preview";});

  function render(data,isSample){
    var ev=data.events||[];
    if(!ev.length){out.innerHTML='<div class="app-msg info">No tracking events found yet for <strong>'+esc(data.number)+'</strong>. Please check the number, or try again in a few hours.</div>';return;}
    var h="";
    if(isSample){h+='<div class="sample-banner"><span>⚠</span><span><strong>Sample timeline, not a live shipment.</strong> This shows the tracking layout. Live scan events appear here once the PFC API is connected.</span></div>';}
    h+='<div class="trk-wrap">';
    var hd=data.header;
    if(hd&&(hd.status||hd.destination||hd.channel)){
      h+='<div class="trk-header">';
      h+='<div><div class="k">Number</div><div class="v">'+esc(data.number)+'</div></div>';
      if(hd.status)h+='<div><div class="k">Status</div><div class="v">'+esc(hd.status)+'</div></div>';
      if(hd.destination)h+='<div><div class="k">Destination</div><div class="v">'+esc(hd.destination)+'</div></div>';
      if(hd.channel)h+='<div><div class="k">Service</div><div class="v">'+esc(hd.channel)+'</div></div>';
      h+='</div>';
    }
    h+='<ul class="trk-timeline">';
    ev.forEach(function(e){h+='<li><div class="desc">'+esc(e.description)+'</div>'+(e.time?'<div class="time">'+esc(e.time)+'</div>':'')+'</li>';});
    h+='</ul></div>';
    out.innerHTML=h;
  }

  function run(no){
    out.innerHTML='<div class="app-msg info"><span class="spin"></span>Looking up '+esc(no)+'</div>';
    fetch("/api/track?no="+encodeURIComponent(no)).then(function(r){
      return r.json().then(function(j){return {status:r.status,body:j};});
    }).then(function(res){
      if(res.status===200){render(res.body,false);return;}
      if(res.status===503){var s=JSON.parse(JSON.stringify(SAMPLE));render(s,true);return;}
      if(res.status===400){out.innerHTML='<div class="app-msg err">That does not look like a valid tracking or order number.</div>';return;}
      out.innerHTML='<div class="app-msg err">Tracking is temporarily unavailable. Please try again shortly or <a href="Contact-Us.html">contact us</a>.</div>';
    }).catch(function(){
      out.innerHTML='<div class="app-msg err">Could not reach the tracking service. Please try again shortly.</div>';
    });
  }

  form.addEventListener("submit",function(e){e.preventDefault();var no=input.value.trim();if(no)run(no);});
  var pre=new URLSearchParams(location.search).get("no");
  if(pre){input.value=pre;run(pre);}
})();
</script>
"""

PAGES = [
    dict(
        file="shipping-calculator.html",
        title="Shipping Rate Calculator | China Fulfillment",
        desc="Compare live shipping rates from our Shenzhen warehouse. Enter destination, weight and parcel size to see carrier services, delivery times and prices.",
        slug="shipping-calculator",
        og="china-to-amazon-fba-container-shipping-sea-freight.webp",
        hero=CALC_HERO, body=CALC_BODY, script=CALC_SCRIPT,
    ),
    dict(
        file="track-order.html",
        title="Track Your Shipment | China Fulfillment",
        desc="Track your China Fulfillment parcel or freight. Enter your tracking or order number to see the latest scan events and delivery status.",
        slug="track-order",
        og="china-to-amazon-fba-container-shipping-sea-freight.webp",
        hero=TRK_HERO, body=TRK_BODY, script=TRK_SCRIPT,
    ),
]

for p in PAGES:
    html = page(p["title"], p["desc"], p["slug"], p["og"], p["hero"], p["body"], p["script"])
    out = os.path.join(REPO, p["file"])
    open(out, "w", encoding="utf-8").write(html)
    print("wrote", p["file"], len(html), "bytes")
