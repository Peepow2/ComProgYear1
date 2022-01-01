# 01_Expr_★_Stirling_Factorial
import math as m
n = int(input())
pi = m.pi
e = m.e
lower = m.sqrt(2*pi) * (n**(n+0.5)) * (e**(-n+(1/(12*n+1))));
upper = m.sqrt(2*pi) * (n**(n+0.5)) * (e**(-n+(1/(12*n))));
print(lower); print(upper)
# ---------------------------------------------------------------------------#

# 01_Expr_★_Quadratic_Root
import math as m
a = float(input())
b = float(input())
c = float(input())

x1 = (-b - m.sqrt((b*b)-(4*a*c))) / (2*a)
x2 = (-b + m.sqrt((b*b)-(4*a*c))) / (2*a)

x1 = round(x1, 3)
x2 = round(x2, 3) 
print(x1, x2)
# ---------------------------------------------------------------------------#

# 01_Expr_★★_An_Expression.
import math as m
w = float(input())
h = float(input())
MOS = m.sqrt(w*h)/60
HAY = 0.024265 * (w**0.5378) * (h**0.3964)
BOY = 0.0333 * (w**(0.6157 - 0.0188*m.log(w,10))) * (h**0.3)
print(MOS)
print(HAY)
print(BOY)
# ---------------------------------------------------------------------------#

# 01_Expr_★★_Body_Surface_Area
import math as m
w = float(input())
h = float(input())
MOS = m.sqrt(w*h)/60
HAY = 0.024265 * (w**0.5378) * (h**0.3964)
BOY = 0.0333 * (w**(0.6157 - 0.0188*m.log(w,10))) * (h**0.3)
print(MOS)
print(HAY)
print(BOY)
