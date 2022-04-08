def empty(D):      return D == {}
def No_None(A, B): return A != None and B != None

def convert_to_dict_with_key(data,column_name,key):
    OUT = dict()
    for i in range(len(data)):
        D = dict()
        for j in range(len(data[i])):
            KEY, VAL = column_name[j], data[i][j]
            if key == KEY: K = data[i][j]
            else:
                if No_None(KEY, VAL): D[KEY] = VAL         
        if K != None and OUT.get(K) == None and not empty(D): OUT[K] = D
    return OUT
