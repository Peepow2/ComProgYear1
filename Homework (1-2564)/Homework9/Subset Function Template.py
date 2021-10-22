def SUBSET(dict1, dict2):
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True

# ---------------- Driver Code ---------------- #
print(SUBSET(B, A)) # B เป็นสับเซตของ A ไหม
