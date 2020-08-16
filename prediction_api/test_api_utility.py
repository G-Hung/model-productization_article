# -*- coding: utf-8 -*-

"""
load_model
    test wrong input
    test output type, sklearn and Classifier

Predictor
    test __init__ items type

    test update multiple times: type & Classifier
"""

from pathlib import Path
from pickle import load

import pytest
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

from api_utility import Predictor


def test_init():
    predictor = Predictor(model_path=Path("model/rf_model.pkl"))

    assert isinstance(predictor.model, RandomForestClassifier)
    assert predictor.model_class_name == "RandomForestClassifier"
    assert len(predictor.model_candidates) == 2


def test_update_from_rf():
    """
    Start from RF
    Flip 6 times 
    * nth special about 6, just wanna flip multiple time and even number is easier to write
    """
    # start from rf, it should be rf now
    predictor = Predictor(model_path=Path("model/rf_model.pkl"))
    res = []
    for _ in range(6):
        predictor.update()
        res.append(predictor.model_class_name)

    assert res == ["GradientBoostingClassifier", "RandomForestClassifier"] * 3


def test_update_from_gb():
    """
    change the starting model from RF to GB
    Flip 6 times
    * nth special about 6, just wanna flip multiple time and even number is easier to write    
    """
    predictor = Predictor(model_path=Path("model/gb_model.pkl"))
    res = []
    for _ in range(6):
        predictor.update()
        res.append(predictor.model_class_name)

    assert res == ["RandomForestClassifier", "GradientBoostingClassifier"] * 3
