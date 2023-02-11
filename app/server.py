import pickle
import uvicorn
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Classify Flowers")

class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.on_event("startup")
def load_clf():
    with open("./app/flower.pkl", "rb") as f:
        global clf
        clf = pickle.load(f)


@app.post("/predict")
def predict(flower: Flower):
    data_point = np.array([[
        flower.sepal_length,
        flower.sepal_width,
        flower.petal_length,
        flower.petal_width
    ]])

    pred = clf.predict(data_point).tolist()[0]
    return {"prediction": pred}


if __name__ == "__main__":
    uvicorn.run(app)