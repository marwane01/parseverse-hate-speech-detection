#!/usr/bin/env bash
set -e
mkdir -p data
: "${URL:=https://raw.githubusercontent.com/t-davidson/hate-speech-and-offensive-language/master/data/labeled_data.csv}"
: "${OUT:=data/labeled_data.csv}"
echo "Downloading $URL -> $OUT"
curl -L "$URL" -o "$OUT"
echo "Done."
