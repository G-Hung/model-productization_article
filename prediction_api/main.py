# -*- coding: utf-8 -*-

"""
This script is used to create prediction API using FastAPI

Usage:
    For local, run @ project root:
    It means, go to prediction_api folder, find a file called main, run it
    --reload means it should be interactive, autorefresh when you change the code
    Of coz this may not be the behavior you want in production, but we are testing~

    uvicorn prediction_api.main:app --reload
"""


import time
from pathlib import Path
from typing import Optional

import numpy as np
from fastapi import FastAPI, Query
from pydantic import BaseModel

from api_utility import Predictor


##################
# Define input data model
##################
class Sample(BaseModel):
    fixed_acidity: float = Query(..., gt=0)
    volatile_acidity: float = Query(..., gt=0)
    citric_acid: float = Query(..., gt=0)
    residual_sugar: float = Query(..., gt=0)
    chlorides: float = Query(..., gt=0)
    free_sulfur_dioxide: float = Query(..., gt=0)
    total_sulfur_dioxide: float = Query(..., gt=0)
    density: float = Query(..., gt=0)
    pH: float = Query(..., gt=0)
    sulphates: float = Query(..., gt=0)
    alcohol: float = Query(..., gt=0)


##################
# Import trained model
##################
# initialize the API with one of the models, rf in this case
predictor = Predictor(model_path=Path("model/rf_model.pkl"))

##################
# Prediction API
##################
app = FastAPI()


@app.get("/")
def read_root():
    """
    root, welcome message
    """

    return {
        "message": "this is root, prediction endpoint should be `predict`!, update endpoint should be `update_model`"
    }


@app.get("/predict/")
def predict_item(sample: Sample):
    tmp = sample.dict()
    res = predictor.model.predict(np.array(list(tmp.values())).reshape(1, -1))[0]
    return {
        "prediction": int(res),
        "utc_ts": int(time.time()),
        "model": predictor.model_class_name,
    }


@app.put("/update_model/")
def update_model():
    """
    Naive model update, when people call the API, just swap the models
    """
    old_model_name = predictor.model_class_name
    predictor.update()
    return {
        "old_model": old_model_name,
        "new_model": predictor.model_class_name,
        "utc_ts": int(time.time()),
    }
