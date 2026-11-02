"""Gera index.html, terms.html e privacy.html a partir de src/.

Uso: python3 build.py
"""
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
SRC = ROOT / "src"

ETSY_NOTICE = (
    "The term 'Etsy' is a trademark of Etsy, Inc. "
    "This Application uses Etsy's API, but is not endorsed or certified by Etsy."
)

DRAFT_BANNER = (
    '<div class="draft"><strong>Draft, not yet in effect.</strong> '
    "This document is under legal review. The company providing ERPrinter and "
    "the highlighted items will be filled in before launch.</div>"
)

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="./">ERP<span>rinter</span></a>
    <nav>
      <a href="./#etsy">Etsy</a>
      <a href="./#contact">Contact</a>
      <a href="terms.html">Terms</a>
      <a href="privacy.html">Privacy</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site">
  <div class="wrap">
    <p>{etsy_notice}</p>
    <p><a href="terms.html">Terms of Use</a> · <a href="privacy.html">Privacy Policy</a> · <a href="mailto:support@erprinter.com">support@erprinter.com</a></p>
  </div>
</footer>
</body>
</html>
"""

DESCRIPTION = "ERPrinter is a back-office ERP for small 3D printing shops: cost estimates, materials inventory, production queue and orders."


def render(name, title, body):
    html = PAGE.format(title=title, description=DESCRIPTION, body=body, etsy_notice=ETSY_NOTICE)
    (ROOT / name).write_text(html, encoding="utf-8")


def legal(md_file):
    text = (SRC / md_file).read_text(encoding="utf-8")
    # A primeira linha em negrito vira o título da página.
    first, rest = text.split("\n", 1)
    heading = first.strip("* ").replace("ERPrinter — ", "")
    content = markdown.markdown(rest, extensions=["tables"])
    return f'<div class="wrap legal">{DRAFT_BANNER}<h1>{heading}</h1>{content}</div>'


render("index.html", "ERPrinter: the back office for 3D printing shops", (SRC / "index.html").read_text(encoding="utf-8"))
render("terms.html", "Terms of Use · ERPrinter", legal("terms.md"))
render("privacy.html", "Privacy Policy · ERPrinter", legal("privacy.md"))
print("ok: index.html, terms.html, privacy.html")
