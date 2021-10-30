def Bsort(arr):
    swapped = True
    size = len(arr)
    while swapped:
        swapped = False
        for i in range(1, size):
            if arr[i-1][3] > arr[i][3]:
                arr[i-1][3], arr[i][3] = arr[i][3], arr[i-1][3]
                swapped = True
    return arr
# ----------------------------------------
A = ["A", "B", 2000, 6, "hash1"]
B = ["A", "B", 1000, 8, "hash2"]
C = ["C", "A", 3000, 7, "hash3"]
txn_list = [A, B, C]
sorted_txn = Bsort(txn_list)
print(sorted_txn)

# https://pastebin.com/gNV4GGCd
# https://visualgo.net/en/sorting
# ในที่นี้จะใช้เงื่อนไขในการสลับคือ timestamp (ตัวที่ 4 index 3) ของแต่ละสิสต์ย่อย
