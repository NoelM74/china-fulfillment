#!/usr/bin/env python3
"""
fix_canonical_urls.py — Normalise canonical + og:url across every page.

The server serves pages at their literal `.html` path (extension-less URLs 404).
Several canonicals/og:urls pointed at extension-less slugs that don't resolve,
and china-crowdfunding-fulfillment.html pointed at the wrong slug entirely.

This sets, for every page:
  canonical -> https://www.china-fulfillment.com/<filename>   (index -> /)
  og:url    -> same

Run once: python fix_canonical_urls.py
"""
import re
import pathlib

BASE = "https://www.china-fulfillment.com/"
root = pathlib.Path(__file__).parent

canon_re = re.compile(r'(<link\s+rel="canonical"\s+href=")([^"]*)(")', re.I)
ogurl_re = re.compile(r'(<meta\s+property="og:url"\s+content=")([^"]*)(")', re.I)

changed = []
for f in sorted(root.glob("*.html")):
    name = f.name
    target = BASE if name == "index.html" else BASE + name
    text = f.read_text(encoding="utf-8")
    orig = text

    def sub_canon(m):
        return m.group(1) + target + m.group(3)

    def sub_ogurl(m):
        return m.group(1) + target + m.group(3)

    text = canon_re.sub(sub_canon, text)
    text = ogurl_re.sub(sub_ogurl, text)

    if text != orig:
        f.write_text(text, encoding="utf-8")
        changed.append(name)

print(f"Updated {len(changed)} files:")
for c in changed:
    print("  " + c)
