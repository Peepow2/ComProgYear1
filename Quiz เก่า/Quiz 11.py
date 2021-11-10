D = dict()
n = int(input())
for i in range(n):
    Name, sport = input().strip().split()
    sport = sport.split(",")
    if Name not in D: D[Name] = set()
    for s in sport: D[Name].add(s)

N = input().strip()
while N != 'q':
    N1, N2 = N.split()
    print(list(sorted(D[N1] & D[N2])))
    N = input().strip()
