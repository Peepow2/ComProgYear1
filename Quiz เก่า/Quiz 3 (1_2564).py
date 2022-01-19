str1 = str(input())
name = str1.split(",")[0]
sur = str1.split(":")[0]
sur = sur.split(",")[1]
let = len(name) + len(sur) + 2
date = str1[let:]
date = date.split("/")
print(sur, name + str(":"), date[1], date[0] + str(","), date[2])
