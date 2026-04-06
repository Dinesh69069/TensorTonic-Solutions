import numpy as np

def sigmoid(x):
    matrix = np.array(x , dtype = float)  

    return 1/(1 + np.exp(-matrix))

