import os
import glob
import yaml
import markdown
import re
import json
import datetime
from html import escape


def build_faq_section(scripts):
    """Render a visible FAQ accordion from the post's FAQPage JSON-LD.

    Google requires FAQ rich-result content to be visible on the page, not
    schema-only. We mirror the existing site markup: a <section class="faq">
    with one <details>/<summary> per question, placed just before the footer.
    Returns "" if the draft has no FAQPage block.
    """
    for s in scripts:
        if '"FAQPage"' not in s:
            continue
        m = re.search(r'<script[^>]*>(.*?)</script>', s, flags=re.DOTALL)
        if not m:
            continue
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            return ""
        rows = []
        for qa in data.get("mainEntity", []):
            q = qa.get("name", "")
            a = qa.get("acceptedAnswer", {}).get("text", "")
            if not q or not a:
                continue
            rows.append(
                "    <details>\n"
                f"     <summary>{escape(q)}</summary>\n"
                f"     <p>{escape(a)}</p>\n"
                "    </details>"
            )
        if not rows:
            return ""
        return (
            '\n<section class="faq">\n  <div class="w">\n'
            "    <h2>Frequently Asked Questions</h2>\n"
            + "\n".join(rows)
            + "\n  </div>\n</section>\n"
        )
    return ""

TEMPLATE_PATH = "news-shopify-fulfillment-china.html"
DRAFTS_PATH = "data/content/drafts/*.md"

# Responsive image variants sit beside the original as name-<width>w.webp.
# They are referenced only when the files exist, so a post without variants
# builds exactly as before. Article images render at 90vw up to 844px and are
# capped at 760px above that, so nothing needs more than 1520px at 2x.
IMG_SIZES = "(max-width: 844px) 90vw, 760px"
VARIANT_WIDTHS = (600, 760, 900, 1140, 1520)


def srcset_attrs(src, original_width=None):
    """Return ' srcset="..." sizes="..."' for src, or '' if it has no variants."""
    if not (src.startswith("/images/") and src.endswith(".webp")):
        return ""
    base = src[: -len(".webp")]
    parts = ["%s-%dw.webp %dw" % (base, w, w) for w in VARIANT_WIDTHS
             if os.path.exists("%s-%dw.webp" % (base.lstrip("/"), w))]
    if not parts:
        return ""
    if original_width:
        parts.append("%s %dw" % (src, original_width))
    return ' srcset="%s" sizes="%s"' % (", ".join(parts), IMG_SIZES)

# Map a display category to the data-cat value blog.html's filters use.
CAT_TO_FILTER = {
    "Amazon FBA": "fba",
    "eCommerce": "ecom",
    "Crowdfunding": "ecom",
    "Shipping": "shipping",
    "Operations": "ops",
    "Blog": "ecom",
}


def fmt_dates(value):
    """Return (long, short) date strings from a frontmatter date.

    long  -> 'June 2, 2026'  (article hero byline)
    short -> 'June 2026'      (blog card)
    Falls back to the raw value if it cannot be parsed.
    """
    if isinstance(value, (datetime.date, datetime.datetime)):
        d = value
    else:
        try:
            d = datetime.datetime.strptime(str(value), "%Y-%m-%d")
        except (ValueError, TypeError):
            return str(value), str(value)
    return f"{d.strftime('%B')} {d.day}, {d.year}", f"{d.strftime('%B')} {d.year}"


def resolve_category(meta, slug):
    """Prefer an explicit frontmatter category; else infer from the slug."""
    cat = meta.get("category")
    if cat:
        return cat
    if "fba" in slug or "amazon" in slug:
        return "Amazon FBA"
    if "crowdfunding" in slug or "kickstarter" in slug or "indiegogo" in slug:
        return "Crowdfunding"
    if "de-minimis" in slug or "customs" in slug or "duty" in slug or "shipping" in slug:
        return "Shipping"
    if "kitting" in slug or "bundle" in slug or "packaging" in slug or "assembly" in slug:
        return "Operations"
    if "shopify" in slug or "d2c" in slug or "3pl" in slug or "ecommerce" in slug:
        return "eCommerce"
    return "Blog"

# ── Keep readers on the site: next step, related posts, inline quote form ──
#
# Each post ends with a "next step" box matched to its topic, then three
# related posts. Long posts also get a short quote form part-way down. The
# topic comes from an optional `next_step` frontmatter key, else from the
# category and slug. `related: [slug, ...]` in frontmatter pins related posts.

NEXT_STEPS = {
    "d2c": {
        "title": "Shipping D2C orders from China?",
        "text": "Send us your products, order volume and main markets and we will come back with a quote, usually within 24 hours. Pick and pack is $0.99 per order with standard packaging included.",
        "links": [("ecommerce-fulfillment.html", "eCommerce fulfillment"),
                  ("our-pricing.html", "See our pricing"),
                  ("express-international-shipping-china.html", "Shipping options")],
        "service": "ecommerce",
    },
    "us": {
        "title": "Selling to US customers from China?",
        "text": "Tell us your products and monthly orders and we will quote DDP delivery to the US, usually within 24 hours. Pick and pack is $0.99 per order with standard packaging included.",
        "links": [("china-to-us-fulfillment-2027.html", "China to US fulfillment"),
                  ("our-pricing.html", "See our pricing"),
                  ("ddp-shipping-from-china-explained-2026.html", "How DDP works")],
        "service": "ecommerce",
    },
    "dropship": {
        "title": "Ready to move on from dropshipping?",
        "text": "Hold your own stock in our Shenzhen warehouse and ship branded orders from there. Tell us what you sell and how many orders you ship, and we will tell you honestly whether it makes sense yet.",
        "links": [("dropshipping-fulfillment.html", "Dropshipping fulfillment"),
                  ("branded-packaging-kitting.html", "Branded packaging"),
                  ("our-pricing.html", "See our pricing")],
        "service": "ecommerce",
    },
    "crowdfunding": {
        "title": "Planning your reward shipping?",
        "text": "Send us your backer count, reward tiers and countries and we will quote pick, pack and DDP delivery, usually within 24 hours.",
        "links": [("china-crowdfunding-fulfillment.html", "Crowdfunding fulfillment"),
                  ("kickstarter-indiegogo-shipping-duties-2027.html", "Duties for backers"),
                  ("our-pricing.html", "See our pricing")],
        "service": "crowdfunding",
    },
    "fba": {
        "title": "Sending stock to Amazon from China?",
        "text": "Tell us your SKUs, carton count and target fulfillment centres and we will quote prep and freight, usually within 24 hours.",
        "links": [("amazon-fba-prep-china.html", "FBA prep in China"),
                  ("amazon-fba-consolidation.html", "FBA consolidation"),
                  ("fba-freight-from-china.html", "FBA freight")],
        "service": "fba",
    },
    "customs": {
        "title": "Need help with duty and customs?",
        "text": "We ship DDP, so duty is paid within the shipping price and your customer is never asked for it on delivery. Tell us your products and markets and we will quote.",
        "links": [("tariff-management-china.html", "Tariff and customs management"),
                  ("ddp-shipping-from-china-explained-2026.html", "How DDP works"),
                  ("our-pricing.html", "See our pricing")],
        "service": "tariff",
    },
    "ops": {
        "title": "Want this handled at the source?",
        "text": "Inspection, kitting, bundling and branded packing happen in our Shenzhen warehouse before anything ships. Tell us what you need and we will quote.",
        "links": [("branded-packaging-kitting.html", "Packaging and kitting"),
                  ("quality-control-fba-prep-china.html", "Quality control"),
                  ("our-pricing.html", "See our pricing")],
        "service": "ecommerce",
    },
}

SERVICE_OPTIONS = [
    ("ecommerce", "eCommerce Fulfillment (Shopify / D2C)"),
    ("crowdfunding", "Crowdfunding Fulfillment (Kickstarter / Indiegogo)"),
    ("fba", "Amazon FBA Consolidation"),
    ("tariff", "Tariff &amp; Customs Management"),
    ("freight", "International Freight Forwarding"),
    ("other", "Other / Not Sure Yet"),
]

VOLUME_OPTIONS = [
    ("starting", "Just starting out"),
    ("1-100", "1&#8211;100 orders / month"),
    ("100-500", "100&#8211;500 orders / month"),
    ("500-2000", "500&#8211;2,000 orders / month"),
    ("2000-10000", "2,000&#8211;10,000 orders / month"),
    ("10000+", "10,000+ orders / month"),
]

# Posts longer than this (words) get the inline quote form.
INLINE_FORM_MIN_WORDS = 1100

ARTICLE_EXTRA_CSS = """<style>/* blog: next step, related posts, inline quote form */
.nstep{margin:48px 0 8px;padding:28px 28px 24px;border:1px solid var(--bd);border-left:5px solid var(--ac);border-radius:12px;background:var(--off)}
.article .nstep h2{margin:0 0 8px;font-size:1.3rem}
.nstep p{margin-bottom:16px}
.nstep-links{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.article .nstep-links a{text-decoration:none;font-family:'Outfit',sans-serif;font-weight:700;font-size:.95rem;padding:10px 16px;border-radius:8px;border:1px solid var(--bd);background:#fff;color:var(--ink)}
.article .nstep-links a.nstep-main{background:var(--acd);border-color:var(--acd);color:#fff}
.article .nstep-links a:hover{border-color:var(--b2)}
.article .nstep-links a.nstep-main:hover{background:var(--acdh)}
.rel{margin:40px 0 0}
.article .rel h2{margin:0 0 16px;font-size:1.2rem}
.rel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.article .rel-card{display:flex;flex-direction:column;text-decoration:none;border:1px solid var(--bd);border-radius:12px;overflow:hidden;background:#fff;color:var(--ink);transition:box-shadow .16s,transform .16s}
.article .rel-card:hover{box-shadow:0 8px 28px rgba(13,33,68,.12);transform:translateY(-2px)}
.rel-card img{width:100%;aspect-ratio:2/1;object-fit:cover}
.rel-card span{display:block;padding:12px 14px 4px;font-size:.74rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--acd)}
.rel-card strong{display:block;padding:0 14px 16px;font-family:'Outfit',sans-serif;font-size:.98rem;line-height:1.3}
.qform{margin:40px 0;padding:26px 26px 22px;border:1px solid var(--bd);border-radius:14px;background:#fff;box-shadow:0 4px 24px rgba(0,0,0,.06)}
.article .qform h2{margin:0 0 6px;font-size:1.2rem}
.article .qform p{font-size:.95rem;margin-bottom:16px}
.qform .qrow{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
.qform label{display:block;font-size:.85rem;font-weight:700;color:var(--ink);margin-bottom:4px}
.qform input,.qform select,.qform textarea{width:100%;padding:10px 12px;border:1px solid var(--bd);border-radius:8px;font:inherit;font-size:.95rem;background:#fff;color:var(--ink)}
.qform textarea{min-height:80px;margin-bottom:12px}
.qform button{width:100%;padding:13px 20px;border:none;border-radius:8px;background:var(--acd);color:#fff;font-family:'Outfit',sans-serif;font-weight:700;font-size:1rem;cursor:pointer}
.qform button:hover{background:var(--acdh)}
.article .qform .qnote{font-size:.82rem;color:var(--mu);margin:10px 0 0;text-align:center}
@media(max-width:700px){.rel-grid{grid-template-columns:1fr}.qform .qrow{grid-template-columns:1fr}.rel-card img{aspect-ratio:3/1}}
</style>
"""


def topic_for(meta, slug, cat):
    """Pick the NEXT_STEPS key for a post."""
    t = meta.get("next_step")
    if t in NEXT_STEPS:
        return t
    if "dropship" in slug:
        return "dropship"
    if cat == "Crowdfunding" or "kickstarter" in slug or "crowdfunding" in slug:
        return "crowdfunding"
    if cat in ("Amazon FBA", "Amazon") or "fba" in slug or "amazon" in slug:
        return "fba"
    if cat == "Customs":
        return "customs"
    if cat == "Operations":
        return "ops"
    if "-us-" in slug or "usa" in slug:
        return "us"
    return "d2c"


def build_next_step(topic):
    n = NEXT_STEPS[topic]
    links = ['<a class="nstep-main" href="Contact-Us.html">Get a free quote &rarr;</a>']
    links += ['<a href="%s">%s</a>' % (h, t) for h, t in n["links"]]
    return ('\n<aside class="nstep" aria-label="Next step">\n'
            '  <h2>%s</h2>\n  <p>%s</p>\n  <div class="nstep-links">%s</div>\n</aside>\n'
            % (n["title"], n["text"], "".join(links)))


def build_inline_form(topic, slug):
    """A short quote form. Field names match the Contact-Us form so the same
    handler can take it; `source` records which post it came from."""
    selected = NEXT_STEPS[topic]["service"]
    services = "".join('<option value="%s"%s>%s</option>' % (v, " selected" if v == selected else "", t)
                       for v, t in SERVICE_OPTIONS)
    volumes = '<option value="" selected>Approximate volume</option>' + "".join(
        '<option value="%s">%s</option>' % (v, t) for v, t in VOLUME_OPTIONS)
    return (
        '\n<aside class="qform" aria-label="Get a quote">\n'
        '  <h2>Get a quote while you read</h2>\n'
        '  <p>Tell us what you sell and where your customers are. We reply with a quote, usually within 24 hours. No commitment.</p>\n'
        '  <form action="/Contact-Us.html" method="POST">\n'
        '    <input type="hidden" name="source" value="blog:%s"/>\n'
        '    <div class="qrow">\n'
        '      <div><label for="q-fname">First name *</label><input type="text" id="q-fname" name="fname" required autocomplete="given-name"/></div>\n'
        '      <div><label for="q-lname">Last name *</label><input type="text" id="q-lname" name="lname" required autocomplete="family-name"/></div>\n'
        '    </div>\n'
        '    <div class="qrow">\n'
        '      <div><label for="q-email">Email *</label><input type="email" id="q-email" name="email" required autocomplete="email" placeholder="you@company.com"/></div>\n'
        '      <div><label for="q-service">What do you need? *</label><select id="q-service" name="service" required>%s</select></div>\n'
        '    </div>\n'
        '    <div class="qrow">\n'
        '      <div><label for="q-volume">Monthly orders</label><select id="q-volume" name="volume">%s</select></div>\n'
        '      <div><label for="q-markets">Main markets</label><input type="text" id="q-markets" name="markets" placeholder="e.g. US, UK, EU"/></div>\n'
        '    </div>\n'
        '    <label for="q-message">What do you sell?</label>\n'
        '    <textarea id="q-message" name="message" rows="3" placeholder="Products, where they are made, and how you fulfil orders today."></textarea>\n'
        '    <button type="submit">Send my quote request &rarr;</button>\n'
        '    <p class="qnote">New customers: 30 days FREE storage when you ship in your first month.</p>\n'
        '  </form>\n'
        '</aside>\n' % (slug, services, volumes))


def insert_inline_form(body_html, form_html):
    """Place the form before the <h2> nearest the middle of the post, never
    before the first or after the last section."""
    starts = [m.start() for m in re.finditer(r"<h2[ >]", body_html)]
    if len(starts) < 4:
        return body_html
    mid = len(body_html) // 2
    pos = min(starts[1:-1], key=lambda p: abs(p - mid))
    return body_html[:pos] + form_html + body_html[pos:]


def word_count(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())


STOPWORDS = set("a an and the of for to from in on with vs or how what your you is are do does "
                "2025 2026 2027 china chinese guide".split())


def keyword_words(meta, slug):
    text = " ".join([slug.replace("-", " "), str(meta.get("target_keyword", ""))]
                    + [str(k) for k in meta.get("secondary_keywords", []) or []])
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOPWORDS and len(w) > 2}


def pick_related(post, posts, n=3):
    """Pinned `related` slugs first, then the posts sharing the most keyword
    words with this one, preferring the same category."""
    by_slug = {p["slug"]: p for p in posts}
    chosen = [by_slug[s] for s in post["related"] if s in by_slug and s != post["slug"]]
    if len(chosen) < n:
        scored = []
        for p in posts:
            if p["slug"] == post["slug"] or p in chosen:
                continue
            score = len(post["words"] & p["words"]) + (3 if p["cat"] == post["cat"] else 0)
            scored.append((score, p["slug"], p))
        scored.sort(key=lambda x: (-x[0], x[1]))
        chosen += [p for _, _, p in scored[: n - len(chosen)]]
    return chosen[:n]


def build_related(related):
    cards = []
    for p in related:
        cards.append(
            '<a class="rel-card" href="%s.html"><img src="%s" alt="" width="400" height="200" loading="lazy" decoding="async"/>'
            '<span>%s</span><strong>%s</strong></a>' % (p["slug"], p["img"], p["cat"], escape(p["title"])))
    return ('\n<div class="rel" role="navigation" aria-label="Related posts">\n  <h2>Keep reading</h2>\n  <div class="rel-grid">%s</div>\n</div>\n'
            % "".join(cards))


def extract_template_parts():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Split to get head, breadcrumb, footer
    
    # 1. Head top
    head_top = html.split('<title>')[0]
    
    # 2. Schema section
    nav_to_bread = html.split('</script>\n\n<link rel="preconnect"')[1].split('<div class="bread">')[0]
    nav_to_bread = '</script>\n<link rel="preconnect"' + nav_to_bread
    
    # 3. Footer
    footer = '<div class="ctaf">' + html.split('<div class="ctaf">')[1]
    
    return head_top, nav_to_bread, footer

def process_markdown(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract frontmatter
    parts = content.split("---")
    if len(parts) < 3: return None
    
    frontmatter_str = parts[1]
    body = "---".join(parts[2:])
    
    meta = yaml.safe_load(frontmatter_str)
    
    # Extract scripts from body
    scripts = []
    def script_replacer(match):
        scripts.append(match.group(0))
        return ""
    
    body_no_scripts = re.sub(r'<script.*?</script>', script_replacer, body, flags=re.DOTALL)
    
    # Extract Title (H1) and remove from body
    h1_match = re.search(r'^#\s+(.+)$', body_no_scripts, flags=re.MULTILINE)
    title = meta.get('title', h1_match.group(1) if h1_match else "")
    
    # Remove H1 from body
    if h1_match:
        body_no_scripts = body_no_scripts.replace(h1_match.group(0), '', 1)
        
    # Remove the first image (which is the hero image)
    img_match = re.search(r'^!\[.*?\]\(.*?\)$', body_no_scripts, flags=re.MULTILINE)
    if img_match:
        body_no_scripts = body_no_scripts.replace(img_match.group(0), '', 1)
    
    # The new articles already have title in frontmatter, let's use that.
    # Convert body to HTML
    body_html = markdown.markdown(body_no_scripts, extensions=['tables'])

    # Wide markdown tables must scroll inside their own container rather than
    # pushing the whole page sideways on a phone.
    body_html = body_html.replace('<table>', '<div class="tw"><table>')
    body_html = body_html.replace('</table>', '</table></div>')

    # In-body images need intrinsic dimensions or they cause layout shift.
    # Infographics are generated 4:5 portrait; anything else keeps its ratio
    # declared at the width the article column actually renders.
    def _size_img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        src = src.group(1) if src else ""
        alt = alt.group(1) if alt else ""
        w, h = (1200, 1500) if 'infographic' in src else (1200, 675)
        extra = srcset_attrs(src, 1200 if 'infographic' in src else None)
        return ('<img src="%s"%s alt="%s" width="%d" height="%d" '
                'loading="lazy" decoding="async"/>' % (src, extra, alt, w, h))

    body_html = re.sub(r'<img\b[^>]*/?>', _size_img, body_html)
    
    # In markdown, image urls might be /images/blog/...
    # They should be fine if we moved them.
    
    return meta, scripts, title, body_html

def build_pages():
    head_top, nav_to_bread, footer = extract_template_parts()
    
    drafts = sorted(glob.glob(DRAFTS_PATH))
    posts_data = []

    # First pass: read every draft so each post can link to related ones.
    parsed = []
    for draft in drafts:
        res = process_markdown(draft)
        if not res: continue
        meta, scripts, title, body_html = res
        slug = meta.get('slug', os.path.basename(draft).replace('.md', ''))
        parsed.append({
            "meta": meta, "scripts": scripts, "title": title, "body": body_html,
            "slug": slug, "cat": resolve_category(meta, slug),
            "img": meta.get("images", {}).get("hero", ""),
            "related": meta.get("related", []) or [], "words": keyword_words(meta, slug),
        })

    for post in parsed:
        meta, scripts, title, body_html = post["meta"], post["scripts"], post["title"], post["body"]
        slug = post["slug"]
        topic = topic_for(meta, slug, post["cat"])
        if word_count(body_html) >= INLINE_FORM_MIN_WORDS:
            body_html = insert_inline_form(body_html, build_inline_form(topic, slug))
        body_html += build_next_step(topic) + build_related(pick_related(post, parsed))
        
        # SERP <title> can differ from the on-page H1: use an optional shorter
        # `seo_title` (<=60 chars, keyword-first) when present, else the H1 title.
        seo_title = meta.get('seo_title', title)

        # Build new HTML
        new_html = []
        new_html.append(head_top)
        new_html.append(f'<title>{seo_title}</title>\n')
        new_html.append(f'<meta name="description" content="{meta.get("meta_description", "")}"/>\n')
        new_html.append(f'<link rel="canonical" href="https://www.china-fulfillment.com/{slug}.html"/>\n')
        new_html.append(f'<meta property="og:title" content="{title}"/>\n')
        new_html.append(f'<meta property="og:description" content="{meta.get("meta_description", "")}"/>\n')
        new_html.append(f'<meta property="og:image" content="https://www.china-fulfillment.com{meta.get("og_image", "")}"/>\n')
        new_html.append(f'<meta property="og:type" content="article"/>\n')
        new_html.append(f'<meta name="twitter:card" content="summary_large_image"/>\n')
        new_html.append(f'<meta name="twitter:image" content="https://www.china-fulfillment.com{meta.get("og_image", "")}"/>\n')
        new_html.append(f'<meta property="og:url" content="https://www.china-fulfillment.com/{slug}.html"/>\n')
        new_html.append(f'<meta property="article:published_time" content="{meta.get("last_updated", "")}"/>\n')
        
        for script in scripts:
            new_html.append(script + "\n")
            
        new_html.append(nav_to_bread.replace('</head>', ARTICLE_EXTRA_CSS + '</head>', 1))
        new_html.append(f'<div class="bread"><a href="/">Home</a><span>›</span><a href="blog.html">Blog</a><span>›</span>{title}</div>\n')
        
        # Hero Section
        cat = resolve_category(meta, slug)
        long_date, short_date = fmt_dates(meta.get("last_updated", ""))
        hero_src = meta.get("images", {}).get("hero", "")
        hero_srcset = srcset_attrs(hero_src)

        new_html.append(f'''
<section class="art-hero">
  <div class="w">
    <div class="art-cat">{cat}</div>
    <h1>{title}</h1>
    <div class="art-meta">
      <span>By <strong>{meta.get("author", "China Fulfillment")}</strong></span>
      <span>Published {long_date}</span>
    </div>
    <div class="art-hero-img">
      <img src="{hero_src}"{hero_srcset} alt="{meta.get("images", {}).get("hero_alt", "")}" width="1200" height="440" loading="eager" fetchpriority="high" decoding="async"/>
    </div>
  </div>
</section>

<div class="article">
  <div class="w">
    {body_html}
  </div>
</div>
''')
        # We need to remove the <div class="faq"> section from the footer since the new body_html contains the FAQs if any
        # Actually the footer variable contains <div class="ctaf"> ... </div> <div class="faq"> ... </div> <footer> ...
        footer_parts = footer.split('<div class="faq">')
        if len(footer_parts) > 1:
            # Reconstruct footer without the hardcoded FAQ
            clean_footer = footer_parts[0] + "<footer>" + footer_parts[1].split('<footer>')[1]
        else:
            clean_footer = footer

        # Inject a visible, page-specific FAQ accordion (from the FAQPage
        # JSON-LD) just before the footer, so the structured data is backed
        # by visible content and eligible for FAQ rich results.
        faq_html = build_faq_section(scripts)
        if faq_html:
            clean_footer = clean_footer.replace("<footer>", faq_html + "<footer>", 1)

        new_html.append(clean_footer)
        
        out_filename = f"{slug}.html"
        with open(out_filename, "w", encoding="utf-8") as f:
            f.write("".join(new_html))
            
        print(f"Built {out_filename}")
        
        posts_data.append({
            "title": title,
            "desc": meta.get("meta_description", ""),
            "slug": slug,
            "img": meta.get("images", {}).get("hero", ""),
            "cat": cat,
            "date": short_date
        })

    # Now update blog.html
    with open("blog.html", "r", encoding="utf-8") as f:
        blog_html = f.read()
        
    grid_start_marker = '<div class="blog-grid" id="blogGrid">'
    parts = blog_html.split(grid_start_marker)
    
    if len(parts) == 2:
        new_links = []
        for p in posts_data:
            # Idempotency: never add a card for a post already in the grid.
            if f'href="{p["slug"]}.html"' in blog_html:
                print(f"Skipped blog.html card (already present): {p['slug']}")
                continue
            data_cat = CAT_TO_FILTER.get(p['cat'], "ecom")
            new_links.append(f'''
      <!-- NEW: {p['title']} -->
      <a href="{p['slug']}.html" class="post" data-cat="{data_cat}">
        <div class="post-img"><img src="{p['img']}" alt="{p['title']}" width="400" height="200" loading="lazy" decoding="async"/></div>
        <div class="post-body">
          <div class="post-cat">{p['cat']}</div>
          <h3>{p['title']}</h3>
          <p>{p['desc'][:120]}...</p>
          <div class="post-meta"><span>{p['date']}</span><span class="post-read">Read &rarr;</span></div>
        </div>
      </a>
''')
        
        new_blog_html = parts[0] + grid_start_marker + "\n" + "".join(new_links) + parts[1]
        with open("blog.html", "w", encoding="utf-8") as f:
            f.write(new_blog_html)
        print("Updated blog.html")

if __name__ == "__main__":
    build_pages()
