import numpy as np
import pandas as pd
from app.models.model_loader import load_model

model, preprocessor = load_model()

def predict_price(data):
    df = pd.DataFrame([{
        "year": data.year,
        "km_driven": data.km_driven,
        "fuel": data.fuel,
        "transmission": data.transmission,
        "owner": data.owner,
        "company": data.company
    }])

    X = preprocessor.transform(df)
    prediction = model.predict(X)

    return float(prediction[0])

from app.db.supabase import supabase

def save_prediction(data, price):
    supabase.table("predictions").insert({
        "year": data.year,
        "km_driven": data.km_driven,
        "fuel": data.fuel,
        "price": price
    }).execute()