# --------------------------------------------------------- #
def next_position_number(posnums):
    L = len(posnums)
    r = (L // 2) + 1; s = (L + 1) % 2 
    return r * (3 * r + (-1) ** s) // 2
# --------------------------------------------------------- #
def next_partition_number(p, posnums):
    m = len(p)
    step = ans = idx = 0
    while posnums[idx] <= m:
        ans += (p[m-posnums[idx]] * (-1) ** int(step))
        step += 0.5; idx += 1
    return ans
# --------------------------------------------------------- #
def least_pn_having(x):
    x = str(x); L = len(x); 
    posnums = [1]; p = [1];
    while True:
        posnums.append(next_position_number(posnums))
        p.append(next_partition_number(p, posnums))
        PN = str(p[-1]); cnt = 0
        pos = PN.find(x[0], 0)
        while pos != -1:
            cnt += 1
            if cnt == L: return p[-1]
            pos = PN.find(x[cnt], pos + 1)
# --------------------------------------------------------- #
