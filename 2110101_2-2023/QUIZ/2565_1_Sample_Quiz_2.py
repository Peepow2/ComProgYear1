def check_string(T, S):
    T , S = T.upper(), S.upper()
    for i in range(len(S)):
        if T[i] != S[i] and T[i] != '?':
            return False
    return True

# Driver Code (main)
FILENAME = input().strip()
O_NAME = input().strip() 
N_NAME = input().strip()
str1 = ''
f = open(FILENAME, 'r')
for line in f.readlines():
    i = 0
    while i < len(line) - len(O_NAME):
        if check_string(O_NAME, line[i:i+len(O_NAME)]) and line[i+len(O_NAME)] == '/':
            str1 += N_NAME
            i += len(O_NAME)
        else:
            str1 += line[i]
            i += 1
    str1 += line[i:]
print(str1)
