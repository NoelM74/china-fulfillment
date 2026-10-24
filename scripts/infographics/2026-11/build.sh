#!/usr/bin/env bash
# Rebuild the November 2026 infographics from source.
#   bash scripts/infographics/2026-11/build.sh
# Edit make_infographics.py (wording, figures), then run this. Output goes to images/blog/
# as name.webp (1200x1500) plus -600w and -900w copies, the sizes build_blog.py looks for.
# Needs: python3, node with Playwright (/opt/node22), ImageMagick with WebP.
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/../../.." && pwd)"
cd "$DIR"
# Outfit (the site font, SIL Open Font License) is fetched from Google Fonts, not committed.
if [ ! -f outfit-local.css ]; then
  mkdir -p fonts
  UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
  curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800;900&display=swap" -o outfit.css
  i=0; cp outfit.css outfit-local.css
  for u in $(grep -o "https://fonts.gstatic.com[^)]*" outfit.css | sort -u); do
    i=$((i+1)); curl -s -o "fonts/outfit$i.woff2" "$u"; sed -i "s#$u#fonts/outfit$i.woff2#g" outfit-local.css
  done
fi
python3 make_infographics.py
NODE="$(command -v node || echo /opt/node22/bin/node)"
"$NODE" render.mjs "$DIR"
for n in infographic-sea-freight-fba-timeline infographic-lcl-vs-fcl-break-even infographic-china-europe-four-modes infographic-ieepa-refund-who-gets-paid; do
  convert "$n.png" -quality 88 -define webp:method=6 "$REPO/images/blog/$n.webp"
  convert "$n.png" -resize 600x -quality 86 -define webp:method=6 "$REPO/images/blog/$n-600w.webp"
  convert "$n.png" -resize 900x -quality 86 -define webp:method=6 "$REPO/images/blog/$n-900w.webp"
  echo "wrote images/blog/$n.webp (+600w, 900w)"
done
