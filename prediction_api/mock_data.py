"""
example data
    # valid
    # typo
    # required / missing    
    # wrong type
    # negative
"""


def data_valid_base():
    """
    Valid input
    """
    return {
        "fixed_acidity": 10.5,
        "volatile_acidity": 0.51,
        "citric_acid": 0.64,
        "residual_sugar": 2.4,
        "chlorides": 0.107,
        "free_sulfur_dioxide": 6.0,
        "total_sulfur_dioxide": 15.0,
        "density": 0.9973,
        "pH": 3.09,
        "sulphates": 0.66,
        "alcohol": 11.8,
    }


def data_invalid_empty():
    return {}


def data_invalid_typo():
    """
    Invalid input, fixed_acidity is CAPITALIZED
    """
    return {
        "FIXED_ACIDITY": 10.5,
        "volatile_acidity": 0.51,
        "citric_acid": 0.64,
        "residual_sugar": 2.4,
        "chlorides": 0.107,
        "free_sulfur_dioxide": 6.0,
        "total_sulfur_dioxide": 15.0,
        "density": 0.9973,
        "pH": 3.09,
        "sulphates": 0.66,
        "alcohol": 11.8,
    }


def data_invalid_missing():
    """
    Invalid input, fixed_acidity is missing
    """
    return {
        "volatile_acidity": 0.51,
        "citric_acid": 0.64,
        "residual_sugar": 2.4,
        "chlorides": 0.107,
        "free_sulfur_dioxide": 6.0,
        "total_sulfur_dioxide": 15.0,
        "density": 0.9973,
        "pH": 3.09,
        "sulphates": 0.66,
        "alcohol": 11.8,
    }


def data_invalid_wrongtype():
    """
    Invalid input, fixed_acidity is str
    """
    return {
        "fixed_acidity": "wrong type",
        "volatile_acidity": 0.51,
        "citric_acid": 0.64,
        "residual_sugar": 2.4,
        "chlorides": 0.107,
        "free_sulfur_dioxide": 6.0,
        "total_sulfur_dioxide": 15.0,
        "density": 0.9973,
        "pH": 3.09,
        "sulphates": 0.66,
        "alcohol": 11.8,
    }


def data_invalid_negative():
    """
    Invalid input, fixed_acidity is negative
    """
    return {
        "fixed_acidity": -42,
        "volatile_acidity": 0.51,
        "citric_acid": 0.64,
        "residual_sugar": 2.4,
        "chlorides": 0.107,
        "free_sulfur_dioxide": 6.0,
        "total_sulfur_dioxide": 15.0,
        "density": 0.9973,
        "pH": 3.09,
        "sulphates": 0.66,
        "alcohol": 11.8,
    }
