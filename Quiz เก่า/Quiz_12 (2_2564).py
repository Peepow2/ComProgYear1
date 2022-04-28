import numpy as np
def f1(v):
    return np.sum(v != np.arange(len(v))) == 0

def f2(u, v):
    return u + v[::-1]

def f3(M, v):
    return M * v

#----- DON'T modify any of the following lines -----
for k in range(int(input())):
    exec(input().strip())
