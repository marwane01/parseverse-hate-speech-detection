# Parseverse — Hate Speech Detection (NLP)

End‑to‑end hate/offensive speech **classification** on Twitter-like text.
Built with **PyTorch + Transformers** and classic ML baselines.

## Highlights
- Data cleaning, tokenization, and vectorization
- Baselines (LogReg/SVM) and a **DistilBERT** fine‑tuned model
- Reproducible training script + notebook
- Clear metrics and confusion matrix

## Data

### Download
- Use the helper script to fetch the public dataset (not stored in the repo):

```bash
python scripts/download_data.py
# or
scripts/download_data.sh
```

Dataset from Davidson et al. (2017), *Automated Hate Speech Detection and the Problem of Offensive Language* (ICWSM).
Original repo: t-davidson/hate-speech-and-offensive-language.

> Columns: tweet text, votes per class, and majority `class` label (0=hate, 1=offensive, 2=neither).

Place the CSV under `data/` (see `data/README.md`).

## Quickstart
```bash
# 1) Create env & install
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) Train (baseline)
python -m src.parseverse.train --model baseline --max-features 5000

# 3) Train (transformer)
python -m src.parseverse.train --model distilbert --epochs 3

# 4) Predict
python -m src.parseverse.predict --text "Your input text here"
```

## Repo Structure
```
src/parseverse/        # training & inference code
notebooks/             # exploratory notebook(s)
data/                  # input CSV (ignored in git)
models/                # trained weights (ignored in git)
reports/               # metrics, plots (ignored in git)
assets/                # images for README
tests/                 # smoke tests
```

## Results
- Accuracy: 91.24%
- F1 (Macro): 75.54%
- F1 (Weighted): 91.11%

Add your real numbers after running the notebook or `src/` scripts.

## Citation
- Davidson, T., Warmsley, D., Macy, M., & Weber, I. (2017). *Automated Hate Speech Detection and the Problem of Offensive Language*. ICWSM.

## License
MIT — see `LICENSE`.
