import pytest
import sklearn

from train import initiate_model


def test_initiate_model():

    # valid case
    ensemble_model = "RandomForestClassifier"
    model_config = {"n_estimators": 300}
    model = initiate_model(ensemble_model, model_config)

    assert ensemble_model in str(model.__class__), "right class should be picked"
    assert (
        model.n_estimators == model_config["n_estimators"]
    ), "right parameters should be loaded"

    # invalid case
    ensemble_model = "KNeighborsClassifier"
    with pytest.raises(NameError):
        initiate_model(ensemble_model, model_config)
