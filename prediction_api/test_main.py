# -*- coding: utf-8 -*-

import pytest
from fastapi.testclient import TestClient

from main import app
from mock_data import *

#############################################
### Group mock data for parametrized unit test
#############################################
TO_TEST_INVALID = [
    data_invalid_empty,
    data_invalid_typo,
    data_invalid_missing,
    data_invalid_wrongtype,
    data_invalid_negative,
]

VALID_MODELS = ["RandomForestClassifier", "GradientBoostingClassifier"]

client = TestClient(app)

#############################################
### For root
#############################################
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200, "Successful call is expected"
    assert "message" in response.json().keys(), "`message` key is expected in response"
    assert len(response.json()) == 1, "only one key is expected"


#############################################
### For /predict/
#############################################
def test_predict():
    response = client.get("/predict/", json=data_valid_base())
    response_json = response.json()

    assert response.status_code == 200

    # output shape and key check
    assert all(
        [key in response_json.keys() for key in ["prediction", "utc_ts", "model"]]
    )
    assert len(response_json) == 3, "3 outputs are expected"

    # valid model check
    assert response_json["model"] in VALID_MODELS

    # ouput type check
    assert isinstance(response_json["prediction"], int)
    assert isinstance(response_json["utc_ts"], int)
    assert isinstance(response_json["model"], str)


@pytest.mark.parametrize("test_object", TO_TEST_INVALID)
def test_predict_invalid(test_object):
    response = client.get("/predict/", json=test_object())
    response_json = response.json()

    assert response.status_code == 422


#############################################
### For /update_model/
#############################################
def test_update_model():
    response = client.put("/update_model/")
    response_json = response.json()

    assert response.status_code == 200

    # output shape and key check
    assert all(
        [key in response_json.keys() for key in ["old_model", "new_model", "utc_ts"]]
    )
    assert len(response_json) == 3, "3 outputs are expected"

    # ouput type check
    assert isinstance(response_json["old_model"], str)
    assert isinstance(response_json["new_model"], str)
    assert isinstance(response_json["utc_ts"], int)

    # valid model check
    assert response_json["old_model"] in VALID_MODELS
    assert response_json["new_model"] in VALID_MODELS


def test_update_model_wrongmethod():
    """
    We used get instead of put
    """
    response = client.get("/update_model/")
    response_json = response.json()

    assert response.status_code == 405


"""
# root
#     exact match
#     output keys

predict
    # output type
    # output keys

update_model
    multiple time
    output type
    output keys
    wrong method
"""
