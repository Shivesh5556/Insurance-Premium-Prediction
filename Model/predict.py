from pathlib import Path
import pickle
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

# Load model once
model_path = BASE_DIR / "model" / "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_premium(data: dict) -> str:
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return prediction
