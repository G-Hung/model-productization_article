# -*- coding: utf-8 -*-

"""
This script is used to run convert the raw data to train and test data
It is designed to be idempotent [stateless transformation]

Usage:
    python3 etl.py config.yml

"""

import logging
from pathlib import Path

import click
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from utility import parse_config, set_logger


@click.command()
@click.argument("config_file", type=str, default="scripts/config.yml")
def etl(config_file):
    """
    ETL function that load raw data and convert to train and test set

    Args:
        config_file [str]: path to config file

    Returns:
        None
    """

    ##################
    # configure logger
    ##################
    logger = set_logger("../log/etl.log")

    ##################
    # Load config from config file
    ##################
    logger.info(f"Load config from {config_file}")
    config = parse_config(config_file)

    raw_data_file = config["etl"]["raw_data_file"]
    processed_path = Path(config["etl"]["processed_path"])
    test_size = config["etl"]["test_size"]
    random_state = config["etl"]["random_state"]
    logger.info(f"config: {config['etl']}")

    ##################
    # Data transformation
    ##################
    logger.info("-------------------Start data transformation-------------------")
    wine = pd.read_csv(raw_data_file)

    bins = (2, 6.5, 8)
    group_names = ["bad", "good"]
    wine["quality"] = pd.cut(wine["quality"], bins=bins, labels=group_names)

    label_quality = LabelEncoder()

    wine["quality"] = label_quality.fit_transform(wine["quality"])
    logger.info("End data transformation")

    ##################
    # train test split & Export
    ##################
    # train test split
    logger.info("-------------------Train test split & Export-------------------")
    train, test = train_test_split(wine, test_size=test_size, random_state=random_state)

    # export data
    logger.info(f"write data to {processed_path}")
    train.to_csv(processed_path / "train.csv", index=False)
    test.to_csv(processed_path / "test.csv", index=False)
    logger.info(f"train: {train.shape}")
    logger.info(f"test: {test.shape}")
    logger.info("\n")


if __name__ == "__main__":
    etl()
