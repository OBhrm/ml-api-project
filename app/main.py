from fastapi import FastAPI
from app.api.schemas import EnergyInput
from app.models.model import model
import pandas as pd
import numpy as np

app = FastAPI(title="ML API Project")

@app.get("/")                   # Root endpoint pour vérifier que l'API fonctionne
def read_root():
    return {"message": "API is working"}

@app.get("/health")             # Endpoint de santé pour vérifier que l'API est opérationnelle
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: EnergyInput):
    try:
        df = pd.DataFrame([data.model_dump()])
        prediction_log = model.predict(df)
        prediction = np.expm1(prediction_log)

        return {"prediction": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
