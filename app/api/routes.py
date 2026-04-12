from fastapi import APIRouter, Depends
from app.schemas.prediction import CarInput
from app.services.predictor import predict_price
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/predict")
def predict(data: CarInput, user=Depends(get_current_user)):
    result = predict_price(data)
    return {"predicted_price": result}