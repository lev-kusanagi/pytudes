import numpy as np


def taxicab_distance(p, q):
    """Return the taxicab distance between vectors p and q.
    Args:
    p, q: np.arrays with shape 1 x n
    """
    return np.sum(np.abs(p - q))
