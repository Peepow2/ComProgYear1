List_num = [float(e) for e in input().split()]
command = str(input().strip())

if command == 'mean':
    print(sum(List_num)/len(List_num))  
elif command == 'median':
    l = len(List_num)
    print((List_num[(l-1)//2] + List_num[l//2]) / 2)
else:
    print("Not a command")
