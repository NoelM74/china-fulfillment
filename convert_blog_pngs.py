#!/usr/bin/env python3
"""
convert_blog_pngs.py — one-time: convert the 6 heavy local blog PNGs to WebP.
Heroes cap at 1200px wide (photos, q82). Infographics keep text crisp (q88,
cap 1100px). Prints before/after sizes. Does NOT delete originals (done after
HTML is repointed and verified).
"""
import pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).parent / "images" / "blog"

# (filename, max_width, quality)
JOBS = [
    ("hero-3pl-vs-self-fulfilling.png", 1200, 82),
    ("hero-fba-prep-rejections.png",    1200, 82),
    ("hero-kickstarter-fulfillment.png",1200, 82),
    ("infographic-fba-checklist.png",   1100, 88),
    ("infographic-kickstarter-flow.png",1100, 88),
    ("infographic-3pl-flow.png",        1100, 88),
]

total_before = total_after = 0
for name, maxw, q in JOBS:
    src = ROOT / name
    if not src.exists():
        print("MISSING:", name); continue
    dst = src.with_suffix(".webp")
    im = Image.open(src)
    if im.mode in ("P", "LA"):
        im = im.convert("RGBA")
    if im.width > maxw:
        h = round(im.height * maxw / im.width)
        im = im.resize((maxw, h), Image.LANCZOS)
    im.save(dst, "WEBP", quality=q, method=6)
    b = src.stat().st_size; a = dst.stat().st_size
    total_before += b; total_after += a
    print(f"{name:38s} {b//1024:4d}KB -> {a//1024:4d}KB  ({dst.name})")

print(f"\nTOTAL {total_before//1024}KB -> {total_after//1024}KB "
      f"({100 - total_after*100//total_before}% smaller)")
