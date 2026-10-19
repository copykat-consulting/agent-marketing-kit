#!/usr/bin/env python3
"""Makes a review copy of a finished piece so it can be published as a private
Artifact and linked from the Marketing Command Center.

Two modes:

  HTML piece (blog, newsletter, single-topic email):
    python3 make_review_page.py html <piece.html> <out.html> --name "<Agent> Lifestyle Blog, November 2026" \
        --kind "Lifestyle blog" --saved "claude/blogs/<file>.html"

  Postcard (or any print piece with preview images and a PDF):
    python3 make_review_page.py postcard <out-dir> --name "<Agent> Market Postcard, November 2026" \
        --front front.png --back back.png --pdf postcard.pdf --saved "claude/postcards/<file>.pdf"
    Copies the files into <out-dir> next to index.html. Publish index.html with the
    three files as supporting files (published paths: front.png, back.png, postcard.pdf).

The original file is never changed. In the review copy:
- a slim "Review copy" bar sits on top, naming the piece and where the paste-ready file is saved;
- photos hosted elsewhere (ImageKit and similar) can't load inside an Artifact, so each one
  shows as a labeled photo box, and the bar lists every photo as a link that opens it.
"""
import argparse
import html
import os
import re
import shutil
import sys
import urllib.parse

BAR_CSS = """
<style>
:root{color-scheme:light}
body{background:#f4f2ee}
.rvw-bar{font-family:'Montserrat',system-ui,-apple-system,'Segoe UI',sans-serif;background:#2b2d2a;color:#f3f0e9;
  padding-block:14px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));
  font-size:13px;line-height:1.55}
.rvw-in{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:6px}
.rvw-top{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline}
.rvw-pill{font-size:10px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;background:#f3f0e9;color:#2b2d2a;padding:3px 9px;border-radius:20px}
.rvw-name{font-weight:600}
.rvw-note{color:rgba(243,240,233,.78)}
.rvw-photos{display:flex;flex-wrap:wrap;gap:4px 14px}
.rvw-photos a{color:#f3f0e9;text-decoration:underline;text-underline-offset:2px}
.rvw-bar a:focus-visible{outline:2px solid #f3f0e9;outline-offset:2px}
</style>
"""


def photo_name(url):
    base = urllib.parse.unquote(urllib.parse.urlparse(url).path.rsplit("/", 1)[-1])
    return re.sub(r"\.(png|jpe?g|webp|gif)$", "", base, flags=re.I) or "Photo"


def placeholder(name, small=False):
    h = 320 if small else 700
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}">'
        f'<rect width="1200" height="{h}" fill="#e7e1d6"/>'
        f'<rect x="24" y="24" width="1152" height="{h - 48}" fill="none" stroke="#9a8d7e" stroke-width="3" stroke-dasharray="14 10"/>'
        f'<text x="600" y="{h // 2 - 20}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="{44 if small else 30}" letter-spacing="6" fill="#6f665b">{"IMAGE" if small else "PHOTO"}</text>'
        f'<text x="600" y="{h // 2 + 40}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="{48 if small else 40}" fill="#292c29">{html.escape(name if len(name) <= 36 else name[:34] + "...")}</text>'
        "</svg>"
    )
    return "data:image/svg+xml," + urllib.parse.quote(svg)


def bar(kind, name, saved, photos, extra=""):
    ph = ""
    if photos:
        links = "".join(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(n)}</a>' for n, u in photos)
        ph = ('<div class="rvw-note">Photos load from your image host on the live page. Open each one:</div>'
              f'<div class="rvw-photos">{links}</div>')
    sv = f'<div class="rvw-note">Saved: {html.escape(saved)}</div>' if saved else ""
    return (f'<div class="rvw-bar"><div class="rvw-in"><div class="rvw-top"><span class="rvw-pill">Review copy</span>'
            f'<span class="rvw-name">{html.escape(kind)}</span><span class="rvw-note">Not live yet</span></div>'
            f"{sv}{ph}{extra}</div></div>")


def html_mode(a):
    s = open(a.src, encoding="utf-8").read()
    s = re.sub(r"^\s*<!--.*?-->\s*", "", s, count=1, flags=re.S)       # leading paste-instructions comment
    s = re.sub(r"<!DOCTYPE[^>]*>", "", s, flags=re.I)
    s = re.sub(r"<title>.*?</title>", "", s, flags=re.I | re.S)
    photos, seen = [], set()

    def swap(m):
        tag, url = m.group(0), m.group(2)
        name = photo_name(url)
        alt = re.search(r"\balt=(\"|')([^\"']*)\1", tag, flags=re.I)
        if alt and alt.group(2).strip() and (len(name) < 4 or name.isdigit()):
            name = alt.group(2).strip()[:60]
        w = re.search(r"\bwidth=[\"']?(\d+)", tag, flags=re.I)
        small = bool(w and int(w.group(1)) <= 400)
        if url not in seen:
            seen.add(url)
            photos.append((name, url))
        return tag.replace(m.group(1) + url + m.group(1), m.group(1) + placeholder(name, small) + m.group(1), 1)

    s = re.sub(r"<img\b[^>]*?\bsrc=(\"|')(https?://[^\"']+)\1[^>]*>", swap, s, flags=re.I)
    head = (f"<title>{html.escape(a.name)}</title>\n"
            '<meta name="claude:viewport-fit-sides" content="cover">\n' + BAR_CSS)
    out = head + bar(a.kind, a.name, a.saved, photos) + "\n" + s
    open(a.out, "w", encoding="utf-8").write(out)
    print(f"Review copy: {a.out} ({len(photos)} photos listed)")


def postcard_mode(a):
    os.makedirs(a.out, exist_ok=True)
    for src, dst in ((a.front, "front.png"), (a.back, "back.png"), (a.pdf, "postcard.pdf")):
        shutil.copyfile(src, os.path.join(a.out, dst))
    extra = ('<div class="rvw-note">Shown at actual proportions. The print-ready PDF includes bleed for your printer.</div>'
             '<div class="rvw-photos"><a href="postcard.pdf" target="_blank" rel="noopener">Open the print-ready PDF</a></div>')
    page = (f"<title>{html.escape(a.name)}</title>\n"
            '<meta name="claude:viewport-fit-sides" content="cover">\n' + BAR_CSS + """
<style>
.pc{font-family:'Montserrat',system-ui,sans-serif;color:#292c29;padding-block:28px 56px;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.pc-in{max-width:980px;margin:0 auto;display:flex;flex-direction:column;gap:28px}
.pc figure{margin:0;display:flex;flex-direction:column;gap:8px}
.pc figcaption{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#6f665b}
.pc img{display:block;width:100%;max-width:100%;height:auto;box-shadow:0 2px 18px rgba(41,44,41,.14);background:#fff}
.pc p{margin:0;font-size:13px;color:#6f665b}
</style>
""" + bar(a.kind, a.name, a.saved, [], extra) + """
<div class="pc"><div class="pc-in">
  <figure><figcaption>Front</figcaption><img src="front.png" alt="Postcard front"></figure>
  <figure><figcaption>Back</figcaption><img src="back.png" alt="Postcard back"></figure>
</div></div>
""")
    open(os.path.join(a.out, "index.html"), "w", encoding="utf-8").write(page)
    print(f"Review page: {os.path.join(a.out, 'index.html')} (+ front.png, back.png, postcard.pdf)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="mode", required=True)
    h = sub.add_parser("html")
    h.add_argument("src"); h.add_argument("out")
    pc = sub.add_parser("postcard")
    pc.add_argument("out")
    pc.add_argument("--front", required=True); pc.add_argument("--back", required=True); pc.add_argument("--pdf", required=True)
    for q in (h, pc):
        q.add_argument("--name", required=True, help="Artifact title, e.g. 'Jane Smith Lifestyle Blog, November 2026'")
        q.add_argument("--kind", default="", help="Shown in the bar, e.g. 'Lifestyle blog'")
        q.add_argument("--saved", default="", help="Where the paste-ready file is saved in the Project")
    a = p.parse_args()
    a.kind = a.kind or ("Market report postcard" if a.mode == "postcard" else "Review copy")
    html_mode(a) if a.mode == "html" else postcard_mode(a)


if __name__ == "__main__":
    sys.exit(main())
