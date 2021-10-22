def SUBSET(dict1, dict2):
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True

# ---------------- Driver Code ---------------- #
A = {'1' : 'PP', '2': 'is', '3': 'very', '4': 'handsome', '5': '.'}
B = {'1' : 'PP', '2': 'is'}
print(SUBSET(B, A)) # B เป็นสับเซตของ A ไหม
