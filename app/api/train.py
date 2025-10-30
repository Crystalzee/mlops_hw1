from fastapi import APIRouter, HTTPException
from app.schemas.schemas import TrainRequest
from app.core.model_manager import train_model

router = APIRouter()

@router.post("/train")
def train(req: TrainRequest):
    try:
        model_name = train_model(req.model_name, req.X, req.y, req.params)
        return {"message": f"Model {model_name} trained and saved."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
