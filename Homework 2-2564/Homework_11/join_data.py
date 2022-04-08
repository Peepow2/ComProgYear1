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
