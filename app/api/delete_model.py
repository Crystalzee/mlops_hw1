from fastapi import APIRouter, HTTPException
import os

router = APIRouter()

MODELS_DIR = "app/models"

@router.delete("/delete/{model_name}")
def delete_model(model_name: str):
    """удаление сохранённой модели"""
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Model not found")
    os.remove(model_path)
    return {"message": f"Model {model_name} deleted."}
