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
def get_nutrient(nutrient, food_name):
    L = match_foods(nutrient, food_name)
    if L == []: return []

    Nu = list()
    for i in nutrient:
        for j in L:
            if j == i[0]: Nu += [i];
            
    div = [0] * (len(nutrient[0]) - 2)
    OUT = ['NA'] * (len(nutrient[0]) - 2)
    for temp in Nu:
        temp = temp[2::]
        for i in range(len(temp)):
            if temp[i] != 'NA':
                if OUT[i] == 'NA': OUT[i] = 0
                OUT[i] += temp[i]
                div[i] += 1

    for i in range(len(OUT)):
        if OUT[i] != 'NA': OUT[i] /= div[i]
    return OUT
# ---------------------------------------------------------------- #
def summarize_daily_intake(nutrient, intakes):
    L = list(); Match = list(); day_false = [] 
    for t in intakes:
        idx = search_id(t[0], Match)
        if idx == -1: Match += [[t[0]]]
        M = match_foods(nutrient, t[1])
        if M == []: day_false += [t[0]]
        else:
            Match[idx] += [id2food(nutrient, M)[1]]

    for t in Match:
        idx = search_id(t[0], L)
        if idx == -1: L += [[t[0]] + ['NA'] * 6 + [True]]
        for w in t[1::]: 
            g_nu = get_nutrient(nutrient, w)
            for x in range(len(g_nu)):
                if g_nu[x] != 'NA':
                    if L[idx][x+1] == 'NA': L[idx][x+1] = 0
                    L[idx][x+1] += g_nu[x]

    for d in day_false:
        idx = search_id(d, L)
        L[idx][-1] = False
    return sorted(L)[::-1]
# ---------------------------------------------------------------- #
def search_id(s, L):
    for i in range(len(L)):
        if L[i][0] == s:
            return i
    return -1
# ---------------------------------------------------------------- #
