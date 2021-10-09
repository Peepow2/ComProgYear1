```
# -------------------- Clip 1 -------------------- # 
inp = (str("Espresso, Macchiato, Ristretto, Americano, Latte, Cappuccino, Mocha, Affogato"))
inp = inp.split(", ")
for i in range(len(inp)):
    print(inp[i] + " " * (12 - len(inp[i])), end = '')
    if i%3 == 2:    print()

import urllib.request as ulr
def find_idx(c, st, str1):
    en = len(str1)
    for i in range(st, en):
        if str1[i] == c:
            return i
    return -1
# -------------- Driver Code -------------- #
url = "http://air4thai.pcd.go.th/services/getNewAQI_XML.php?stationID=bkp63t"
web = ulr.urlopen(url)
for line in web:
    line = line.decode()
    if "<PM25 value=" in line:
        idx1 = find_idx('"', 0, line)        # line.find('"')
        idx2 = find_idx('"', idx1 + 1, line) # line.find('"', idx + 1)
        break;
print("PM2.5 value --> " + str(line[idx1 + 1:idx2]))
```
```
# -------------------- Clip 2 -------------------- #
# print("A\n\n\nBC\nD")
s = "  Hello World "
print(len(s))
print(s.lower(), s)
print(s.upper(), s)
print(s.strip())
print(s.find("o"))
print(s.find("o", 7))
```
```
# -------------------- Clip 3 -------------------- #
import math
d = 3.1415 / 6.0
x = math.radians(d)
s = math.sin(x)
y = abs(s)
r = round(y, 2)
print(round(abs(math.sin(math.radians(d))), 2), r) # เปรียบเทียบผลลัพธ์

line1 = "   Hello World  "
line2 = line1.strip()
line3 = line2.upper()
idx1 = line3.find("LO")
idx2 = line1.strip().upper().find("LO")
print(idx1, idx2) # เปรียบเทียบผลลัพธ์

# ห้ามเปลี่ยนค่าใน string
# s[2] = a, s[3:7] = "-^o^-"
# s.lower(), s.upper() ต้องมีตัวแปรมารับเพราะ s เก็บค่าเดิม
# s = s.lower() สามารถทำได้
```
```
# -------------------- Clip 4 -------------------- #
fp = open("data.txt", "r") # ตัวรับ = open("ชื่อไฟล์", "สิ่งที่ต้องการทำ")
line1 = fp.readline() # 1
line2 = fp.readline() # 2
line3 = fp.readline() # 3
line4 = fp.readline() # 4
print(line1); print(line2); print(line3); print(line4);
print(len(line1)) # เอ๊ะ ทำไมได้ len + 1 เนี่่ย
print(len(line4)) # จบแล้ว len = 0
print(line1[-1] == '\n') # ตัวท้ายเก็บ \n ไว้
fp.close() # เปิดแล้วต้องปิดเสมอ
print("---------------------------------------------")
# การอ่านข้อมูลในแฟ้มข้อความ
fp = open("data.txt", "r")
for line in fp:
    print(line)
fp.close()

# การบันทึกข้อมูลลงในแฟ้มข้อความ
fout = open("Writing.txt", "w")
fout.write("Your text")
fout.write("Your text") # ไม่ขึ้นบรรทัดใหม่ให้
fout.write("\nYour text1\nYour text2")
fout.close()
```
