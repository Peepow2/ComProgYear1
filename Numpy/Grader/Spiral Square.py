import numpy as np

def spiral_square(n): # n is a positive odd number
    table = np.zeros(n*n, int).reshape(n, n)
    length = n
    num = n * n

    Lcol = 0; Urow = 0
    Rcol = n; Drow = n

    while num > 0 and length > 0:
        table[Drow - 1, Lcol:Rcol] = range(num, num - length, -1)[::-1] # left
        num -= length - 1;

        table[Urow:Drow, Lcol] = range(num, num - length, -1)[::-1] #  up
        num -= length - 1; 

        table[Urow, Lcol:Rcol] = range(num, num - length, -1) # right
        num -= length - 1; length -= 1

        table[Urow:Drow - 1, Rcol - 1] = range(num, num - length, -1) # down
        num -= length

        length -= 1
        Lcol += 1; Urow += 1
        Rcol -= 1; Drow -= 1
    return table.tolist()

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip()) 
