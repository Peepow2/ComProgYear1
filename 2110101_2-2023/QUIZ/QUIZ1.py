# QUIZ1_1
def rotate_left(s, n):
    return s[n:] + s[:n]

def rotate_right(s, n):
    return s[-n:] + s[:-n]

def str_mod(s ,n):
    OUT = ""
    for c in s:
        OUT += str(int(c) % n)
    return OUT

def main():
    s = input()
    if s[-2] == '1':
        print(rotate_left(s, int(s[-1])))
    elif s[-2] == '2':
        print(rotate_right(s, int(s[-1])))
    elif s[-2] == '3':
        print(str_mod(s, int(s[-1])))
    else:
        print(s)

exec(input().strip())

# QUIZ1_2
x = ['x'] + [float(e) for e in input().split()]
print("AQI|1 2 3 4 5")
print("-------------")
for i in range(1, 8):
    if x[i] < 25:
        print(str(i) + "..|+........")
    elif 25 <= x[i] < 50:
        print(str(i) + "..|..+......")
    elif 50 <= x[i] < 100:
        print(str(i) + "..|....+....")
    elif 100 <= x[i] < 200:
        print(str(i) + "..|......+..")
    elif 200 <= x[i]:
        print(str(i) + "..|........+")
print("-------------")

# QUIZ1_3 Flowchart โจทย์ยาวจำไม่ได้
