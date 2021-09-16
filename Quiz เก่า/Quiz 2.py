import math as m
x = int(input())
ans = x**(2 * (m.log10(x + 4) ) ) - (x / 10) - x
print(round(ans, 6))
