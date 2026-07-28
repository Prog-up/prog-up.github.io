#!/usr/bin/env bash

set -euo pipefail

# Script to optimize images in src/assets/ using ImageMagick
# Converts JPG/PNG images to WebP, updates markdown/njk references, and removes original unoptimized files.

ASSETS_DIR="src/assets"
QUALITY=85

echo "🔍 Searching for unoptimized images (.jpg, .jpeg, .png) in ${ASSETS_DIR}..."

# Choose ImageMagick command (prefer 'magick', fallback to 'convert')
if command -v magick &>/dev/null; then
    MAGICK_CMD="magick"
elif command -v convert &>/dev/null; then
    MAGICK_CMD="convert"
else
    echo "❌ ImageMagick is not installed. Please install ImageMagick (magick or convert)."
    exit 1
fi

FOUND=0

while IFS= read -r -d '' img; do
    FOUND=1
    ext="${img##*.}"
    base_no_ext="${img%.*}"
    webp_path="${base_no_ext}.webp"
    filename=$(basename "$img")
    webp_filename=$(basename "$webp_path")

    echo "🖼️  Optimizing: ${img} -> ${webp_path}"

    # Convert to webp with ImageMagick
    "$MAGICK_CMD" "$img" -quality "$QUALITY" "$webp_path"

    # Update references in src directory (.md and .njk files)
    find src -type f \( -name "*.md" -o -name "*.njk" -o -name "*.html" \) -exec perl -pi -e "s|\Q${filename}\E|${webp_filename}|g" {} +

    # Remove the original image file
    rm -f "$img"

    echo "✅ Converted and updated references for ${filename}."
done < <(find "$ASSETS_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0)

if [ "$FOUND" -eq 0 ]; then
    echo "✨ All images are already optimized to WebP format!"
else
    echo "🎉 Image optimization completed successfully."
fi
