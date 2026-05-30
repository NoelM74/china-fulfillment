#!/usr/bin/env python3
"""
apply_premium_design.py — Propagate the homepage's premium design system
across every other page.

Removes AI-build decorative gradients (multi-stop navy washes, grid-texture
overlays, radial glow blobs, and off-brand green/red/blue/yellow gradient
section washes), flattening them to solid brand surfaces. Functional gradients
(marquee edge-fades, image scrims, the hero photo overlay) are left untouched.
Also adds the typography foundation (font smoothing, balanced headings).

index.html is skipped — it was hand-tuned already. Run once.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
NAVY_SECTION = "#0a152a"   # full-bleed dark sections / heroes
NAVY_CARD = "#0e2042"      # dark card surfaces (kept distinct from sections)

# Exact gradient-function text -> replacement. Only the gradient text is swapped,
# so the surrounding `background:` / `border:` context stays intact.
EXACT = {
    # ── dark section / hero / CTA washes -> flat section navy
    "linear-gradient(135deg,var(--ink) 0%,var(--navy) 55%,#001428 100%)": NAVY_SECTION,
    "linear-gradient(130deg,#010b1a 0%,#0d2144 45%,#091830 70%,#001428 100%)": NAVY_SECTION,
    "linear-gradient(135deg,var(--n2) 0%,#001428 100%)": NAVY_SECTION,
    "linear-gradient(135deg,var(--n3),var(--navy))": NAVY_SECTION,
    "linear-gradient(135deg,var(--ink),#001830)": NAVY_SECTION,
    "linear-gradient(135deg,var(--ink) 0%,#001830 100%)": NAVY_SECTION,
    "linear-gradient(145deg,var(--n3) 0%,var(--navy) 40%,#001428 100%)": NAVY_SECTION,
    # ── ambiguous / card-ish dark gradients -> flat card navy (never invisible)
    "linear-gradient(135deg,#1a1a3a 0%,#0d2144 100%)": NAVY_CARD,
    "linear-gradient(135deg,#111827 0%,#1e3a5f 100%)": NAVY_CARD,
    "linear-gradient(135deg,#0d2144,#0a3060)": NAVY_CARD,
    "linear-gradient(135deg,#0d2144 0%,#1a3a6e 100%)": NAVY_CARD,
    "linear-gradient(135deg,#0a1628 0%,#0d2144 100%)": NAVY_CARD,
    "linear-gradient(135deg,#1a0a2e,#2d1060)": NAVY_CARD,   # purple slop
    "linear-gradient(135deg,#1a1a0a,#3d2a00)": NAVY_CARD,   # brown slop
    # ── subtle white card sheens -> flat translucent
    "linear-gradient(135deg,rgba(255,255,255,.08),rgba(255,255,255,.04))": "rgba(255,255,255,.05)",
    "linear-gradient(135deg,rgba(255,255,255,.07),rgba(255,255,255,.03))": "rgba(255,255,255,.04)",
    # ── off-brand colored section washes -> flat single tint
    "linear-gradient(135deg,#f0fdf4,#ecfdf5)": "#f2f9f4",   # green
    "linear-gradient(135deg,#fef2f2,#fff7ed)": "#fdf4f2",   # red
    "linear-gradient(135deg,#e8eef7,#d0ddf0)": "#eaf0f8",   # blue
    "linear-gradient(135deg,#fffbeb,#fef3c7)": "#fdf6e3",   # yellow
    # ── accent bars / circles / lines -> solid brand colour
    "linear-gradient(135deg,var(--navy),var(--blue))": "var(--blue)",
    "linear-gradient(135deg,var(--navy),var(--b2))": "var(--blue)",
    "linear-gradient(90deg,var(--blue),var(--blue2))": "var(--blue)",
    "linear-gradient(90deg,var(--blue),var(--b2))": "var(--blue)",
    "linear-gradient(90deg,var(--navy),var(--b2),var(--ac))": "var(--bd)",
    "linear-gradient(90deg,var(--yellow),#fcd34d)": "var(--yellow)",
    "linear-gradient(90deg,var(--green),#34d399)": "var(--green)",
    "linear-gradient(90deg,#ef4444,#f87171)": "#ef4444",
    "linear-gradient(to bottom,var(--blue),rgba(26,79,214,.08))": "var(--blue)",
}

# Regexes: glow blobs and grid textures (these have no ';' or '}' inside the value).
GLOW_RE = re.compile(r"background:\s*radial-gradient[^;}]*")
GRID_RE = re.compile(r"background-image:\s*linear-gradient[^;{}]*1px[^;{}]*")

TYPO = (
    "body{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;"
    "text-rendering:optimizeLegibility}\n"
    "h1,h2,h3,h4,h5{text-wrap:balance}\np{text-wrap:pretty}\n"
)

changed = []
for f in sorted(ROOT.glob("*.html")):
    if f.name == "index.html":
        continue
    t = f.read_text(encoding="utf-8")
    orig = t

    for needle, repl in EXACT.items():
        t = t.replace(needle, repl)

    t = GLOW_RE.sub("background:none", t)
    t = GRID_RE.sub("background-image:none", t)

    # Typography foundation, once, right after the first <style>
    if "text-wrap:balance" not in t and "<style>" in t:
        t = t.replace("<style>", "<style>\n" + TYPO, 1)

    if t != orig:
        f.write_text(t, encoding="utf-8")
        changed.append(f.name)

print(f"Updated {len(changed)} pages:")
for c in changed:
    print("  " + c)
