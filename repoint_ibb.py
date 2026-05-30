#!/usr/bin/env python3
"""
repoint_ibb.py — rewrite every i.ibb.co URL in the HTML to its local WebP
(from ibb_map.json). Relative paths for <img>/CSS/preload; absolute prod
URLs for social/SEO metadata (og:image, twitter:image, JSON-LD image/logo/url).
Also drops now-useless <link rel=preconnect href=...i.ibb.co>.
"""
import json, glob, re, pathlib

ROOT = pathlib.Path(__file__).parent
PROD = "https://www.china-fulfillment.com/"
mapping = json.load(open(ROOT / "ibb_map.json"))

# longest URLs first so no prefix-shadowing during replace
items = sorted(mapping.items(), key=lambda kv: -len(kv[0]))

total_files = 0
total_refs = 0
for f in glob.glob(str(ROOT / "*.html")):
    t = open(f, encoding="utf-8").read()
    o = t
    n = o.count("i.ibb.co")
    for url, rel in items:
        if url in t:
            t = t.replace(url, rel)
    # promote metadata refs to absolute prod URLs
    t = t.replace('content="images/site/', f'content="{PROD}images/site/')
    t = t.replace(':"images/site/', f':"{PROD}images/site/')
    t = t.replace(': "images/site/', f': "{PROD}images/site/')
    # drop dead preconnect to i.ibb.co
    t = re.sub(r'\s*<link rel="preconnect" href="https://i\.ibb\.co"[^>]*>\n?', '\n', t)
    if t != o:
        open(f, "w", encoding="utf-8").write(t)
        total_files += 1
        total_refs += n
        print(f"{pathlib.Path(f).name}: {n} refs")

print(f"\n{total_files} files updated, {total_refs} ibb refs replaced")
