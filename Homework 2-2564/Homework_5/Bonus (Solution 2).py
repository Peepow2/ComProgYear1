# --------------------------------------------------- #
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
# --------------------------------------------------- #
# Bonus HW5
def least_pn_having(x):
    x = str(x); n = 1; L = len(x)
    while True:
        posnums = position_numbers(n)
        p = [1]
        for i in range(n):
            p += [next_partition_number(p, posnums)]
        if Longest_Common_Subsequence(str(p[n]), x) == L: return p[n]
        n += 1
# --------------------------------------------------- #
