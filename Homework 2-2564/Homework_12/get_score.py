import numpy as np
def get_score(board):
    return np.sum(np.min(board, axis = 1) != 0) * 40
