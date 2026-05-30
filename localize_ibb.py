#!/usr/bin/env python3
"""
localize_ibb.py — download every i.ibb.co image referenced in the site,
convert to right-sized WebP, store under images/site/, and emit a
url -> local-path map (ibb_map.json). Resumable: skips already-downloaded.

Photos: cap 1200px wide, q80. Transparent PNGs (logo/icons): keep alpha, q90.
Run once for download+convert; repointing is done by a separate step that
reads ibb_map.json.
"""
import re, json, glob, pathlib, urllib.request, io
from PIL import Image

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "images" / "site"
OUT.mkdir(parents=True, exist_ok=True)

URL_RE = re.compile(r'https://i\.ibb\.co/[A-Za-z0-9]+/[A-Za-z0-9._-]+')

# collect unique URLs
urls = set()
for f in glob.glob(str(ROOT / "*.html")):
    urls |= set(URL_RE.findall(open(f, encoding="utf-8").read()))
urls = sorted(urls)
print(f"{len(urls)} unique i.ibb.co URLs found\n")

def base_name(url):
    base = url.rsplit("/", 1)[1]
    stem = re.sub(r"\.(png|jpe?g|webp)$", "", base, flags=re.I).lower()
    return stem + ".webp"

# resolve final local name per url, disambiguating collisions by ibb id
grouped = {}
for u in urls:
    grouped.setdefault(base_name(u), []).append(u)
name_for = {}
for n, us in grouped.items():
    if len(us) == 1:
        name_for[us[0]] = n
    else:
        for u in us:
            ibb_id = u.split("/")[-2]
            name_for[u] = re.sub(r"\.webp$", f"-{ibb_id}.webp", n)

mapping = {}
failed = []
for u in urls:
    n = name_for[u]
    dst = OUT / n
    mapping[u] = f"images/site/{n}"
    if dst.exists() and dst.stat().st_size > 0:
        continue
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=30).read()
        im = Image.open(io.BytesIO(raw))
        has_alpha = im.mode in ("RGBA", "LA", "P") and (
            im.mode != "P" or "transparency" in im.info)
        if im.mode == "P":
            im = im.convert("RGBA" if has_alpha else "RGB")
        elif im.mode == "LA":
            im = im.convert("RGBA")
        elif im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        if im.width > 1200:
            h = round(im.height * 1200 / im.width)
            im = im.resize((1200, h), Image.LANCZOS)
        q = 90 if has_alpha else 80
        im.save(dst, "WEBP", quality=q, method=6)
        print(f"OK   {len(raw)//1024:5d}KB -> {dst.stat().st_size//1024:4d}KB  {n}")
    except Exception as e:
        failed.append((u, str(e)))
        print(f"FAIL {u}  ({e})")

json.dump(mapping, open(ROOT / "ibb_map.json", "w"), indent=1)
print(f"\nmapped {len(mapping)} urls, {len(failed)} failed")
if failed:
    print("FAILURES:")
    for u, e in failed:
        print(" ", u, e)
