#!/usr/bin/env bash
set -euo pipefail

# Rerun this script after adding or replacing files in assets/img/lab so the
# Lab Activities page can serve lightweight card thumbnails.
src_dir="${1:-assets/img/lab}"
thumb_dir="${2:-assets/img/lab/thumbs}"
max_width="${LAB_THUMB_WIDTH:-900}"
quality="${LAB_THUMB_QUALITY:-78}"

python3 scripts/generate_lab_thumbnails.py \
  --src-dir "$src_dir" \
  --thumb-dir "$thumb_dir" \
  --max-width "$max_width" \
  --quality "$quality" \
  --all
