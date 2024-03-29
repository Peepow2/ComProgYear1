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
    change = False
    for i in range(len(Q)):
        if M > 0 and MAXN[i][1] < Q[i][1]:
            MAXN[i][1] += 1
            M -= 1
            change = True
    if not change: break
    
for i in range(len(MAXN)):
    print(MAXN[i][0], MAXN[i][1])
# -------------------------------------------------------- #
# Quiz_2_2 Matching Rule
def match(s, cs):    
    # a[bc]d(efg) --> ['a', '[bc]', 'd', '(efg)']
    word = list()
    i = j = 0
    while i < len(cs) and i != -1:
        if cs[i] == '[':
            j = cs.find(']', i)        
        elif cs[i] == '(':
            j = cs.find(')', i)
        else:
            j = i
        word.append(cs[i:j+1])
        i = j + 1
    
    if len(word) != len(s): return False
    for i in range(len(word)):
        if '[' in word[i] and ']' in word[i]:
            if s[i] not in word[i]: return False
        elif '(' in word[i] and ')' in word[i]:
            if s[i] in word[i]: return False
        elif s[i] != word[i] and cs[i] != '?': return False
    return True

# ห้ามลบหรือแก้ไขบรรทัดด้านล่างนี้้
exec(input().strip())
# -------------------------------------------------------- #
# Quiz_2_3 Complex Replace
def complex_replace(s,k_strs,r_strs):
    minN = len(s) + 10
    word = ''
    Found = True
    for i in range(len(k_strs)):
        idx = s.find(k_strs[i])
        if idx != -1 and idx < minN:
            minN = idx
            word = r_strs[i]
            Found = True
        
    if Found:
        return s[:minN] + '<' + word + '>' + s[minN + len(word):]
    return s

exec(input().strip())
