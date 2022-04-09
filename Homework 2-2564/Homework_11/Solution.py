def convert_to_dict(data,column_name):
    out = list()
    for i in range(len(data)):
        D = dict()
        for j in range(len(data[i])):
            if data[i][j] != None : D[column_name[j]] = data[i][j]
        if D != {}: out.append(D)
    return out

def convert_to_dict_with_key(data,column_name,key):
    OUT = dict()
    for i in range(len(data)):
        D = dict()
        for j in range(len(data[i])):
            if key == column_name[j]: K = data[i][j]
            else:
                if data[i][j] != None: D[column_name[j]] = data[i][j]             
        if (K != None) and (K not in OUT) and (D != {}): OUT[K] = D
    return OUT

def join_data(data1,data2):
    OUT = dict()
    for k1 in data1:
        if k1 in data2:
            OUT[k1] = data1[k1]
            for k2 in data2[k1]:
                if k2 not in OUT[k1]:
                    OUT[k1][k2] = data2[k1][k2]
                else:
                    OUT[k1][k2 + '_1'] = data2[k1][k2]                    
    return OUT

def merge_data(data1,data2):
    OUT = dict()
    for k1 in data1:
        if k1 in data2:
            OUT[k1] = data1[k1]
            for k2 in data2[k1]:
                if k2 not in OUT[k1]:
                    OUT[k1][k2] = data2[k1][k2]
                else:
                    OUT[k1][k2 + '_1'] = data2[k1][k2]
        else: OUT[k1] = data1[k1]
            
    for k2 in data2:
        if k2 not in OUT:
            OUT[k2] = data2[k2]
    return OUT

def subtract_data(data1,data2):
    OUT = dict()
    for k in data1:
        if k in data2:
            T = dict()
            for d_k in set(data1[k].keys()) - set(data2[k].keys()):
                T[d_k] = data1[k][d_k]
            if T != {}: OUT[k] = T
        else: OUT[k] = data1[k]
    return OUT
