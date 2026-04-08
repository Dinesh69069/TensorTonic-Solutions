import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    mx = np.array(x)
    my = np.array(y)
    return (mx * my).sum()