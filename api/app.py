from fastapi import FastAPI
from pydantic import BaseModel

from predict import predict

app = FastAPI()


class Property(BaseModel):
    province: str
    type_property: str
    subtype_property: str
    livable_surface: int
    latitude: float
    longitude: float
    facades: int
    bedrooms: int
    bathrooms: int
    toilets: int
    terrace: int
    garden: int
    garage: int
    swimming_pool: int
    distance_from_train_stations_by_foot: int
    distance_from_elementary_school_by_foot: int
    distance_from_high_school_by_foot: int
    state_of_property: str
    heating_type: str
    sun_exposure: str
    epc_score: str
    flooding_area_type: str


@app.get("/")
def alive():
    return {"status": "alive"}


@app.post("/predict")
def predict_price(property: Property):
    result = predict(property.model_dump())

    return {
        "prediction": result,
        "status_code": 200
    }