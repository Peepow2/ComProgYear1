def convolute(M, K):
    ROW = len(M); COL = len(M[0])
    ANS = 0
    for i in range(ROW):
        for j in range(COL):
            ANS += M[i][j] * K[i][j]
    return ANS
exec(input().strip())
