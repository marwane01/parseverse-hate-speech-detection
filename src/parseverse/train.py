import argparse, os, json, joblib
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Minimal baseline trainer (TF-IDF + Logistic Regression)
def train_baseline(csv_path: str, text_col: str, label_col: str, max_features: int = 5000):
    df = pd.read_csv(csv_path)
    X = df[text_col].astype(str).fillna("")
    y = df[label_col].astype(int)

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    vec = TfidfVectorizer(ngram_range=(1,2), max_features=max_features, min_df=2)
    Xtrv = vec.fit_transform(Xtr)
    Xtev = vec.transform(Xte)

    clf = LogisticRegression(max_iter=200)
    clf.fit(Xtrv, ytr)

    yhat = clf.predict(Xtev)
    print(classification_report(yte, yhat, digits=4))

    out_dir = Path("models")
    out_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(vec, out_dir / "tfidf.joblib")
    joblib.dump(clf, out_dir / "logreg.joblib")
    print(f"Saved TF-IDF and model to: {out_dir}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["baseline"], default="baseline")
    ap.add_argument("--csv", default="data/labeled_data.csv")
    ap.add_argument("--text-col", default="tweet")
    ap.add_argument("--label-col", default="class")
    ap.add_argument("--max-features", type=int, default=5000)
    args = ap.parse_args()

    if args.model == "baseline":
        train_baseline(args.csv, args.text_col, args.label_col, args.max_features)

if __name__ == "__main__":
    main()
