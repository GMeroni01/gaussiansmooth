import numpy as np
from gaussiansmooth.smooth import gaussian_smooth


def test_length():
    x = np.random.randn(200)
    y = gaussian_smooth(x, sigma=3)
    assert len(x) == len(y)


def test_smoothing_reduces_variance():
    np.random.seed(0)
    x = np.random.randn(2000)
    y = gaussian_smooth(x, sigma=5)
    assert np.var(y) < np.var(x)