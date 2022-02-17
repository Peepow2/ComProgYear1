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
def Longest_Common_Subsequence(str1, str2):
    str1 = " " + str1; str2 = " " + str2; 
    L1 = len(str1); L2 = len(str2);
    LCS = [[0] * (L2) for i in range(L1)]
    for i in range(L1):
        for j in range(L2):
            if i == 0 or j == 0 :
                LCS[i][j] = 0
            elif str1[i] == str2[j]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j] , LCS[i][j-1])
    return LCS[L1-1][L2-1]
# --------------------------------------------------------- #
# Bonus HW5
def least_pn_having(x):
    x = str(x); L = len(x); 
    posnums = [1]; p = [1];
    while True:
        posnums.append(next_position_number(posnums))
        p.append(next_partition_number(p, posnums))
        if Longest_Common_Subsequence(str(p[-1]), x) == L: return p[-1]
# --------------------------------------------------- #
