""" Python Language
 # Task: 02_StrList_06 (Add Vector)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
def convert(ss):
    ss = ss.strip()
    en = len(ss) - 1
    ss = ss[1:en]
    ss = ss.split(", ")
    return ss;

# Driver Code
str1 = str(input())
str2 = str(input())
str1 = convert(str1)
str2 = convert(str2)
ans1 = []
ans2 = []
ans3 = []

ans1.append(float(str1[0]))
ans1.append(float(str1[1]))
ans1.append(float(str1[2]))

ans2.append(float(str2[0]))
ans2.append(float(str2[1]))
ans2.append(float(str2[2]))

ans3.append((float(str1[0]) + float(str2[0])))
ans3.append((float(str1[1]) + float(str2[1])))
ans3.append((float(str1[2]) + float(str2[2])))
print(ans1, "+", ans2, "=", ans3)
