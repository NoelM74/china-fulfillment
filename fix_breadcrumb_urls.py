#!/usr/bin/env python3
"""
fix_breadcrumb_urls.py — Align BreadcrumbList item URLs with served .html paths.

BreadcrumbList JSON-LD pointed at extension-less slugs that 404, and the
crowdfunding page's breadcrumb pointed at the wrong slug (/china-fulfillment).
Mismatched breadcrumb item URLs weaken the breadcrumb rich result.

Rule: any breadcrumb item URL with a non-empty path and no .html suffix gets
.html appended. The home item (bare domain + trailing slash) is left alone.
The crowdfunding slug is corrected explicitly. Run once.
"""
import re
import pathlib

root = pathlib.Path(__file__).parent
# match "item":"https://www.china-fulfillment.com/<slug>"  (slug = no slash, no dot)
item_re = re.compile(
    r'("item":"https://www\.china-fulfillment\.com/)([A-Za-z0-9-]+)(")'
)

changed = []
for f in sorted(root.glob("*.html")):
    text = f.read_text(encoding="utf-8")
    orig = text

    # Fix the wrong crowdfunding breadcrumb slug first (only matches in that file).
    text = text.replace(
        '"name":"Crowdfunding Fulfillment from China","item":"https://www.china-fulfillment.com/china-fulfillment"',
        '"name":"Crowdfunding Fulfillment from China","item":"https://www.china-fulfillment.com/china-crowdfunding-fulfillment.html"',
    )

    # Append .html to any remaining extension-less breadcrumb item paths.
    text = item_re.sub(lambda m: m.group(1) + m.group(2) + ".html" + m.group(3), text)

    if text != orig:
        f.write_text(text, encoding="utf-8")
        changed.append(f.name)

print(f"Updated {len(changed)} files:")
for c in changed:
    print("  " + c)
