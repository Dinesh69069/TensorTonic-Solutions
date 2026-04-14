import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    xa = np.array(x)
    ya = np.array(y)
    return float(np.sum(np.abs(xa-ya)))