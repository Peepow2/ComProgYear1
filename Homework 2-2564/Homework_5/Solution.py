def position_numbers(n):
    pos_num = list()
    t = r = s = 1
    while t <= n:
        t = (int(r) * (3 * int(r) + ((-1)**s))) // 2
        pos_num.append(int(t))
        r += 0.5; s = (s + 1) % 2
    return pos_num
# --------------------------------------------------- #
def next_partition_number(p, posnums):
    m = len(p)
    step = idx = ans = 0
    while posnums[idx] <= m:
        ans += (p[m-posnums[idx]] * (-1) ** int(step))
        step += 0.5; idx += 1
    return ans
# --------------------------------------------------- #
def rhs_of_pn(n, posnums):
    pn_equation = ""
    step = 1.5; idx = 0
    while posnums[idx] <= n:
        pn_equation += "p(" + str(n - posnums[idx]) + ") " + chr(44 + (-1)**int(step)) + " "  
        idx += 1; step += 0.5
    return pn_equation[:-3]
# --------------------------------------------------- #
# ไม่ต้องแก้ไขอะไรใด ๆ ในชุดคำสั่งข้างล่างนี้
def main(n, show_rhs):
    n = int(n)
    posnums = position_numbers(n)
    p = [1]  # p[0] = 1
    for m in range(1, n+1):
        p += [ next_partition_number(p, posnums) ]
    out = 'p(' + str(n) + ') = '
    if show_rhs == 'Y':
        out += rhs_of_pn(n, posnums) + ' = '
    out += str(p[n])
    print(out)
# --------------------------------------------------- #
# Bonus HW5
def least_pn_having(x):
    X = str(x); n = 1; 
    while True:
        posnums = position_numbers(n)
        p = [1]
        for i in range(1, n + 1):
            p += [next_partition_number(p, posnums)]
        cnt = 0; PN = str(p[n])
        pos = PN.find(X[0], 0)
        while pos != -1: 
            cnt += 1
            if cnt == len(X): return p[n]
            if cnt < len(X):  pos = PN.find(X[cnt], pos + 1)
        n += 1
# --------------------------------------------------------- #