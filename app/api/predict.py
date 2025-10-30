from fastapi import APIRouter, HTTPException
from app.schemas.schemas import PredictRequest
from app.core.model_manager import predict_model

router = APIRouter()

@router.post("/predict")
def predict(req: PredictRequest):
    try:
        preds = predict_model(req.model_name, req.X)
        return {"predictions": preds}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
