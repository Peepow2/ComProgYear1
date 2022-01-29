""" Python Language
 # Task: 02_StrList_08 (Decimal2Fraction)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import math as m
a, b, c = input().strip().split(",")
fac = int(a + b + c) - int(a + b);
dev = 10**(len(b + c)) - 10**(len(b))
GCD = m.gcd(fac, dev)
print(fac//GCD, "/", dev//GCD)
