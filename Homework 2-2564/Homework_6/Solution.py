# ---------------------------------------------------------------- #
def compute_similarity(food_name1, food_name2):
    F1 = food_name1.split()
    F2 = food_name2.split()
    cnt = 0; s = len(F1) + len(F2)
    for i in F1: 
        for j in F2: 
            if i == j: cnt += 1
    return (cnt * 2) / s
# ---------------------------------------------------------------- #
def match_foods(nutrient, food_name):
    OUT = list()
    for temp in nutrient:
        t = compute_similarity(temp[1], food_name)
        if t > 0.5: OUT += [[t, temp[0]]]

    if OUT == []: return []
    mx = max(OUT)[0]
    out = list()
    for temp in OUT:
        if temp[0] == mx: out += [temp[1]]
    return sorted(out)
# ---------------------------------------------------------------- #
