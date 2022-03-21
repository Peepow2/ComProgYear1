# HW8_StrFile (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

def read_csv(filename, column_name):
    fin = open(filename, 'r')
    data = fin.readlines()
    first_line = data[0].strip().split(','); idx = -1
    if column_name in first_line:  idx = first_line.index(column_name)
    fin.close()
    return data, idx
# ------------------------------------------------------------------------------- #
def get_unique_value(filename,column_name):
    data, idx = read_csv(filename, column_name)
    if idx == -1: return []

    OUT = list()
    for line in data[1:]:
      line = line.strip().split(',')
      if line[idx] not in OUT:
        OUT.append(line[idx])
    return OUT

def count_announce_date_province(filename,date,province):
    cnt = 0
    for line in open(filename, 'r'):
        line = line.strip().split(',')
        if line[1] == date and line[7] == province: cnt += 1
    return cnt  

def count_value_in_column(filename,column_name,value):
    cnt = 0
    data, idx = read_csv(filename, column_name)
    if idx == -1: return -1
    
    for line in data[1:]:
       line = line.strip().split(',')
       if line[idx] == value: cnt += 1       
    return cnt

def create_file_by_value_in_column(filename,fileout,column_name,value):
    data, idx = read_csv(filename, column_name)
    if idx == -1: return 

    fout = open(fileout, 'w')
    fout.write(data[0])
    for line in data[1:]:
        line = line.strip().split(',')
        if line[idx] == value: 
            fout.write(",".join(line) + '\n')
    fout.close()
    return

def count_by_date(filename,province):
    OUT = list()
    data, idx = read_csv(filename, ' ')
    prev = "xx"

    for line in data[1:]:
        line = line.strip().split(',')
        if line[1] != prev: 
            OUT.append(0)
            prev = line[1]
        if line[7] == province: 
            OUT[-1] += 1
    return OUT

def create_summary_file(filename,fileout):
    date = get_unique_value(filename, 'announce_date')
    province = sorted(get_unique_value(filename, 'province_of_isolation')) 
    fout = open(fileout, 'w')
    fout.write("province_of_isolation," + ",".join(date) + '\n')
    for t in province:
        fout.write(t + ',' + ",".join([str(e) for e in count_by_date(filename, t)]) + '\n')
    fout.close()
    return
