""" Python Language
 # Task: 02_StrList_08 (Decimal2Fraction)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import math as m
str1 = input().strip().split(",")
a, b, c = str1[0], str1[1], str1[2];
leb = len(b); lec = len(c);
fac = int(a + b + c) - int(a + b);
dev = 10**(leb + lec) - 10**(leb)
GCD = m.gcd(fac, dev)
print(fac//GCD,"/",dev//GCD)

