#!/usr/bin/env python3
"""Generate lightweight thumbnails for lab activity images."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional

from PIL import Image, ImageOps


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def is_image(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def source_images(src_dir: Path) -> list[Path]:
    return sorted(path for path in src_dir.iterdir() if is_image(path))


def listed_images(list_path: Path, src_dir: Path) -> list[Path]:
    images: list[Path] = []
    for raw_line in list_path.read_text().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        path = Path(line)
        if "thumbs" in path.parts:
            continue
        if not path.is_absolute():
            path = Path.cwd() / path
        if is_image(path) and src_dir.resolve() in path.resolve().parents:
            images.append(path)
    return sorted(set(images))


def save_thumbnail(src: Path, thumb_dir: Path, max_width: int, quality: int, skip_existing: bool) -> Optional[Path]:
    dest = thumb_dir / src.name
    thumb_dir.mkdir(parents=True, exist_ok=True)

    if skip_existing and dest.exists():
        print(f"skipped existing {dest}")
        return None

    with Image.open(src) as image:
        image = ImageOps.exif_transpose(image)
        image.thumbnail((max_width, max_width), Image.Resampling.LANCZOS)

        suffix = dest.suffix.lower()
        save_kwargs: dict[str, object] = {"optimize": True}
        if suffix in {".jpg", ".jpeg"}:
            image = image.convert("RGB")
            save_kwargs.update({"quality": quality, "progressive": True})
        elif suffix == ".png":
            if image.mode not in {"RGB", "RGBA"}:
                image = image.convert("RGBA")
            save_kwargs.update({"compress_level": 9})
        elif suffix == ".webp":
            save_kwargs.update({"quality": quality, "method": 6})

        image.save(dest, **save_kwargs)

    return dest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src-dir", default="assets/img/lab", type=Path)
    parser.add_argument("--thumb-dir", default="assets/img/lab/thumbs", type=Path)
    parser.add_argument("--max-width", default=int(os.environ.get("LAB_THUMB_WIDTH", "900")), type=int)
    parser.add_argument("--quality", default=int(os.environ.get("LAB_THUMB_QUALITY", "78")), type=int)
    parser.add_argument("--from-list", type=Path, help="Generate thumbnails for image paths listed in a text file.")
    parser.add_argument("--all", action="store_true", help="Generate thumbnails for every image in src-dir.")
    parser.add_argument("--skip-existing", action="store_true", help="Only create thumbnails that do not already exist.")
    args = parser.parse_args()

    src_dir = args.src_dir
    thumb_dir = args.thumb_dir

    if args.from_list:
        images = listed_images(args.from_list, src_dir)
    else:
        images = source_images(src_dir)

    if not args.all and not args.from_list:
        parser.error("pass --all or --from-list")

    if not images:
        print("No lab images to thumbnail.")
        return

    for src in images:
        dest = save_thumbnail(src, thumb_dir, args.max_width, args.quality, args.skip_existing)
        if dest:
            print(f"generated {dest}")


if __name__ == "__main__":
    main()
