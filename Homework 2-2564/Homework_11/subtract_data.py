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
