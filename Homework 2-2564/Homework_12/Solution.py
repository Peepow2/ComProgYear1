""" Python Language
 # Task: Homework12 Tetris
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import numpy as np

def get_score(board):
    M = np.min(board, axis = 1)
    return np.sum(M != 0) * 40

def get_time_cap(board, time_caps):
    M = np.max(board, axis = 1)
    pos = np.arange(len(board))
    n = pos[M != 0]
    if len(n) == 0: return time_caps[-1]
    n = int(n[0])
    idx = ceil(n+1, len(board) // len(time_caps)) - 1 
    return time_caps[idx]

def rotate_right(shape):
    return np.array(shape.T[::, ::-1])

def rotate_left(shape):
    return np.array(shape.T[::-1, ::])

def animate_drop(board, shape, c):
    Zero = np.sum(board != 0) + np.sum(shape != 0)
    W, L = shape.shape
    OUT = list()
    for i in range(-shape.shape[0], len(board) - W + 1):
        new_board = np.array(board) 
        if i < 0:
          new_board[0:-i, c:c+L] += shape[i:]
          if np.sum(new_board != 0) != np.sum(board != 0) + np.sum(shape[i:] != 0): return []
        else:
          new_board[i:i+W, c:c+L] += shape
          if np.sum(new_board != 0) != Zero: break
          OUT.append(np.array(new_board))
    return OUT

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

def ceil(a, b): return -(-a//b)
