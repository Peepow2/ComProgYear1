str1 = str(input())
for c in str1:
    if 48 <= ord(c) <= 57:
        print("#", end = "")
    elif 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
        print("*", end = "")
    else:
        print(c, end = "")
