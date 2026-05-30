#!/usr/bin/env python3
"""
apply_service_byline.py — Add a visible 'Updated <date> · By ...' byline under
the hero H1 on the money/service pages (E-E-A-T + AEO freshness signal).
Idempotent. Run once.
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
SERVICE = [
    "ecommerce-fulfillment.html", "china-crowdfunding-fulfillment.html",
    "amazon-fba-consolidation.html", "amazon-fba-prep-china.html",
    "amazon-fulfillment.html", "china-consolidation.html",
    "quality-control-fba-prep-china.html", "supplier-management-china.html",
    "tariff-management-china.html", "international-freight-forwarding-china.html",
    "express-international-shipping.html", "express-international-shipping-china.html",
    "dropshipping-fulfillment.html", "branded-packaging-kitting.html",
    "cod-service.html",
]
CSS = (".hbyline{color:rgba(255,255,255,.62);font-size:.86rem;font-weight:500;"
       "font-family:'Outfit',sans-serif;margin:2px 0 20px;letter-spacing:.01em}"
       ".hbyline strong{color:rgba(255,255,255,.82);font-weight:600}")
BYLINE = ('<div class="hbyline">Updated <time datetime="2026-05-30">May 2026</time> '
          '&middot; By <strong>China Fulfillment International</strong>, Shenzhen</div>')

changed = []
for name in SERVICE:
    f = ROOT / name
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    if "hbyline" in t:
        continue
    if "</h1>" not in t or "</style>" not in t:
        print("anchor missing:", name); continue
    t = t.replace("</style>", CSS + "\n</style>", 1)
    t = t.replace("</h1>", "</h1>\n    " + BYLINE, 1)  # first h1 = hero h1
    f.write_text(t, encoding="utf-8")
    changed.append(name)

print(f"Updated {len(changed)} service pages")
for c in changed:
    print("  " + c)
