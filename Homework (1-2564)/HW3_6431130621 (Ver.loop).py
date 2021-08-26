def mpt(x): # makeprintable
    return int(((x % 90) + 32 % 90))
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

def addkey(txt, key):
    ss = str("")
    for i in range(0,16):
        ss += xor(key[i], txt[i])
    return ss
# End addkey

def fipl(c): # findreplace
    c2 = chr(ord(c) + 1)
    return c2
# End fpl

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

# Driver Code
key = str(input().strip())
txt = str(input().strip())
ans = Hash(Hash(txt,key), key)
print(ans)

"""
key = "ABCDEFGHIJKLMNOP"
plaintext = "I LOVE PYTHON101"

OUTPUT = 4kZ;SR2U$;p2\<n\

ABCDEFGHIJKLMNOP
I LOVE PYTHON101
--> 4kZ;SR2U$;p2\<n\

Koraphat lumlert
Peerawich sodsua
--> 45* !>_#^#Hk2=Pp
"""
