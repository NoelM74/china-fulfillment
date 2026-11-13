"""Build the image sitemap and the sitemap index.

    python3 scripts/build_sitemaps.py

sitemap.xml stays the hand-kept list of pages (one entry per page, with
lastmod and one lead image). This script reads it and writes:

- sitemap-images.xml: every content image on every page in sitemap.xml, with
  its alt text as the title. Logos and the "Keep reading" cards (which show
  other posts' heroes) are left out, and so are the post cards on blog.html.
- sitemap-index.xml: points to both, so Google Search Console and Bing
  Webmaster Tools need only one URL.

Run it after adding or removing pages in sitemap.xml, or after a blog build.
"""
import datetime
import os
import re
from html import escape, unescape

SITE = "https://www.china-fulfillment.com/"
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
SKIP = ("new-cf-logo", "logo.png", "favicon")


def attr(tag, name):
    m = re.search(r'\b%s="([^"]*)"' % name, tag)
    return unescape(m.group(1)) if m else ""


def absolute(src):
    src = src.strip()
    if src.startswith("http"):
        return src if src.startswith(SITE) else None
    return SITE + src.lstrip("/")


def page_images(path):
    html = open(path, encoding="utf-8").read()
    # Drop blocks that show other pages' images.
    html = re.sub(r'<a class="rel-card".*?</a>', "", html, flags=re.S)
    if path == "blog.html":
        html = re.sub(r'<a href="[^"]+" class="post".*?</a>', "", html, flags=re.S)
    found = {}
    og = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    for tag in IMG_RE.findall(html):
        src = attr(tag, "src")
        if not src or src.startswith("data:") or any(s in src for s in SKIP):
            continue
        url = absolute(src)
        if url and url not in found:
            found[url] = attr(tag, "alt")
    if og:
        url = absolute(og.group(1))
        if url and url not in found and not any(s in url for s in SKIP):
            found[url] = ""
    # Only list files that exist in the repo.
    return {u: a for u, a in found.items() if os.path.exists(u[len(SITE):].split("?")[0])}


def main():
    sm = open("sitemap.xml", encoding="utf-8").read()
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    pages = images = 0
    for loc in locs:
        rel = loc[len(SITE):] or "index.html"
        if not os.path.exists(rel):
            print("skipped (no file):", loc)
            continue
        imgs = page_images(rel)
        if not imgs:
            continue
        pages += 1
        out.append("  <url>\n    <loc>%s</loc>" % escape(loc))
        for url, alt in imgs.items():
            images += 1
            out.append("    <image:image>\n      <image:loc>%s</image:loc>" % escape(url))
            if alt:
                out.append("      <image:title>%s</image:title>" % escape(alt))
            out.append("    </image:image>")
        out.append("  </url>")
    out.append("</urlset>\n")
    open("sitemap-images.xml", "w", encoding="utf-8").write("\n".join(out))

    today = datetime.date.today().isoformat()
    index = """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>%ssitemap.xml</loc>
    <lastmod>%s</lastmod>
  </sitemap>
  <sitemap>
    <loc>%ssitemap-images.xml</loc>
    <lastmod>%s</lastmod>
  </sitemap>
</sitemapindex>
""" % (SITE, today, SITE, today)
    open("sitemap-index.xml", "w", encoding="utf-8").write(index)
    print("sitemap-images.xml: %d pages, %d images" % (pages, images))
    print("sitemap-index.xml: 2 sitemaps")


if __name__ == "__main__":
    main()
