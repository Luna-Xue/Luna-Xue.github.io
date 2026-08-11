#!/usr/bin/env bash
set -euo pipefail

# Rerun this script after adding or replacing files in assets/img/lab so the
# Lab Activities page can serve lightweight card thumbnails.
src_dir="${1:-assets/img/lab}"
thumb_dir="${2:-assets/img/lab/thumbs}"
max_width="${LAB_THUMB_WIDTH:-900}"
quality="${LAB_THUMB_QUALITY:-78}"

mkdir -p "$thumb_dir"

find "$src_dir" -maxdepth 1 -type f \( \
  -iname '*.jpg' -o \
  -iname '*.jpeg' -o \
  -iname '*.png' -o \
  -iname '*.webp' \
\) -print0 | while IFS= read -r -d '' src; do
  filename="$(basename "$src")"
  dest="$thumb_dir/$filename"

  convert "$src" \
    -auto-orient \
    -strip \
    -resize "${max_width}x${max_width}>" \
    -quality "$quality" \
    "$dest"

  printf 'generated %s\n' "$dest"
done
