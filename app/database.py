from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:117432@localhost:5432/ml_api_db"    #Adapter l'URL de connexion à la base de données PostgreSQL

engine = create_engine(DATABASE_URL)  #crée la connexions vers la base de données PGSQL

SessionLocal = sessionmaker(            #crée une session pour interagir avec la base de données
    autocommit=False,
    autoflush=False,
    bind=engine
)


from app.db_models import Base

Base.metadata.create_all(bind=engine)     
#Crée les tables dans la base de données si elles n'existent pas déjà, en utilisant les modèles définis dans db_models.py