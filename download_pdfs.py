#!/usr/bin/env python3
"""
PDF Downloader — fetches a sequentially numbered set of PDFs from a URL pattern.

Usage:
    python download_pdfs.py

Edit the CONFIG section below to customize the URL, range, and output folder.

Examples:
    MIT 6.5900 Lectures:   https://csg.csail.mit.edu/6.5900/Lectures/L{n}.pdf
    MIT 6.5930 Lectures:   https://csg.csail.mit.edu/6.5930/Lectures/L{n}.pdf
"""

import os
import time
import urllib.request
import urllib.error

# ─── CONFIG ────────────────────────────────────────────────────────────────────

# URL template — use {n} as the placeholder for the lecture number.
URL_TEMPLATE = "https://csg.csail.mit.edu/6.5900/Lectures/L{n}.pdf"

# Range of numbers to try (inclusive).
START = 10
END   = 24

# Folder to save downloaded PDFs into (created automatically if it doesn't exist).
OUTPUT_DIR = "pdfs/mit-65900-Computer-System-Architecture"

# Stop after this many consecutive 404 / failures (avoids hammering the server).
MAX_CONSECUTIVE_FAILURES = 3

# Seconds to wait between requests (be polite to the server).
DELAY = 0.5

# ───────────────────────────────────────────────────────────────────────────────


def download_pdfs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    consecutive_failures = 0
    downloaded = 0
    skipped = 0

    print(f"Output folder : {os.path.abspath(OUTPUT_DIR)}")
    print(f"URL template  : {URL_TEMPLATE}")
    print(f"Range         : L{START} – L{END}")
    print("─" * 60)

    for n in range(START, END + 1):
        url      = URL_TEMPLATE.format(n=n)
        filename = os.path.basename(url)
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Skip files that are already downloaded.
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            print(f"  [skip]  {filename} (already exists)")
            skipped += 1
            continue

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as response:
                if response.status == 200:
                    data = response.read()
                    with open(filepath, "wb") as f:
                        f.write(data)
                    size_kb = len(data) / 1024
                    print(f"  [ok]    {filename}  ({size_kb:.0f} KB)")
                    downloaded += 1
                    consecutive_failures = 0
                else:
                    print(f"  [skip]  {filename}  (HTTP {response.status})")
                    consecutive_failures += 1

        except urllib.error.HTTPError as e:
            print(f"  [miss]  {filename}  (HTTP {e.code})")
            consecutive_failures += 1
        except urllib.error.URLError as e:
            print(f"  [err]   {filename}  ({e.reason})")
            consecutive_failures += 1
        except Exception as e:
            print(f"  [err]   {filename}  ({e})")
            consecutive_failures += 1

        if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
            print(f"\nStopped after {MAX_CONSECUTIVE_FAILURES} consecutive failures.")
            break

        time.sleep(DELAY)

    print("─" * 60)
    print(f"Done. {downloaded} downloaded, {skipped} already existed.")


if __name__ == "__main__":
    download_pdfs()
