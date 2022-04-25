import numpy as np

def get_score(board):
    return np.sum(np.sum(board == 0, axis = 1) == 0) * 40

def get_time_cap(board, time_caps):
    pos = np.arange(1, len(board) + 1)
    n = pos[np.max(board, axis = 1) != 0]
    if len(n) == 0: n = len(board)
    else: n = int(n[0])
    return time_caps[ceil(n, (len(board) // len(time_caps))) - 1]

def rotate_right(shape):
    return np.array(shape.T[::, ::-1])

def rotate_left(shape):
    return np.array(shape.T[::-1, ::])

def animate_drop(board, shape, c):
    W, L = shape.shape
    OUT = list()
    for i in range(len(board) - W + 1):
        new_board = np.array(board)
        new_board[i:i + W, c:c + L] += shape
        if np.sum(board != 0) + np.sum(shape != 0) != np.sum(new_board != 0): break
        OUT.append(new_board)
    return OUT

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
        
        c = pos[idx][-1]
        if c != len(board):
            new_board[1:c+1] = new_board[0:c]
            new_board[0] = 0
            OUT.append(np.array(new_board))       
        if np.sum(np.sum(new_board[-nr:], axis = 1) != 0) == nr: break
    return OUT

def ceil(a, b): return (a // b) + (a % b)
