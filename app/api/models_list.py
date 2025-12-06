from fastapi import APIRouter
from app.core.model_manager import list_models

router = APIRouter()

@router.get("/models")
def get_models():
    return {"available_models": list_models()}
