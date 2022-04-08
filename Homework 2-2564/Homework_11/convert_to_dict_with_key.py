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
