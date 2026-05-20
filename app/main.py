from http.client import HTTPException

from fastapi import FastAPI
from app.api.schemas import EnergyInput
from app.models.model import model
import pandas as pd
import numpy as np
from app.database import SessionLocal
from app.db_models import Prediction

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
        prediction = np.expm1(prediction_log)[0]

        db = SessionLocal()

        db_prediction = Prediction(
            building_type=data.BuildingType,
            primary_property_type=data.PrimaryPropertyType,
            neighborhood=data.Neighborhood,
            prediction=float(prediction)
        )

        db.add(db_prediction)
        db.commit()
        db.close()

        return {"prediction": float(prediction)}

    except Exception as e:
        print("ERREUR PREDICTION:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
    
    #except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print("ERREUR PREDICTION:", e)
        raise HTTPException(status_code=500, detail=str(e))
    

