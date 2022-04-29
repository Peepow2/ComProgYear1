import numpy as np
def animate_clear(board):
    new_board = np.array(board)
    row = np.min(board, axis = 1) != 0
    if np.sum(row) == 0: return []
    new_board[row, :] = 0
    
    OUT = [np.array(new_board)]
    R = board.shape[0]
    while R > 1 and np.sum(new_board[0:R] != 0) > 0:
        if np.sum(new_board[R-1]) == 0:
            new_board[1:R] = new_board[0:R-1]
            new_board[0] = 0
            OUT.append(np.array(new_board))
        else: R -= 1
    return OUT
