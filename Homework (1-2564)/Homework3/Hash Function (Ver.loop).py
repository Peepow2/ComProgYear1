""" Python Language
 # Task: Homework 3 (PP's loop version)
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
def mpt(x): # makeprintable
    return int(((x % 90) + 32) % 90)
# End mpt

def multi(a, b):
    c = ord(a) * ord(b)
    re = mpt(c)
    return chr(re)
# End multi

def xor(a, b):
    a = int(ord(a)); b = int(ord(b));
    c = a ^ b
    d = mpt(c)
    return chr(d)
# End xor

def sbip():  # subinput
    s = str("")
    for i in range(32,91):
        s += chr(i)
    return s
# End sbip

def sbop():  # suboutput
    s = ""
    for i in range(33,91):
        s += chr(i)
    s += chr(32)
    return s
# End sbop

def fipl(c): # findreplace
    si = sbip(); so = sbop();
    idx = si.find(c)
    cc = so[idx]
    return cc
# End fipl

def addkey(txt, key):
    ss = str("")
    for i in range(0,16):
        ss += xor(key[i], txt[i])
    return ss
# End addkey

def subbyte(ss):
    s = str("")
    for i in range(0,16):
        s += fipl(ss[i])
    return s
# End subbyte

def shiftrow(txt):
    ss = str("")
    ss = txt[14:] + txt[:14]
    return ss;
# End shiftrow

def mixcolumn(t):
    # 231 112 311 123 3112
    fix = "2311123111233112"
    ss = str("")
    for i in range(0,16):
        ss += multi(t[i], fix[i])
    return ss;
# End shiftrow

def Hash(txt, key):
    code = addkey(txt, key)
    code = subbyte(code)
    code = shiftrow(code)
    code = mixcolumn(code)
    return code;
# End Hash

# Driver Code [main]
key = str(input().strip())
txt = str(input().strip())
ans = Hash(Hash(txt,key), key)
print(ans)
