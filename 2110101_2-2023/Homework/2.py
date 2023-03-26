# Riemann sum functions
# ---------------------------- #
def riemann_left(f, a, b, n):
    dx = (b - a) / n
    S = 0
    for i in range(n):
        S += f(a + (i*dx))
    return S * dx

def riemann_right(f, a, b, n):
    dx = (b - a) / n
    S = 0
    for i in range(1, n+1):
        S += f(a + (i*dx))
    return S * dx

def riemann_mid(f, a, b, n):
    dx = (b - a) / n
    S = 0
    for i in range(1, 2*n, 2):
        S += f(a + (i*dx)/2)
    return S * dx

def riemann_trap(f, a, b, n):
    dx = (b - a) / n
    S = 0
    for i in range(1, n):
        S += 2 * f(a + (i*dx))
    return 0.5 * (S + f(a) + f(b)) * dx
# ---------------------------- #
def estimate(riemann_sum_function, f, a, b, precision):
    k = 1
    r2 = round(riemann_sum_function(f, a, b, k), precision)
    r1 = r2 - 1
    while r2 != r1: 
      r1 = r2
      r2 = round(riemann_sum_function(f, a, b, k + 1), precision)
      k += 1
    return [r1, k - 1]
