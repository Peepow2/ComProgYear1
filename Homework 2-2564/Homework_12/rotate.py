import numpy as np

def rotate_right(shape):
    return np.array(shape.T[::, ::-1])

def rotate_left(shape):
    return np.array(shape.T[::-1, ::])
