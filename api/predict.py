import joblib
import pandas as pd

model = joblib.load("xgboost_model.pkl")

def predict(property_data):
    df = pd.DataFrame([property_data])
    prediction = model.predict(df)

    return float(prediction[0])