import numpy as np
def animate_clear(board):
    new_board = np.array(board)
    new_board[np.min(board, axis = 1) != 0, :] = 0
    nr = np.sum(np.sum(new_board, axis = 1) != 0) 
    pos = np.arange(len(board))
    
    OUT = list()
    OUT.append(np.array(new_board))
    
    while True:
        idx = np.sum(new_board, axis = 1) == 0
        if np.sum(idx) == 0: return []
        if np.sum(np.sum(new_board[-nr:], axis = 1) != 0) == nr: break
        
        c = pos[idx][-1]
        if c != len(board):
            new_board[1:c+1] = new_board[0:c]
            new_board[0] = 0
            OUT.append(np.array(new_board))       
    return OUT
