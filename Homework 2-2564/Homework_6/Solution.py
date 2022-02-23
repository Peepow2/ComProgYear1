# ---------------------------------------------------------------- #
def compute_similarity(food_name1, food_name2):
    F1 = food_name1.split()
    F2 = food_name2.split()

    count = 0; s = len(F1) + len(F2)
    for s1 in F1:
        for s2 in F2:
            if s1 == s2: count += 1
    return (count * 2) / s
# ---------------------------------------------------------------- #
def match_foods(nutrient, food_name):
    tod = list()
    for temp in nutrient:
        t = compute_similarity(temp[1], food_name)
        if t > 0.5: tod += [[t, temp[0]]]
    if tod == []: return []
    mx = max(tod)[0] # [0.857, id]
    OUT = list()
    for temp in tod:
        if temp[0] == mx: OUT += [temp[1]]
    return OUT
# ---------------------------------------------------------------- #
def get_nutrient(nutrient,food_name):
    L = match_foods(nutrient, food_name)
    if L == []: return []
    
    Nu = list()
    for i in nutrient:
        for j in L:
            if j == i[0]: Nu += [i]
    
    TIME = [0] * 6
    SUM = ['NA'] * 6
    
    for temp in Nu:
        temp = temp[2::]
        for i in range(len(temp)):
            if temp[i] != 'NA':
                if SUM[i] == 'NA': SUM[i] = 0
                SUM[i] += temp[i]
                TIME[i] += 1
    
    for i in range(len(SUM)):
        if SUM[i] != 'NA': SUM[i] /= TIME[i]
    return SUM
# ---------------------------------------------------------------- #
def summarize_daily_intake(nutrient, intakes):
    # [[date, food1, food2, ...]]
    Timeline = list(); day_false = list()
    for t in intakes:
        idx = find_date_index(t[0], Timeline)
        if idx == -1: Timeline.append([t[0]])
        if match_foods(nutrient, t[1]) == []: day_false.append(t[0])
        Timeline[idx].append(t[1])
    
    Energy = list()
    for t in Timeline:
        idx = find_date_index(t[0], Energy)
        if idx == -1: Energy.append([t[0]] + ['NA'] * 6 + [True])
        for food_name in t[1::]:
            g_nu = get_nutrient(nutrient,food_name)
            for x in range(len(g_nu)):
                if g_nu[x] != 'NA':
                    if Energy[idx][x+1] == 'NA': Energy[idx][x+1] = 0
                    Energy[idx][x+1] += g_nu[x]
    
    for d in day_false:
        idx = find_date_index(d, Energy)
        Energy[idx][-1] = False
    return sorted(Energy)[::-1]
# ---------------------------------------------------------------- #
def find_date_index(search, List):
    for i in range(len(List)):
        if List[i][0] == search:
            return i
    return -1
# ---------------------------------------------------------------- #
