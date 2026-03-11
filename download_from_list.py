#!/usr/bin/env python3
"""
Batch PDF Downloader — downloads PDFs from an explicit list of URLs.

Supports two kinds of entries:
  - Direct PDF URLs  → downloaded as-is
  - Webpage URLs     → page is scraped for the first PDF link, which is then downloaded

Usage:
    1. Add URLs to the DOWNLOADS list below.
    2. Set OUTPUT_DIR to your desired folder.
    3. Run:  python3 download_from_list.py
"""

import os
import time
import urllib.request
import urllib.error
import urllib.parse
from html.parser import HTMLParser

# ─── CONFIG ────────────────────────────────────────────────────────────────────

OUTPUT_DIR = "pdfs/cs149-parallel-computing"

# Each entry is either:
#   "https://..."                          → filename inferred from URL
#   ("https://...", "my-custom-name.pdf")  → saved with the given filename
DOWNLOADS = [
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/efficiency/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/multicore1/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/multicore2/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/thoughtprocess/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/perfopt1/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/perfopt2/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/gpuarch/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/dataparallel/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/dnninference/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/accelerators/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/proghardware/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/aidatacenter/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/aiperfoptimization/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/cachecoherence/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/sync_consistency/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/finegrainedsync/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/transactions/",
    "https://gfxcourses.stanford.edu/cs149/fall25/lecture/wrapup/",
]

# Seconds to wait between requests (be polite to servers).
DELAY = 0.5

# ───────────────────────────────────────────────────────────────────────────────

HEADERS = {"User-Agent": "Mozilla/5.0"}


class PDFLinkExtractor(HTMLParser):
    """Scrapes all href values that contain '.pdf' from an HTML page."""
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.pdf_links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value and ".pdf" in value.lower():
                    self.pdf_links.append(urllib.parse.urljoin(self.base_url, value))


def is_direct_pdf(url):
    """True if the URL path ends with .pdf (ignoring query string)."""
    return urllib.parse.urlparse(url).path.lower().endswith(".pdf")


def find_pdf_on_page(page_url):
    """Fetch a webpage and return the first PDF link found, or None."""
    try:
        req = urllib.request.Request(page_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        parser = PDFLinkExtractor(page_url)
        parser.feed(html)
        return parser.pdf_links[0] if parser.pdf_links else None
    except Exception as e:
        return None


def slug_from_url(url):
    """Derive a readable filename from a URL, e.g. .../gpuarch/ → gpuarch.pdf"""
    path = urllib.parse.urlparse(url).path.rstrip("/")
    slug = os.path.basename(path) or "download"
    return slug if slug.endswith(".pdf") else slug + ".pdf"


def resolve(entry):
    """Return (url, custom_filename_or_None) for a list entry."""
    if isinstance(entry, tuple):
        return entry[0], entry[1]
    return entry, None


def download_pdfs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    downloaded = skipped = failed = 0

    print(f"Output folder : {os.path.abspath(OUTPUT_DIR)}")
    print(f"Entries queued: {len(DOWNLOADS)}")
    print("─" * 60)

    for idx, entry in enumerate(DOWNLOADS, start=1):
        url, custom_name = resolve(entry)

        # ── Step 1: resolve the actual PDF URL ───────────────────────────────
        if is_direct_pdf(url):
            pdf_url = url
        else:
            print(f"  [scan]  {url.split('/')[-2] or url}")
            pdf_url = find_pdf_on_page(url)
            if not pdf_url:
                print(f"  [err]   no PDF found on page → {url}")
                failed += 1
                time.sleep(DELAY)
                continue
            print(f"          → {pdf_url}")

        # ── Step 2: determine output filename ────────────────────────────────
        slug = slug_from_url(url).replace(".pdf", "")  # e.g. "gpuarch"
        if custom_name:
            filename = custom_name
        else:
            filename = f"L{idx:02d}_{slug}.pdf"

        filepath = os.path.join(OUTPUT_DIR, filename)

        # ── Step 3: skip if already downloaded ───────────────────────────────
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            print(f"  [skip]  {filename}  (already exists)")
            skipped += 1
            time.sleep(DELAY)
            continue

        # ── Step 4: download ──────────────────────────────────────────────────
        try:
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(filepath, "wb") as f:
                f.write(data)
            print(f"  [ok]    {filename}  ({len(data) / 1024:.0f} KB)")
            downloaded += 1
        except urllib.error.HTTPError as e:
            print(f"  [err]   {filename}  → HTTP {e.code}")
            failed += 1
        except Exception as e:
            print(f"  [err]   {filename}  → {e}")
            failed += 1

        time.sleep(DELAY)

    print("─" * 60)
    print(f"Done.  {downloaded} downloaded · {skipped} skipped · {failed} failed")


if __name__ == "__main__":
    download_pdfs()
