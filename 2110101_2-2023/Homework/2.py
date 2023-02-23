# Riemann sum functions
#-----------------------------
def riemann_left(f, a, b, n):
    return sum([(f(a + (i * ((b - a) / n))) * ((b - a) / n)) for i in range(n)])

def riemann_right(f, a, b, n):
    return sum([(f(a + (i * ((b - a) / n))) * ((b - a) / n)) for i in range(1, n+1)])

def riemann_mid(f, a, b, n):
    return sum([(f(a + ((i + 0.5) * ((b - a) / n))) * ((b - a) / n)) for i in range(n)])

def riemann_trap(f, a, b, n):
    return sum([(0.5 * ((b - a) / n)) * (f(a + (i * ((b - a) / n))) + f(a + ((i + 1) * ((b - a) / n)))) for i in range(n)])

#----------------------------
def estimate(riemann_sum_function, f, a, b, precision):
    k = 1
    r2 = round(riemann_sum_function(f, a, b, k), precision)
    r1 = r2 - 1
    while r2 != r1: 
      r1 = r2
      r2 = round(riemann_sum_function(f, a, b, k + 1), precision)
      k += 1
    return [r1, k - 1]
