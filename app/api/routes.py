from fastapi import APIRouter
from app.schemas.prediction import CarInput
from app.services.predictor import predict_price

router = APIRouter()

@router.post("/predict")
def predict(data: CarInput):
    result = predict_price(data)
    return {"predicted_price": result}