store = list()  
inp = input().strip()
while inp != 'q':
    inp = inp.split()
    store += [inp[0], float(inp[1])]
    inp = input().strip()

buys = input().strip().split()
price = 0
for b in buys:
    idx = store.index(b)
    price += store[idx + 1]
print("total payment", price)
