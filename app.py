from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
import interface

app = FastAPI()

interface.load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = interface.predict(request.dict())
    return PredictResponse(prediction=prediction)
