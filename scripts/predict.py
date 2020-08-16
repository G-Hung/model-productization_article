# -*- coding: utf-8 -*-

"""
This script is used to do prediction based on trained model

Usage:
    python3 ./scripts/predict.py

"""
import logging
from pathlib import Path

# from cloudpickle import load
from pickle import load

import click
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

from utility import load_data, parse_config, set_logger


@click.command()
@click.argument("config_file", type=str, default="scripts/config.yml")
def predict(config_file):
    """
    Main function that runs predictions

    Args:
        config_file [str]: path to config file

    Returns:
        None
    """
    ##################
    # configure logger
    ##################
    logger = set_logger("./log/predict.log")

    ##################
    # Load config from config file
    ##################
    logger.info(f"Load config from {config_file}")
    config = parse_config(config_file)

    model_path = Path(config["predict"]["model_path"])
    processed_test = config["predict"]["processed_test"]
    predicted_file = config["predict"]["predicted_file"]
    export_result = config["predict"]["export_result"]

    logger.info(f"config: {config['predict']}")

    ##################
    # Load model & test set
    ##################
    # Load model
    logger.info(f"-------------------Load the trained model-------------------")
    with open(model_path, "rb") as f:
        trained_model = load(f)

    # Load test set
    logger.info(f"Load the test data from {processed_test}")
    X, y, cols = load_data(processed_test)
    logger.info(f"cols: {cols}")
    logger.info(f"X: {X.shape}")
    logger.info(f"y: {y.shape}")

    ##################
    # Make prediction and evaluate
    ##################
    logger.info(f"-------------------Predict and evaluate-------------------")
    y_hat = trained_model.predict(X)
    logger.info(f"Classification report: \n {classification_report(y, y_hat)}")
    output = pd.DataFrame(y)
    output["prediction"] = y_hat
    if export_result:
        output.to_csv(predicted_file, index=False)
        logger.info(f"Export prediction to : {predicted_file}")


if __name__ == "__main__":
    predict()
