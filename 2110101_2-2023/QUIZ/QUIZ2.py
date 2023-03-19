# Quiz_2_1 Small Lot First
Q = list()
M = int(input())

CC = input().strip().split()
while len(CC) != 1:
    Q.append([CC[0], int(CC[1])])
    CC = input().strip().split()
    
MAXN = list()
for i in range(len(Q)):
    MAXN.append([Q[i][0], 0])

while M > 0:
    for i in range(len(Q)):
        if M - 1 >= 0 and MAXN[i][1] < Q[i][1]:
            MAXN[i][1] += 1
            M -= 1
            
    for i in range(len(Q)):
        if MAXN[i][1] < Q[i][1]: continue
            
for i in range(len(MAXN)):
    print(MAXN[i][0], MAXN[i][1])
# -------------------------------------------------------- #
# Quiz_2_2 Matching Rule
def match(s, cs):
    # ? check
    if "(" not in cs and "[" not in cs:
        if len(s) != len(cs): return False
        for i in range(len(cs)):
            if (s[i] != cs[i]) and cs[i] != '?':
                return False
            
    # () [] check
    word = list()
    B = False
    for i in range(len(cs)):
        if B: word[-1] += cs[i]
        else: word.append(cs[i])
        
        if cs[i] in '[(':
            B = True
        elif cs[i] in '])':
            B = False
   
    if len(word) != len(s): return False
    for i in range(len(word)):
        if '[' in word[i] and ']' in word[i]:
            if s[i] not in word[i]: return False
        if '(' in word[i] and ')' in word[i]:
            if s[i] in word[i]: return False      
    return True

# ห้ามลบหรือแก้ไขบรรทัดด้านล่างนี้
exec(input().strip())

# -------------------------------------------------------- #
# Quiz_2_3 Complex Replace
def complex_replace(s,k_strs,r_strs):
    L = list()
    for i in range(len(k_strs)):
        if s.find(k_strs[i]) != -1:
            L.append(s.find(k_strs[i]))
        else:
            L.append(9999999999) # set to infinity
    
    if len(L) != 0 and L.count(9999999999) != len(L):
        Min = min(L)
        idx = L.index(Min)
        return s[:Min] + '<' + r_strs[idx] + '>' + s[Min+len(k_strs[idx]):]
    return s

exec(input().strip())
