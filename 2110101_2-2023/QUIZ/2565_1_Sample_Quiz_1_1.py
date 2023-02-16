x = [int(e) for e in input().split()]
x.append(x[-1] + 1)
k = int(input())
c = 1
s = 0
for i in range(0, len(x)-1):
    if x[i] == x[i+1]:
        c += 1
    else:
        if c < k:
            s += x[i] * c
        c = 1
print(s)
