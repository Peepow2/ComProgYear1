""" Python Language
 # Task: 02_StrList_07 (Decryption)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
str1 = str(input())
str1 = "x" + str1
n1 = str1[4] + str1[11] + str1[18] + str1[25] + str1[32];
n2 = str1[8] + str1[13] + str1[18] + str1[23] + str1[28];
s = str(int(n1) + int(n2) + 10000);
ss = int(s[-4]) + int(s[-3]) + int(s[-2]);
pss = str(s[-4]) + str(s[-3]) + str(s[-2]);
alpha = (ss%10) + 1
print(pss + chr(alpha+64))
