a = int(input())
b = int(input())
c = int(input())
F = 1
if a < 100:
    while not a/(b*c) > 20 or F == 1:
        F += 1
        if b < c:
            a += b*b + c*c
        else:
            break
        if a % 10 == 5:
            break
        if a % 2 == 0:
            b += 1
        else:
            c -= 1
else:
    if a < b:
        if b < c:
            a = a + 3
            b = a + c
            c = b + a
        else:
            if a < c:
                a = 2 * a
                b = a + b
                c = b + c
            else:
                a = c + a
                b = 2 * b
                c = b - a
    else:
        if c > a:
            a = 3 * b
            b = c + a
            c = a + b
        else:
            if b > c:
                a = b + c
                b = 7 * a
                c = b - a
            else:
                a = c - 5
                b = a - b
                c = 3 * b
print(a, b, c)
