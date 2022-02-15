def least_pn_having(x):
    X = str(x); n = 1; 
    while True:
        posnums = position_numbers(n)
        p = [1]
        for i in range(n):
            p += [next_partition_number(p, posnums)]
        cnt = 0; pos = 0; PN = str(p[n])
        pos = PN.find(X[cnt])
        while pos != -1: 
            cnt += 1
            if cnt < len(X):  pos = PN.find(X[cnt], pos + 1)
            if cnt == len(X): return p[n]
        n += 1
