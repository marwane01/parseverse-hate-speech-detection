import argparse, joblib
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True, help="Text to classify")
    args = ap.parse_args()

    vec = joblib.load(Path("models") / "tfidf.joblib")
    clf = joblib.load(Path("models") / "logreg.joblib")

    X = vec.transform([args.text])
    pred = clf.predict(X)[0]
    print(f"Predicted class: {pred} (0=hate, 1=offensive, 2=neither)")

if __name__ == "__main__":
    main()
