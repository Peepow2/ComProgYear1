def get_product_from_file(textfile):
    product = {}
    fin = open(textfile, 'r')
    Data = fin.readlines()
    fin.close()
    
    for line in Data:
        line = line.split('=')
        product[line[0].strip()] = line[1].strip()
    s = product['created_date']
    product['created_date'] = s[0:2] + '/' + s[2:4] + '/' + s[4:8]
    return product
#======================================
def cal_defect_ratio(textfile):
    S = get_product_from_file(textfile)['scan_data'].split(',')
    return round(S.count('+')/len(S), 2)
#======================================
def cal_defect_box_ratio(textfile):
    defect_box_ratio = 0.0
    scan_data = get_product_from_file(textfile)['scan_data'].split(',')
    WDH = int(len(scan_data) ** (1/3) + 0.2)

    if '+' in scan_data:
        Defect_X, Defect_Y, Defect_Z = list(), list(), list()
        for i in range(len(scan_data)):
            if scan_data[i] == '+':
                Defect_X.append(i % WDH + 1)
                Defect_Y.append(i // (WDH**2) + 1)
                Defect_Z.append(i // WDH % WDH + 1)
        
        dx = max(Defect_X) - min(Defect_X) + 1
        dy = max(Defect_Y) - min(Defect_Y) + 1
        dz = max(Defect_Z) - min(Defect_Z) + 1
        defect_box_ratio = (dx * dy * dz) / len(scan_data)

    return round(defect_box_ratio, 2)
#======================================
def create_prod_summary_file(pids):
    if len(pids) == 0: return
    
    f = open("product_summary.csv",'w')
    f.write("pid,created_date,factory_id,defect_ratio,defect_box_ratio\n")
    for file_Name in sorted(pids):
        file_Name += '.txt'
        Data = get_product_from_file(file_Name)
        
        # Write product_summary
        f.write(Data['pid'] + ',')
        f.write(Data['created_date'] + ',')
        f.write(Data['factory_id'] + ',')
        f.write(str(cal_defect_ratio(file_Name)) + ',')
        f.write(str(cal_defect_box_ratio(file_Name)) + '\n')
    f.close()
#======================================
def create_size_summary_file(pids):
    if len(pids) == 0: return
    
    # Count SML Size
    SIZE = {'S': 0, 'M': 0, 'L': 0}
    for txt_file in pids: 
        DBR = cal_defect_box_ratio(txt_file + '.txt') # Defect_Box_Ratio
        SIZE['S'] += int(DBR < 0.33)
        SIZE['M'] += int(0.33 <= DBR < 0.67)
        SIZE['L'] += int(DBR >= 0.67)
        
    # Write size_summary
    f = open("size_summary.csv", 'w')
    f.write("size,#\n")    
    f.write("S," + str(SIZE['S']) + '\n')
    f.write("M," + str(SIZE['M']) + '\n')
    f.write("L," + str(SIZE['L']) + '\n')
    f.close()
