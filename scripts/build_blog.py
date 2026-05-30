import os
import glob
import yaml
import markdown
import re
import datetime

TEMPLATE_PATH = "news-shopify-fulfillment-china.html"
DRAFTS_PATH = "data/content/drafts/*.md"

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
    
    # In markdown, image urls might be /images/blog/...
    # They should be fine if we moved them.
    
    return meta, scripts, title, body_html

def build_pages():
    head_top, nav_to_bread, footer = extract_template_parts()
    
    drafts = glob.glob(DRAFTS_PATH)
    posts_data = []
    
    for draft in drafts:
        res = process_markdown(draft)
        if not res: continue
        meta, scripts, title, body_html = res
        
        slug = meta.get('slug', os.path.basename(draft).replace('.md', ''))
        
        # Build new HTML
        new_html = []
        new_html.append(head_top)
        new_html.append(f'<title>{title}</title>\n')
        new_html.append(f'<meta name="description" content="{meta.get("meta_description", "")}"/>\n')
        new_html.append(f'<link rel="canonical" href="https://www.china-fulfillment.com/{slug}.html"/>\n')
        new_html.append(f'<meta property="og:title" content="{title}"/>\n')
        new_html.append(f'<meta property="og:description" content="{meta.get("meta_description", "")}"/>\n')
        new_html.append(f'<meta property="og:image" content="https://www.china-fulfillment.com{meta.get("og_image", "")}"/>\n')
        new_html.append(f'<meta property="og:type" content="article"/>\n')
        new_html.append(f'<meta property="og:url" content="https://www.china-fulfillment.com/{slug}.html"/>\n')
        new_html.append(f'<meta property="article:published_time" content="{meta.get("last_updated", "")}"/>\n')
        
        for script in scripts:
            new_html.append(script + "\n")
            
        new_html.append(nav_to_bread)
        new_html.append(f'<div class="bread"><a href="/">Home</a><span>›</span><a href="blog.html">Blog</a><span>›</span>{title}</div>\n')
        
        # Hero Section
        cat = resolve_category(meta, slug)
        long_date, short_date = fmt_dates(meta.get("last_updated", ""))

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
      <img src="{meta.get("images", {}).get("hero", "")}" alt="{meta.get("images", {}).get("hero_alt", "")}" width="1200" height="440" loading="eager" decoding="async"/>
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
