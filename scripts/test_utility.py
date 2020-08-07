import numpy as np
import pandas as pd
import pytest

from utility import load_data


def test_load_data():
    X, y, cols = load_data("data/winequality.csv")

    # type check
    assert isinstance(X, np.ndarray)
    assert isinstance(y, pd.core.series.Series)
    assert isinstance(cols, list)

    # shape check
    assert X.shape[0] == y.shape[0], "# row of features = # rows of target"
    assert X.shape[1] >= 1, "# features >= 1"
    assert len(cols) == 12, "data should have 12 cols"
