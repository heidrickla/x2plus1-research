"""Flag which source PDFs are scans, so nobody quotes from an OCR layer again.

This exists because two claims were committed and refuted in one day, both
traceable to reading Duke-Friedlander-Iwaniec's displayed mathematics out of a
scanned PDF's text layer. The prose OCRs fine; the *equations* do not.
Proposition 2's bound extracts as

    B(M, N) ? JIapII 11,31 (Ml + N4M3+)

which is unreadable but not obviously so, and a plausible misreading of it made
it into a note and two messages before the page images settled it.

The check is structural, not statistical: a scan is a page-sized raster image
with text painted behind it, so image coverage near 1 means the text layer is
OCR and must not be quoted. Statistical proxies do not work here -- the OCR's
prose scores as well as a born-digital paper's, because only the mathematics is
mangled.

    python tools/check_sources.py

For anything flagged, read the page images:

    python -c "import pymupdf; pymupdf.open(PDF)[IDX].get_pixmap(dpi=300).save('p.png')"

and then open the PNG. For the DFI scan, page index n renders article page
n + 422.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PDFS = REPO / "refs" / "pdf"

#: Fraction of the page covered by a single image, above which we call it a scan.
SCAN_COVERAGE = 0.6


def coverage(page) -> float:
    """Largest fraction of the page area covered by any one embedded image."""
    area = abs(page.rect.width * page.rect.height)
    if not area:
        return 0.0
    best = 0.0
    for img in page.get_images(full=True):
        for rect in page.get_image_rects(img[0]):
            best = max(best, abs(rect.width * rect.height) / area)
    return best


def main() -> int:
    try:
        import pymupdf
    except ImportError:
        print("pymupdf not installed; cannot check. pip install pymupdf")
        return 2
    if not PDFS.exists():
        print(f"{PDFS} missing -- PDFs are gitignored, re-fetch per refs/bibliography.md")
        return 0

    scans = []
    for f in sorted(PDFS.glob("*.pdf")):
        try:
            doc = pymupdf.open(str(f))
            # sample a page past the front matter, which is often an image even
            # in born-digital papers (arXiv stamps, journal logos)
            cov = max(coverage(doc[i]) for i in range(min(3, len(doc)), min(6, len(doc))))
        except Exception as exc:                       # a truncated download, say
            print(f"  {f.name:44s} UNREADABLE: {exc}")
            continue
        if cov > SCAN_COVERAGE:
            scans.append(f.name)
            print(f"  {f.name:44s} SCAN ({cov:.2f}) -- read page images, not text")
        else:
            print(f"  {f.name:44s} born-digital ({cov:.2f})")

    if scans:
        print(
            "\nFor the scanned sources above, anything quoted from the extracted text\n"
            "is unreliable in displayed mathematics. Render and read the images:\n"
            '  python -c "import pymupdf; '
            "pymupdf.open('refs/pdf/NAME.pdf')[IDX].get_pixmap(dpi=300).save('p.png')\"\n"
            "DFI: page index n renders article page n + 422."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
