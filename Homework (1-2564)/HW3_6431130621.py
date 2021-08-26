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
    ss += xor(key[0], txt[0])
    ss += xor(key[1], txt[1])
    ss += xor(key[2], txt[2])
    ss += xor(key[3], txt[3])
    ss += xor(key[4], txt[4])
    ss += xor(key[5], txt[5])
    ss += xor(key[6], txt[6])
    ss += xor(key[7], txt[7])
    ss += xor(key[8], txt[8])
    ss += xor(key[9], txt[9])
    ss += xor(key[10], txt[10])
    ss += xor(key[11], txt[11])
    ss += xor(key[12], txt[12])
    ss += xor(key[13], txt[13])
    ss += xor(key[14], txt[14])
    ss += xor(key[15], txt[15])
    return ss
# End addkey

def fipl(c): # findreplace
    c2 = chr(ord(c) + 1)
    return c2
# End fpl

def subbyte(ss):
    _s = str("")
    _s += fipl(ss[0])
    _s += fipl(ss[1])
    _s += fipl(ss[2])
    _s += fipl(ss[3])
    _s += fipl(ss[4])
    _s += fipl(ss[5])
    _s += fipl(ss[6])
    _s += fipl(ss[7])
    _s += fipl(ss[8])
    _s += fipl(ss[9])
    _s += fipl(ss[10])
    _s += fipl(ss[11])
    _s += fipl(ss[12])
    _s += fipl(ss[13])
    _s += fipl(ss[14])
    _s += fipl(ss[15])
    return _s
# End subbyte

def shiftrow(txt):
    ss = str("")
    ss = txt[14:] + txt[:14]
    return ss;
# End shiftrow

def mixcolumn(t):
    # 231 112 311 123 3112
    ss = str("")
    ss += multi(t[0], "2")
 
    ss += multi(t[1], "3")
    ss += multi(t[2], "1")
    ss += multi(t[3], "1")  
    ss += multi(t[4], "1")
    ss += multi(t[5], "2")
    ss += multi(t[6], "3")  
    ss += multi(t[7], "1")
    ss += multi(t[8], "1")
    ss += multi(t[9], "1")
    ss += multi(t[10], "2")
    ss += multi(t[11], "3")
    ss += multi(t[12], "3")
    ss += multi(t[13], "1")
    ss += multi(t[14], "1")
    ss += multi(t[15], "2")
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
