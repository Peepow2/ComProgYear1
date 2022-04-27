import numpy as np
def can_replace(board, shape): 
    return np.sum(board != 0) + np.sum(shape != 0) == np.sum(new_board != 0)
    
def animate_drop(board, shape, c):
    W, L = shape.shape
    OUT = list()       
    for i in range(-len(shape), len(board) - W + 1):
        new_board = np.array(board)
        if i < 0:
            new_board[0:-i, c:c + L] += shape[i:]
            if not can_replace(new_board, shape[i::]): return []   
        else:
            new_board[i:i + W, c:c + L] += shape
            if not can_replace(new_board, shape): break
            OUT.append(new_board)
    return OUT
