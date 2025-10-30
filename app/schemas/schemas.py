from pydantic import BaseModel
from typing import List, Optional

class TrainRequest(BaseModel):
    model_name: str
    X: List[List[float]]
    y: List[int]
    params: Optional[dict] = None

class PredictRequest(BaseModel):
    model_name: str
    X: List[List[float]]
