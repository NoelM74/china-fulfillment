#!/usr/bin/env python3
"""
apply_hreflang_author.py — Add hreflang self-references and an author meta
to every indexable page (skips noindex login/register).

- hreflang en + x-default pointing at the page's own canonical (protects against
  future country expansion; satisfies the audit's hreflang gap).
- <meta name="author"> for E-E-A-T / AEO citation signal.
Idempotent. Run once.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
SKIP = {"login.html", "register.html"}
AUTHOR = '<meta name="author" content="China Fulfillment International — Shenzhen 3PL since 2010"/>'
canon_re = re.compile(r'(<link rel="canonical" href="([^"]+)"\s*/?>)')

changed = []
for f in sorted(ROOT.glob("*.html")):
    if f.name in SKIP:
        continue
    t = f.read_text(encoding="utf-8")
    if "hreflang" in t and 'name="author"' in t:
        continue
    m = canon_re.search(t)
    if not m:
        print("no canonical, skipped:", f.name)
        continue
    canon_tag, url = m.group(1), m.group(2)
    additions = canon_tag
    if "hreflang" not in t:
        additions += (
            f'\n<link rel="alternate" hreflang="en" href="{url}"/>'
            f'\n<link rel="alternate" hreflang="x-default" href="{url}"/>'
        )
    if 'name="author"' not in t:
        additions += "\n" + AUTHOR
    t = t.replace(canon_tag, additions, 1)
    f.write_text(t, encoding="utf-8")
    changed.append(f.name)

print(f"Updated {len(changed)} pages")
