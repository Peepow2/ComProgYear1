def remove_len1(d):
    D = dict()
    for k in d:
        if len(d[k]) > 1:
            D[k] = d[k]
    return D

def to_type2(type1):
    D = dict()
    for k in type1:
        k1, k2 = k.split(':')
        D[k1] = D.get(k1, list()) + [k2]
        D[k2] = D.get(k2, list()) + [k1]
    return D

exec(input().strip()) # DON'T remove this line

