""" Python Language
 # Task: Homework2 sinx
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""

import math 

def term_k(x,k):
    return ((-1)**k) * (x**(2*k + 1)) / math.factorial(2*k + 1)

def approximated_sin(x):
    value = 0
    value += term_k(x, 0) + term_k(x, 1) + term_k(x, 2)
    value += term_k(x, 3) + term_k(x, 4) + term_k(x, 5)
    value += term_k(x, 6) + term_k(x, 7) + term_k(x, 8)
    value += term_k(x, 9) + term_k(x, 10) + term_k(x, 11)
    value += term_k(x, 12) + term_k(x, 13) + term_k(x, 14)
    value += term_k(x, 15) + term_k(x, 16) + term_k(x, 17)
    return value
    
def find_eff(a,b):
    return abs(a-b) # math.sqrt((a-b)**2)

print(find_eff(math.sin(10), approximated_sin(10))) # ค่าที่ได้จะต้องน้อยกว่า 10**(-6)
