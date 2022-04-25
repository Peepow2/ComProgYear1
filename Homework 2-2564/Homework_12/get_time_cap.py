import numpy as np
def ceil(a, b): return -(-a // b)
def get_time_cap(board, time_caps):
    pos = np.arange(1, len(board) + 1)
    n = pos[np.max(board, axis = 1) != 0]
    if len(n) == 0: n = len(board)
    else: n = int(n[0])
    return time_caps[ceil(n, (len(board) // len(time_caps))) - 1]
