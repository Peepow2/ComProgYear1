""" Python Language
 # Task: 01_Expr_06 (Durtion)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = (h1 * 60 * 60) + (m1 * 60) + s1
t2 = (h2 * 60 * 60) + (m2 * 60) + s2
dt = (t2 - t1) % 86400
dh = dt // (60 * 60)
dt -= dh * 60 * 60
dm = dt // 60
dt -= dm * 60
ds = dt
print(str(dh)+":"+str(dm)+":"+str(ds))
