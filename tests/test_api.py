from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    payload = {
        "BuildingType": "NonResidential",
        "PrimaryPropertyType": "Office",
        "Neighborhood": "DOWNTOWN",
        "PropertyGFATotal_log": 10,
        "BuildingAge": 20,
        "IsMultiBuilding": 0,
        "NumberofBuildingsBin": "1",
        "FloorsBin": "1-2",
        "GFA_per_Floor": 1000,
        "ParkingRatio": 0.1,
        "Electricity_ratio": 0.5,
        "Gas_ratio": 0.3,
        "Steam_ratio": 0.2,
        "office_services_ratio": 0.1,
        "parking_ratio": 0.1,
        "retail_ratio": 0.1,
        "food_ratio": 0.1,
        "education_ratio": 0.1,
        "lodging_ratio": 0.1,
        "multifamily_housing_ratio": 0.1,
        "healthcare_ratio": 0.1,
        "public_services_ratio": 0.1,
        "entertainment_ratio": 0.1,
        "gym_ratio": 0.1,
        "swimming_pool_ratio": 0.1,
        "services_ratio": 0.1,
        "non_refrigerated_warehouse_ratio": 0.1,
        "refrigerated_warehouse_ratio": 0.1,
        "distribution_center_ratio": 0.1,
        "self_storage_ratio": 0.1,
        "manufacturing_industrial_ratio": 0.1,
        "data_center_ratio": 0.1,
        "laboratory_ratio": 0.1,
        "utility_ratio": 0.1,
        "other_ratio": 0.1,
        "ENERGYSTARScore": 50
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()