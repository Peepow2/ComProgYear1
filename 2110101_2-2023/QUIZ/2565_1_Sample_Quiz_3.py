N = int(input())
puk = dict()
vote = dict()
sorted_puk = list()

N = int(input())
for i in range(N):
    x = input().strip()
    puk[x] = list()
    sorted_puk.append(x)
    
N = int(input())
for i in range(N):
    Name, P = input().strip().split()
    puk[P].append(Name)
    
N = int(input())
for i in range(N):
    Name, v = input().strip().split()
    vote[Name] = v


for k in sorted_puk:
    YNX = {'Y': [], 'N': [], 'X': []}
    for Name in sorted(puk[k]):
        if Name not in vote: continue
        YNX[vote[Name]].append(Name)
    
    YNX = sorted([(len(YNX['Y']), YNX['Y']), \
                  (len(YNX['N']), YNX['N']), \
                  (len(YNX['X']), YNX['X'])])[::-1]
    
    print(k)
    if YNX[0][0] != YNX[1][0] and YNX[1][0] + YNX[2][0] == 0:
        print('No cobra')
    
    elif YNX[0][0] == YNX[1][0]:
        print('Inconclusive')
    
    else:
        print(', '.join(sorted(YNX[1][1] + YNX[2][1])))