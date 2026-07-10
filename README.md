# Immo Eliza Deployment

## Description
API allowing real estate price predictions using a trained machine learning model.

## Technologies
- FastAPI
- Scikit-Learn
- XGBoost
- Pandas
- Joblib

## Run locally

pip install -r requirements.txt

uvicorn app:app --reload

## Endpoints

GET /

Returns:
{
    "status": "alive"
}

POST /predict

### Input:
{
  "province": "brussels",
  "type_property": "house",
  "subtype_property": "mansion",
  "livable_surface": 180,
  "latitude": 50.85,
  "longitude": 4.35,
  "facades": 2,
  "bedrooms": 4,
  "bathrooms": 2,
  "toilets": 2,
  "terrace": 1,
  "garden": 1,
  "garage": 1,
  "swimming_pool": 0,
  "distance_from_train_stations_by_foot": 500,
  "distance_from_elementary_school_by_foot": 300,
  "distance_from_high_school_by_foot": 700,
  "state_of_property": "to_be_renovated",
  "heating_type": "gas",
  "sun_exposure": "south",
  "epc_score": "B",
  "flooding_area_type": "no_flooding_area"
}

### Output:
{
    "prediction": 740097.43,
    "status_code": 200
}
