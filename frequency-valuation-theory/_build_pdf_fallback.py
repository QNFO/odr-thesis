"""Convert pandoc HTML to PDF via xhtml2pdf, stripping pseudo-selectors"""
import sys, re

html_path = sys.argv[1] if len(sys.argv) > 1 else "frequency-valuation-theory.html"
pdf_path = sys.argv[2] if len(sys.argv) > 2 else "frequency-valuation-theory.pdf"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Strip CSS pseudo-selectors that xhtml2pdf can't parse
html = re.sub(r':not\([^)]*\)\s*\{[^}]*\}', '', html)
html = re.sub(r':hover\s*\{[^}]*\}', '', html)

# Convert
from xhtml2pdf import pisa
with open(pdf_path, "wb") as f:
    pisa.CreatePDF(html, dest=f)

# Verify no U+FFFD
with open(pdf_path, "rb") as f:
    content = f.read()
    fffd = content.count(b'\xef\xbf\xbd')
    if fffd > 0:
        print(f"WARNING: {fffd} U+FFFD found")
        sys.exit(1)
    print(f"PDF built: {len(content)} bytes, 0 U+FFFD")
