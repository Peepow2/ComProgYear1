def convert_to_dict(data,column_name):
    out = list()
    for i in range(len(data)):
        D = dict()
        for j in range(len(data[i])):
            if data[i][j] != None : D[column_name[j]] = data[i][j]
        if D != {}: out.append(D)
    return out
