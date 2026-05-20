# ML API Project

API de prédiction énergétique déployée avec FastAPI, PostgreSQL et GitHub Actions.

---

# Objectif du projet

Ce projet permet :

- de charger un modèle de Machine Learning
- d’exposer ce modèle via une API FastAPI
- de générer des prédictions énergétiques
- de stocker les prédictions dans PostgreSQL
- d’automatiser les tests avec GitHub Actions

---

# Technologies utilisées

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pytest
- GitHub Actions
- Scikit-learn

---

# Structure du projet

```bash
app/
├── api/
│   └── schemas.py
├── models/
│   ├── energy_model.pkl
│   └── model.py
├── database.py
├── db_models.py
├── main.py

tests/
└── test_api.py

.github/workflows/
└── ci.yml