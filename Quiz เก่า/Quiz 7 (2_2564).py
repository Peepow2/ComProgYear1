def f1(d):
    return sum(d)

def f2():
    n = int(input())
    return [int(input()) for i in range(n)]

def f3(x, e):
    List = list()
    for i in x:
        if i % e == 0: List.append(i)
    return List

def f4():
    L = f2()
    print(f1(f3(L, 2)) - f1(f3(L, 3)) - f1(f3(L, 5)))
