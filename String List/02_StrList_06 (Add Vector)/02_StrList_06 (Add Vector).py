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
v1 = str(input())
v2 = str(input())
v1 = convert(v1)
v2 = convert(v2)

a0 = str(float(v1[0]) + float(v2[0]))
a1 = str(float(v1[1]) + float(v2[1]))
a2 = str(float(v1[2]) + float(v2[2]))
ans = str("")
ans += "[" + str(float(v1[0])) + ", " + str(float(v1[1])) + ", " + str(float(v1[2])) + "]"
ans += " + "
ans += "[" + str(float(v2[0])) + ", " + str(float(v2[1])) + ", " + str(float(v2[2])) + "]"
ans += " = "
ans += "[" + a0 + ", " + a1 + ", " + a2 + "]"
print(ans)
