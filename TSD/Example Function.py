# for elem in S: อาจจะไม่หยิบเรียงตามที่่เขียน
# if e in set เร็วกว่า if e in list

# ฟังก์ชันตรวจสอบว่ามีข้อมูลซ้ำกันหรือไม่
def has_duplicate1(x):
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                return True
    return False

def has_duplicate2(x):
    new_x = sorted(x)
    for i in range(1, len(new_x)):
        if new_x[i - 1] == new_x[i]:
            return True
    return False

def has_duplicate3(x):
    return len(set(x)) != len(x)

def has_duplicate4(x):
    s = set()
    for e in x:
        if e in x:
            return True
        s.add(e)
    return False

# ฟังก์ชันหาสองจำนวนที่รวมกันได้ k
def K_sun(k, x):
    S = set(x)
    ans = list()
    for e in S:
        e1 = e - k
        if e < e1 and e1 in S:
            ans.append((e, e1))
    return ans

# จำนวนเฉพาะที่มีค่าไม่เกิน N
def All_prime(N):
    S1 = set(range(2, N + 1))
    for i in range(2, int(N**0.5) + 1):
        S2 = set(range(2 * i, N + 1, i))
        S1 = S1 - S2
    return S1

# ฟังก์ชัน เก็บตัวการ์ตูน
def cartoon(x):
    cartoon1 = {}
    for sub in x:
        name, atype = sub
        if atype not in cartoon1:
            cartoon1[atype] = {name} # ห้ามใช้ set(name) เด็ดขาด
        else:
            cartoon1[atype].add(name)
    return cartoon1
