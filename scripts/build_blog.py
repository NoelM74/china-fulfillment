import os
import glob
import yaml
import markdown
import re

TEMPLATE_PATH = "news-shopify-fulfillment-china.html"
DRAFTS_PATH = "data/content/drafts/*.md"

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
        cat = "Blog"
        if "fba" in slug or "amazon" in slug: cat = "Amazon FBA"
        elif "kickstarter" in slug: cat = "eCommerce"
        elif "shopify" in slug: cat = "eCommerce"
        
        new_html.append(f'''
<section class="art-hero">
  <div class="w">
    <div class="art-cat">{cat}</div>
    <h1>{title}</h1>
    <div class="art-meta">
      <span>By <strong>{meta.get("author", "China Fulfillment")}</strong></span>
      <span>Published May 16, 2026</span>
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
            "date": "May 2026"
        })

    # Now update blog.html
    with open("blog.html", "r", encoding="utf-8") as f:
        blog_html = f.read()
        
    grid_start_marker = '<div class="blog-grid" id="blogGrid">'
    parts = blog_html.split(grid_start_marker)
    
    if len(parts) == 2:
        new_links = []
        for p in posts_data:
            data_cat = "fba" if p['cat'] == "Amazon FBA" else "ecom"
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
