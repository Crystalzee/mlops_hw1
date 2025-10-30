import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from app.core.logger import logger

AVAILABLE_MODELS = {
    "logreg": LogisticRegression,
    "rf": RandomForestClassifier
}

MODELS_DIR = "app/models"
os.makedirs(MODELS_DIR, exist_ok=True)

def train_model(model_name: str, X, y, params: dict | None = None):
    if model_name not in AVAILABLE_MODELS:
        raise ValueError("Unknown model type")

    ModelClass = AVAILABLE_MODELS[model_name]
    model = ModelClass(**(params or {}))
    model.fit(X, y)

    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    logger.info(f"Model {model_name} trained and saved.")
    return model_name


def predict_model(model_name: str, X):
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    preds = model.predict(X).tolist()
    logger.info(f"Predictions made using {model_name}.")
    return preds


def list_models():
    return [f.replace(".pkl", "") for f in os.listdir(MODELS_DIR) if f.endswith(".pkl")]
