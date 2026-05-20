from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()                   #Base class pour les modèles SQLAlchemy 


class Prediction(Base):                     #Modèle de données pour stocker les prédictions dans la base de données
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    building_type = Column(String)
    primary_property_type = Column(String)
    neighborhood = Column(String)
    prediction = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())
