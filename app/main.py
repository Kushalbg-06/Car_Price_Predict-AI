from fastapi import FastAPI
from app.api.routes import router
from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Car Price Prediction API Running"}