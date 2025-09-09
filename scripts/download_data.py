#!/usr/bin/env python3
import argparse, os, sys, urllib.request, pathlib

DATA_URL = "https://raw.githubusercontent.com/t-davidson/hate-speech-and-offensive-language/master/data/labeled_data.csv"

def download(url: str, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    print(f"Downloading {url} -> {out_path}")
    urllib.request.urlretrieve(url, out_path)
    print("Done.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Download dataset CSV into data/ folder.")
    ap.add_argument("--url", default=DATA_URL, help="Source CSV URL")
    ap.add_argument("--out", default="data/labeled_data.csv", help="Output path")
    args = ap.parse_args()
    download(args.url, args.out)
