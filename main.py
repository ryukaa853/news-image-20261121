#!/usr/bin/env python3
"""Entry program for the news-image-20261121 bounty.

Writes the front-page image of Saturday 21 November 2026 to
/output/entry.png. The image is held in this repository as entry.png
(it is drawn by draw.py, run locally before submission) and this
program simply copies it there: no network, no randomness, so every
run writes exactly the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

DEST_DIR.mkdir(parents=True, exist_ok=True)
if not SOURCE.is_file():
    raise SystemExit(f"missing image next to main.py: {SOURCE}")
shutil.copyfile(SOURCE, DEST_DIR / "entry.png")
