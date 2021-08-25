""" Python Language
 # Task: 02_StrList_08 (Decimal2Fraction)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
import math as m
str1 = input().strip()
str1 = str1.split(",")
a = str(str1[0]); b = str(str1[1]); c = str(str1[2]);
leb = len(b); lec = len(c);
num1 = int(a + b);
num2 = int(a + b + c);
fac = num2 - num1;
dev = 10**(leb + lec) - 10**(leb)
GCD = m.gcd(fac, dev)
fac //= GCD; dev //= GCD; 
print(fac,"/",dev)

