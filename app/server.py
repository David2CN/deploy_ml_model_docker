import pickle
import numpy as np
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, conlist


app = FastAPI(title="Classify Flowers")


class Flower(BaseModel):
    batches: List[conlist(item_type=float, min_items=4, max_items=4)]


@app.get("/")
def index():
    return {"message": "server started successfully!"}


@app.on_event("startup")
def load_clf():
    with open("./app/flower.pkl", "rb") as f:
        global clf
        clf = pickle.load(f)


@app.post("/predict")
def predict(flower: Flower):
    batches = flower.batches
    batches = np.array(batches)
    pred = clf.predict(batches).tolist()
    return {"prediction": pred}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=80)
