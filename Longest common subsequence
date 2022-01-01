def LCS(s1, s2):
    l1 = len(s1) + 1; l2 = len(s2) + 1;
    
    count_LCS = [[0]*l2 for i in range(0, l1)]
    
    for i in range(1, l1):
        for j in range(1, l2):
            if (i == 0 or j == 0):
                count_LCS[i][j] = 0
                
            elif s1[i-1] == s2[j-1]:
                count_LCS[i][j] += count_LCS[i-1][j-1] + 1
                
            else:
                count_LCS[i][j] = max(count_LCS[i-1][j], count_LCS[i][j-1])
    # print(count_LCS)
    return count_LCS[l1-1][l2-1]

# --------------------------- Driver Code ---------------------------
str1, str2 = input(), input()
n = LCS(str1, str2)
print(n)
