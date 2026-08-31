# china-fulfillment.com

Static HTML marketing site for China Fulfillment International, a Shenzhen 3PL. No framework, no bundler. Pages are plain `.html` files at the repository root, served as-is.

---

## ⚠️ Read this before running the build

`scripts/build_blog.py` **regenerates every blog post from its draft, every time it runs.** It is not incremental and it has no diffing. Two consequences bite repeatedly:

1. **Any edit made directly to a generated `.html` post is destroyed.** Edit the draft in `data/content/drafts/`, never the built page.
2. **Held posts come back to life.** The build re-adds their `blog.html` cards and strips their `noindex` tag, because the drafts do not contain it.

**If you are holding posts, re-apply the hold after every build.** See *Holding a post* below.

Hand-built pages, meaning service pages and anything not generated from a draft, are safe **only if no matching draft exists**. When a hand-built page shares a slug with a draft, the build overwrites the hand-built page. That is why `hs-code-classification-tariff-engineering.md` lives in `data/content/pages/` with a `.source.md` suffix rather than in `drafts/`: it keeps the source in the repo while keeping it out of the build's glob.

---

## Building blog posts

```bash
pip install markdown pyyaml
python3 scripts/build_blog.py
```

| | |
|---|---|
| Reads | `data/content/drafts/*.md` |
| Template | `news-shopify-fulfillment-china.html` |
| Writes | `<slug>.html` at the repository root |
| Also writes | `blog.html`, adding a card for any post that lacks one |

A draft is YAML frontmatter, then `Article` and `FAQPage` JSON-LD in `<script>` tags, then an `# H1`, a hero image, a `> **Quick answer:**` blockquote, and the body.

The build derives the visible FAQ accordion from the `FAQPage` JSON-LD, so **do not hand-write `<details>` blocks** in a draft. Add the question to the schema and the accordion follows. Schema and visible questions must stay one to one.

The build also wraps every `<table>` in `<div class="tw">` for mobile scrolling, and adds `width`, `height`, `loading="lazy"` and `decoding="async"` to every `<img>`. It infers dimensions from the filename: anything containing `infographic` is treated as 1200×1500, everything else as 1200×675.

### Things the build does not do

- Add entries to `sitemap.xml`. Do that by hand.
- Remove a card from `blog.html`. It only ever adds.
- Validate that referenced images exist.

---

## Holding a post

Used when a post is finished but its images have not been generated yet. A post with a broken hero is worse than no post.

Three things, all required:

1. `<meta name="robots" content="noindex,nofollow"/><!-- UNPUBLISHED: remove this line to publish -->` immediately after the canonical link
2. No entry in `sitemap.xml`
3. No card in `blog.html`

To publish, reverse all three.

**Removing a card from `blog.html` by regex is how this file gets broken.** A card is an HTML comment `<!-- NEW: Title -->` followed by `<a href="slug.html" class="post" ...>…</a>`. Anchors do not nest here, so the first `</a>` after the opening tag is the closer. Anything looser will eat the `<div class="blog-grid" id="blogGrid">` container and silently unbalance the file. After any card edit, check that div and anchor open and close counts match.

Easiest safe route: if `blog.html` at `HEAD` already lacks the cards, `git checkout blog.html` rather than editing it.

---

## Images

**`IMAGE-STYLE-GUIDE.md` is the standing rule set. Read it before writing any brief or generating anything.** It covers who appears in warehouse photos, what the real facility looks like, how the logo may be used, and the correct brand hex values.

Per-batch prompts live in `IMAGE-BRIEFS-tierN.md`. Where a brief and the style guide disagree, the style guide wins.

| | |
|---|---|
| Format | `.webp`, sRGB |
| Blog hero | generate 2400×880, displayed 1200×440 |
| Infographic | 1200×1500 |
| Post images | `images/blog/` |
| Page and service images | `images/site/` |

Filenames are referenced literally in the HTML. A mismatch is a broken image, not a fallback.

---

## Accessibility invariants

The site had 490 WCAG AA contrast failures in August 2026, traced to 1,368 malformed `rgba()` values missing the comma before the alpha channel, for example `rgba(255,255,255.06)`. Browsers parse the three-argument form as opaque `rgb()`, so every intended translucent overlay rendered as a solid fill. That is fixed. **Do not reintroduce three-argument `rgba()`.**

Every page carries an injected `<style>` block before `</head>` handling AA contrast and responsive tables. It defines `--fx-*` custom properties that remap inside dark sections, so a colour is never defined only inside a media or context block.

When adding markup, watch for light cards nested inside dark sections. A white card such as `.sce-close` placed inside `.reality` inherits the dark section's light text colour and produces white-on-white. Fix it scoped to the page unless the pattern is genuinely site-wide.

Targets: **0 AA failures at 375px**, no horizontal scroll at 375px, valid JSON-LD, FAQ schema matching the visible accordion.

---

## Deployment

**The live site is not served from this repository.** As at 31 August 2026, `china-fulfillment.com` responds from `Microsoft-IIS/7.5` with `X-Powered-By: ASP.NET`, and serves a homepage and `sitemap.xml` that do not match `main`.

Cloudflare Workers and Vercel checks both run on pull requests, but neither appears to serve the production domain. Anything merged here reaches git only. Publishing to the live site is a separate, currently manual, step.

Resolve this before treating a merge as a publish.

---

## Layout

```
*.html                     pages, served as-is
blog.html                  index, cards added by the build
sitemap.xml                maintained by hand
images/site/               page and service imagery
images/blog/               post imagery
scripts/build_blog.py      the generator
data/content/drafts/       post sources, IN the build glob
data/content/pages/        hand-built page sources, OUT of the glob
data/content/briefs/       content calendar
IMAGE-STYLE-GUIDE.md       standing image rules
IMAGE-BRIEFS-tierN.md      per-batch prompts
```
