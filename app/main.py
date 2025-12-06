from fastapi import FastAPI
from app.api import health, train, predict, models_list, delete_model

app = FastAPI(title="ML Model API")

app.include_router(health.router)
app.include_router(train.router)
app.include_router(predict.router)
app.include_router(models_list.router)
app.include_router(delete_model.router)