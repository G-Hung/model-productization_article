# -*- coding: utf-8 -*-

from pathlib import Path
from pickle import load


class Predictor:
    """
    Preictor class that host the model and metadata
    """

    def __init__(self, model_path: Path):
        """
        Initialize the model with either RF or GB
        """
        self.model = load_model(model_path)
        self.model_class_name = str(self.model.__class__.__name__)
        # yeah, I know this is hardcoded, maybe it should be dynamic
        # in real case but let's keep it simple first~
        self.model_candidates = {
            "RandomForestClassifier": Path("model/rf_model.pkl"),
            "GradientBoostingClassifier": Path("model/gb_model.pkl"),
        }
        assert (
            self.model_class_name in self.model_candidates.keys()
        ), "Should be either RF or GB"

    def update(self):
        """
        swap the model if this method is called, currently for simplicity, 
        there are only 2 models, RF and GB
        """
        if self.model_class_name == "RandomForestClassifier":
            self.model = load_model(self.model_candidates["GradientBoostingClassifier"])
            self.model_class_name = str(self.model.__class__.__name__)
        elif self.model_class_name == "GradientBoostingClassifier":
            self.model = load_model(self.model_candidates["RandomForestClassifier"])
            self.model_class_name = str(self.model.__class__.__name__)


def load_model(model_path: Path):
    """
    Load pretrained model pkl

    Args:
        model_path [Path]: model path in Path format, eg: Path("model/rf_model.pkl")
    
    Returns:
        trained sklearn model

    Usage:
        trained_model = load_model(Path("../model/rf_model.pkl"))
    """
    assert isinstance(model_path, Path), "Path object is expected"
    with open(model_path, "rb") as f:
        trained_model = load(f)
    return trained_model
