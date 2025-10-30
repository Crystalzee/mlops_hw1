import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="ML Model Dashboard", layout="wide")
st.title("ML Model Dashboard")

# --- health check ---
try:
    r = requests.get(f"{API_URL}/health")
    if r.status_code == 200:
        st.success("Backend is running")
except Exception:
    st.error("Backend not reachable. Run `uvicorn app.main:app --reload` first.")

# --- train section ---
st.header("Train model")

model_name = st.selectbox("Choose model", ["logreg", "rf"])
params = st.text_input("Model params (JSON)", '{"max_iter": 100}' if model_name == "logreg" else '{"n_estimators": 10}')

train_data = st.text_area("Training data (X)", "[[1,2],[2,3],[3,4],[4,5]]")
train_labels = st.text_input("Labels (y)", "[0,0,1,1]")

if st.button("Train model"):
    try:
        payload = {
            "model_name": model_name,
            "X": eval(train_data),
            "y": eval(train_labels),
            "params": eval(params)
        }
        resp = requests.post(f"{API_URL}/train", json=payload)
        st.json(resp.json())
    except Exception as e:
        st.error(str(e))

# --- predict section ---
st.header("Predict")

predict_model_name = st.selectbox("Model for prediction", ["logreg", "rf"], key="predict_model")
predict_data = st.text_area("Input data (X)", "[[1,2],[3,4]]")

if st.button("Predict"):
    try:
        payload = {"model_name": predict_model_name, "X": eval(predict_data)}
        resp = requests.post(f"{API_URL}/predict", json=payload)
        preds = resp.json().get("predictions", [])
        st.success(f"Predictions: {preds}")
    except Exception as e:
        st.error(str(e))

# --- list models ---
st.header("Models available")

if st.button("Refresh list"):
    models = requests.get(f"{API_URL}/models").json()
    st.json(models)
