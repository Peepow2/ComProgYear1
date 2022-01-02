# 02-StrLst_★_CitizenID
ID = str(input())
ans = int(0)
ans += 13*int(ID[0]) + 12*int(ID[1]) + 11*int(ID[2]) + 10*int(ID[3]) + 9*int(ID[4])
ans += 8*int(ID[5]) + 7*int(ID[6]) + 6*int(ID[7]) + 5*int(ID[8]) + 4*int(ID[9])
ans += 3*int(ID[10]) + 2*int(ID[11])
ans = (11 - (ans%11))%10
print(ID[0], ID[1:5], ID[5:10], ID[10:12], ans)

# ---------------------------------------------------------------------------#
# 02-StrLst_★_Arabic_Numerals
List = ["zero","one","two","three","four","five","six","seven","eight","nine"]
n = int(input())
print(n, "-->", List[n])

# ---------------------------------------------------------------------------#
# 02-StrLst_★_USDate
month = ["xxx","January","February","March","April","May","June","July","August","September","October","November","December"]
d,m,y = input().split("/");
d = int(d); m = int(m); y = int(y); 
print(month[m]+ " " + str(d)+ ", " + str(y))

# ---------------------------------------------------------------------------#
# 02-StrLst_★_NDigits
str1 = str(input())
n = int(input())
strlen = len(str1)
mx = max(n, strlen)
print("0"*(mx-strlen) + str1)

# ---------------------------------------------------------------------------#
# 02-StrLst_★_WeeklySales
a,b,c,d,e,f,g = input().split()
a = int(a); b = int(b); c = int(c); d = int(d);
e = int(e); f = int(f); g = int(g);
print(a+b+c+d+e+f+g)

# ---------------------------------------------------------------------------#
# 02-StrLst_★★_AddVector
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
