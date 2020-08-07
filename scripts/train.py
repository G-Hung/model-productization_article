# -*- coding: utf-8 -*-

"""
This script is used to train and export ML model according to config

Usage:
    python3 train.py config.yml

"""

import logging
from pathlib import Path

# from cloudpickle import dump
from pickle import dump

import click
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

from utility import load_data, parse_config, set_logger


@click.command()
@click.argument("config_file", type=str, default="scripts/config.yml")
def train(config_file):
    """
    Main function that trains & persists model based on training set

    Args:
        config_file [str]: path to config file

    Returns:
        None
    """
    ##################
    # configure logger
    ##################
    logger = set_logger("../log/train.log")

    ##################
    # Load config from config file
    ##################
    logger.info(f"Load config from {config_file}")
    config = parse_config(config_file)

    processed_train = Path(config["train"]["processed_train"])
    ensemble_model = config["train"]["ensemble_model"]
    model_config = config["train"]["model_config"]
    model_path = Path(config["train"]["model_path"])

    logger.info(f"config: {config['train']}")

    ##################
    # Load data
    ##################
    logger.info(f"-------------------Load the processed data-------------------")
    X, y, cols = load_data(processed_train)
    logger.info(f"cols: {cols}")
    logger.info(f"X: {X.shape}")
    logger.info(f"y: {y.shape}")

    ##################
    # Set & train model
    ##################
    # Load model
    # Limited to sklearn ensemble for the moment
    logger.info(f"-------------------Initiate model-------------------")
    model = initiate_model(ensemble_model, model_config)

    # Train model
    logger.info(f"Train model using {ensemble_model}, {model_config}")
    model.fit(X, y)
    logger.info(f"Train score: {model.score(X, y)}")
    logger.info(
        f"CV score: {cross_val_score(estimator = model, X = X, y = y, cv = 5).mean()}"
    )
    ##################
    # Persist model
    ##################

    logger.info(f"-------------------Persist model-------------------")
    model_path.parent.mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        dump(model, f)
    logger.info(f"Persisted model to {model_path}")


def initiate_model(ensemble_model, model_config):
    """
    initiate model using eval, implement with defensive programming

    Args:
        ensemble_model [str]: name of the ensemble model
    
    Returns:
        [sklearn.model]: initiated model
    """
    if ensemble_model in dir(sklearn.ensemble):
        return eval("sklearn.ensemble." + ensemble_model)(**model_config)
    else:
        raise NameError(f"{ensemble_model} is not in sklearn.ensemble")


if __name__ == "__main__":
    train()
