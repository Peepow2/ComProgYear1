import numpy as np

def f1(M, c):
    return M * c

def f2(U, V):
    return np.sum(np.dot(U, V.T))

def f3(M):
    return M.T

def f4(x, y, dx, dy, k, R):
    neighbors = (x - x[k])**2 + (y - y[k])**2 <= R**2
    sx = np.sum(neighbors * dx)
    sy = np.sum(neighbors * dy)
    t = np.arctan2(sy, sx)
    return np.cos(t), np.sin(t)

#----- DON'T modify any of the following lines -----
for k in range(int(input())):
    exec(input().strip())
