#!/usr/bin/env python3
"""
apply_mobile_readability.py — Bump the mobile type scale across every page.

The design uses a lot of small rem-based text (.82-.93rem ~= 13-15px) which is
hard to read on a phone. Raising the root font-size on small screens scales all
rem-based copy up proportionally (body, FAQ, cards, footer, buttons) without
touching desktop. Inserted just before </style> so it wins the cascade.
Idempotent via a marker. Run once.
"""
import pathlib

MARKER = "/* mobile-readability */"
SNIPPET = (
    MARKER
    + "@media(max-width:768px){html{font-size:17.5px}}"
    + "@media(max-width:360px){html{font-size:16.5px}}"
)

root = pathlib.Path(__file__).parent
changed = []
for f in sorted(root.glob("*.html")):
    t = f.read_text(encoding="utf-8")
    if MARKER in t or "</style>" not in t:
        continue
    # Insert before the FIRST closing style tag.
    t = t.replace("</style>", SNIPPET + "\n</style>", 1)
    f.write_text(t, encoding="utf-8")
    changed.append(f.name)

print(f"Updated {len(changed)} pages")
