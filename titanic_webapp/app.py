from turtle import rt
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from joblib import load
from input_model import ModelInput


from input_model import Gender
from func import check_prediction, convert_gender, journey_embarked

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/prediction")
async def predict(data:ModelInput):
    log_model = load("model.pkl")
    data_input = data.dict()
    pclass = int(data_input["pclass"])
    sex = convert_gender(data_input["sex"])
    age = int(data_input["age"])
    sibsp = int(data_input["sibsp"])
    parch = int(data_input["parch"])
    fare = float(data_input["fare"])
    embarked = journey_embarked(data_input["embarked"])
    prediction = check_prediction(log_model.predict([[pclass, sex, age, sibsp, parch, fare, embarked]]).tolist()[0])
    return {"prediction":prediction}



    