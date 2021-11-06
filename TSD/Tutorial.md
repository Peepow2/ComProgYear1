"""
List = [11, 22, 33,]
Tuple = (11, 22, 33,)
print(List, Tuple)

# ตัวอย่าง operation
t = (11, 22, 33)
print(len(t))
print(t[0], t[-1])
print(t[:2])
print(33 in t)
print(t.index(33))

# แก้ไขไม่ได้ แต่สร้างใหม่ได้
"""
"""
# set เป็นที่เก็บข้อมูลที่ไม่ซ้ำกัน และไม่มีลำดับ (เหมือนคณิตศาสตร์)
# ข้อมูลในเซตต้องเปลี่ยนค่าไม่ได้
s = set() # {} คือ dict ว่าง
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print("A union B")
print(A.union(B))
print(A | B)

print()
print("A intersection B")
print(A.intersection(B))
print(A & B)
print()

print("A - B")
print(A.difference(B))
print(A - B)
print()

# s.add(value) --> add value
# s.remove(value) --> remove value
# A ^ B --> (A - B) U (B - A)
# A <= B, A.issubset(B) --> subset

print("Show all value in set")
for e in A: print(e, end = ' ')
print("\n")

print("Create set")
# s = set(d) --> s = set(); for e in d: s.add(e)
s = set([1, 2, 3, 1]);     print(s)
s = set((1, 2, 3, 1));     print(s)
s = set("Mono");           print(s)
print()

print("Create list")
# L = list(d) --> L = list(); for e in d: L.append(e)
L = list([1, 2, 3, 1]);    print(L)
L = list((1 ,2, 3, 1));    print(L)
L = list("Mono");          print(L)
L = list({"A":2, "B":2});  print(L)
L = list({1, 2, 3});       print(L)
print()

print("Create tuple")
# T = tuple(d) 
T = tuple([1, 2, 3, 1]);   print(T)
T = tuple((1 ,2, 3, 1));   print(T)
T = tuple("Mono");         print(T)
T = tuple({"A":2, "B":2}); print(T)
T = tuple({1, 2, 3});      print(T)
T = tuple(range(1, 7, 2)); print(T)
print()

# x.sort vs sorted(x)
# x.sort ใช้ได้เมื่อ x เป็น list เท่านั้น
# sorted(x) ใช้ได้หมด
"""
