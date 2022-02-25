# --------------------------------------------------- #
def create_interval(x, y):
    if x > y: return "(0,0)"
    return"[" + str(x) + "," + str(y) + "]"
# --------------------------------------------------- #
def intersection(a, b):
    if "(0,0)" in a + b: return "(0,0)"
    A = a[1:-1].split(',')
    B = b[1:-1].split(',')
    left  = max(int(A[0]), int(B[0]))
    right = min(int(A[1]), int(B[1]))
    return create_interval(left, right)
# --------------------------------------------------- #
def is_subset(a, b):
    if a == '(0,0)': return True
    if b == '(0,0)': return False
    A = a[1:-1].split(',')
    B = b[1:-1].split(',')
    return (int(A[0]) >= int(B[0])) and (int(A[1]) <= int(B[1]))
# --------------------------------------------------- #
def get_subsets1(list_a, list_b):
    OUT = list()
    for a in list_a:
        for b in list_b:
            if is_subset(a, b):
                OUT.append(a); break
    return sorted(OUT)
# --------------------------------------------------- #
def get_subsets2(list_a, list_b):
    prev = False
    idxA = 0; endA = len(list_a)
    idxB = 0; endB = len(list_b)
    OUT = list()
    while idxA < endA:
        if idxB >= endB: break
        
        if is_subset(list_a[idxA], list_b[idxB]):
            OUT.append(list_a[idxA])
            prev = True
            
        if prev == True and not is_subset(list_a[idxA], list_b[idxB]):
            idxB += 1; idxA -= 1
            prev = False
        idxA += 1
                  
    return OUT
# --------------------------------------------------- #
