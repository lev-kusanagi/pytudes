import numpy as np


def taxicab_distance(p, q):
    """Return the taxicab distance between vectors p and q.
    Args:
    p, q: np.arrays with shape 1 x n
    """
    return np.sum(np.abs(p - q))


def form_vector(input):
    """Return vector v, resulting from applying the sequence of inputs in
    input
    Returns:
    v: two dimensional np.array
    """
    hdg = 'N'
    x = 0
    y = 0
    for i in input:
        hdg, x, y = compute_displacement(i, hdg)
    return np.array([x, y])

