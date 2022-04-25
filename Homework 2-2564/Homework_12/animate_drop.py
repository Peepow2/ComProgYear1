import numpy as np
def animate_drop(board, shape, c):
    W, L = shape.shape
    OUT = list()
    for i in range(len(board) - W + 1):
        new_board = np.array(board)
        new_board[i:i + W, c:c + L] += shape
        if np.sum(board != 0) + np.sum(shape != 0) != np.sum(new_board != 0): break
        OUT.append(new_board)
    return OUT
