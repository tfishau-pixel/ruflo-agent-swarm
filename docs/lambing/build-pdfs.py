#!/usr/bin/env python3
"""Build the lambing suite PDFs from the HTML sources.

Usage:  python3 build-pdfs.py            (from docs/lambing/)

Requires: a Chromium/Chrome binary (env CHROME, else `chromium` on PATH)
and, for contents-page folios and PDF bookmarks, `pip install pypdf`.

What it does, per output:
  handbook A4 + mobile  - two-pass build: render once, locate each
                          section's page, inject real page numbers into
                          the Contents page, render again, then write
                          PDF outline bookmarks. The mobile variant swaps
                          the two `@variant-` CSS markers first, and its
                          folios are computed against its own pagination.
  far-from-help A4      - single pass + outline bookmarks.
  cheatsheet, laminate  - single pass.
The repository HTML keeps empty `.toc-p` spans; folios exist only inside
the generated PDFs, so each variant's contents page is always correct.
"""
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, "pdf")
CHROME = os.environ.get("CHROME") or shutil.which("chromium") or "/opt/pw-browsers/chromium"

HANDBOOK_TOC = [  # (data-toc id, kicker text, title text)
    ("s1", "Section 1", "Quick-start overview"),
    ("s2", "Section 2", "Preparing before lambing"),
    ("s3", "Section 3", "Understanding late pregnancy"),
    ("s4", "Section 4", "Normal lambing, step by step"),
    ("s5", "Section 5", "Normal and abnormal presentation"),
    ("s6", "Section 6", "Common complications"),
    ("s7", "Section 7", "Immediate newborn lamb care"),
    ("s8", "Section 8", "Colostrum"),
    ("s9", "Section 9", "Hypothermia and weak lambs"),
    ("s10", "Section 10", "Ewe care after lambing"),
    ("s11", "Section 11", "Twins and multiple births"),
    ("s12", "Section 12", "The first 72 hours"),
    ("s13", "Section 13", "Valais Blacknose"),
    ("s14", "Section 14", "New Zealand seasonal"),
    ("s15", "Section 15", "Emergency cheat sheet"),
    ("contacts", "Appendix", "Emergency contacts"),
    ("sources", "Appendix", "Sources"),
]
FFH_OUTLINE = [
    ("Read first", "The rules of engagement"),
    ("Procedure 1", "Internal exam"),
    ("Procedure 2", "Stomach-tubing"),
    ("Procedure 3", "Intraperitoneal"),
    ("Procedure 4", "Replacing a bearing"),
    ("Sections 5", "Extended kit"),
    ("Section 7", "wider evidence"),
]

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def render(html_path, out_pdf):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", html_path],
                   check=True, capture_output=True)

def page_texts(pdf_path):
    out = subprocess.run(["pdftotext", pdf_path, "-"], capture_output=True, text=True)
    if out.returncode != 0:  # poppler missing: degrade to no folios/bookmarks
        return None
    return [norm(p) for p in out.stdout.split("\f")]

def locate(pages, entries, skip=2):
    """First page (1-based) at/after `skip` containing kicker+title together."""
    found = {}
    for key, kicker, title in entries:
        k, t = norm(kicker), norm(title)[:20]
        for i, p in enumerate(pages):
            if i < skip:
                continue
            if k in p and t in p:
                found[key] = i + 1
                break
    return found

def add_bookmarks(pdf_path, items):
    """items: list of (title, page-1-based). Rewrites the file in place."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        print("  pypdf not installed - skipping bookmarks", file=sys.stderr)
        return
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.append(reader)
    for title, page in items:
        if page and 1 <= page <= len(reader.pages):
            writer.add_outline_item(title, page - 1)
    with open(pdf_path, "wb") as f:
        writer.write(f)

def build_handbook(variant, out_name):
    src = open(os.path.join(HERE, "handbook.html")).read()
    if variant == "mobile":
        src = src.replace("size:A4; /* @variant-page */", "size:120mm 212mm;")
        src = src.replace("--base:10.5pt; /* @variant-base */", "--base:11pt;")
    with tempfile.TemporaryDirectory() as td:
        h1 = os.path.join(td, "pass1.html")
        open(h1, "w").write(src)
        p1 = os.path.join(td, "pass1.pdf")
        render(h1, p1)
        pages = page_texts(p1)
        out = os.path.join(PDF, out_name)
        if pages is None:
            render(h1, out)
            print(f"  {out_name}: rendered (no poppler - folios/bookmarks skipped)")
            return
        loc = locate(pages, HANDBOOK_TOC)
        for key, page in loc.items():
            src = src.replace(f'<span class="toc-p" data-toc="{key}"></span>',
                              f'<span class="toc-p" data-toc="{key}">p. {page}</span>')
        h2 = os.path.join(td, "pass2.html")
        open(h2, "w").write(src)
        render(h2, out)
        marks = [("Cover", 1), ("Contents", 2)]
        for key, kicker, title in HANDBOOK_TOC:
            if key in loc:
                marks.append((title, loc[key]))
        add_bookmarks(out, marks)
        print(f"  {out_name}: {len(loc)}/{len(HANDBOOK_TOC)} sections located, bookmarks written")

def build_ffh():
    out = os.path.join(PDF, "far-from-help-A4.pdf")
    render(os.path.join(HERE, "far-from-help.html"), out)
    pages = page_texts(out)
    if pages:
        loc = locate(pages, [(t, k, t) for k, t in FFH_OUTLINE], skip=1)
        marks = [("Cover", 1)] + [(t, loc[t]) for k, t in FFH_OUTLINE if t in loc]
        add_bookmarks(out, marks)
    print("  far-from-help-A4.pdf: done")

def main():
    os.makedirs(PDF, exist_ok=True)
    print("Building lambing suite PDFs with", CHROME)
    build_handbook("a4", "first-lambing-season-handbook-A4.pdf")
    build_handbook("mobile", "first-lambing-season-handbook-mobile.pdf")
    build_ffh()
    render(os.path.join(HERE, "cheatsheet.html"), os.path.join(PDF, "lambing-emergency-cheatsheet-A4.pdf"))
    print("  lambing-emergency-cheatsheet-A4.pdf: done")
    render(os.path.join(HERE, "laminate-cards.html"), os.path.join(PDF, "far-from-help-laminate-cards-A4.pdf"))
    print("  far-from-help-laminate-cards-A4.pdf: done")

if __name__ == "__main__":
    main()
