def empty(D):      return D == {}
def No_None(A, B): return A != None and B != None

def convert_to_dict(data,column_name):
    out = list()
    for i in range(len(data)):
        D = dict()
        for j in range(len(data[i])):
            k, v = column_name[j], data[i][j]
            if No_None(k, v): D[k] = v
        if not empty(D): out.append(D)
    return out
