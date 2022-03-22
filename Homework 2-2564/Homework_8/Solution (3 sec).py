# HW8_StrFile (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้

def read_csv(filename):
    fin = open(filename, 'r', encoding = 'utf-8')
    data = fin.readlines()
    fin.close()
    return data

def write_csv(NAME, data):
    fout = open(NAME, 'w', encoding = 'utf-8')
    fout.write("\n".join(data))
    fout.close()
    return

def search_idx(L, s):
    idx = -1
    if s in L: idx = L.index(s)
    return idx
# ------------------------------------------------------------------------------- #
def get_unique_value(filename,column_name):
    '''
    คืนค่าเป็นลิสต์ที่มีสมาชิกไม่ซ้ำของค่าในคอลัมน์ column_name เรียงลำดับตามบรรทัดที่ปรากฏในไฟล์
    หากไม่มีชื่อคอลัมน์ปรากฏอยู่ ให้คืนค่าเป็นลิสต์ว่าง
    '''
    data = read_csv(filename)
    idx = search_idx(data[0].strip().split(','), column_name)
    HAVE = dict(); OUT = list()
    if idx == -1: return []

    for line in data[1::]:
        line = line.strip().split(',')
        if line[idx] not in HAVE:
          HAVE[line[idx]] = True
          OUT.append(line[idx])
    return OUT

def count_announce_date_province(filename,date,province):
    '''
    คืนค่าเป็นจำนวนบรรทัดที่มีค่า province_of_isolation เท่ากับ province และ announce_date เท่ากับ date 
    หากไม่มีข้อมูลของจังหวัดและวันตามอินพุต ให้คืนค่า 0
    '''
    cnt = 0
    for line in open(filename, 'r'):
        line = line.strip().split(',')
        if line[1] == date and line[7] == province: cnt += 1
    return cnt 

def count_value_in_column(filename,column_name,value):
    '''
    คืนค่าเป็นจำนวนบรรทัดที่มีค่าเท่ากับ value ในคอลัมน์ column_name 
    คืนค่าเป็น -1 ในกรณีที่ไม่มีคอลัมน์ตาม column_name
    ''' 
    cnt = 0
    data = read_csv(filename)
    idx = search_idx(data[0].strip().split(','), column_name)
    if idx == -1: return -1
    
    for line in data[1:]:
       line = line.strip().split(',')
       if line[idx] == value: cnt += 1       
    return cnt

def create_file_by_value_in_column(filename,fileout,column_name,value):
    '''
    สร้างไฟล์ที่มีชื่อเป็น fileout โดยเลือกเฉพาะบรรทัดที่มีค่าในคอลัมน์ column_name เท่ากับ value  
    ในกรณีที่ไม่มีชื่อคอลัมน์ตาม column_name ให้ออกจากฟังก์ชันโดยไม่ต้องทำอะไร 
    ในไฟล์ที่สร้างขึ้นใหม่ จะต้องมีบรรทัดที่เป็นชื่อคอลัมน์เหมือนต้นฉบับ ตามด้วยข้อมูลตามกำหนด
    ''' 
    data= read_csv(filename)
    idx = search_idx(data[0].strip().split(','), column_name)
    if idx == -1: return 

    fout = open(fileout, 'w', encoding = 'utf-8')
    WRITE = list()
    WRITE += [",".join(data[0].strip().split(','))]
    for line in data[1:]:
        line = line.strip().split(',')
        if line[idx] == value: 
            WRITE += [",".join(line)]
    write_csv(fileout, WRITE)
    return

def count_by_date(filename,province):
    '''
    คืนลิสต์ของจำนวนผู้ติดเชื้อรายวันที่รายงานของทุก announce_date เรียงตามวันที่ปรากฏในไฟล์
    ตามบรรทัดที่ province_of_isolation มีค่าเท่ากับ province
    หากวันใดไม่มีข้อมูลของจังหวัดนั้น ๆ รายงาน ให้ใส่ค่าเป็น 0 
    '''
    OUT = list()
    data = read_csv(filename)
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
    '''
    สร้างไฟล์ที่มีบรรทัดแรกเป็น province_of_isolation,28/2/2022,1/3/2022,2/3/2022,3/3/2022,... เรียงวันที่ไปจนครบตามที่มีในไฟล์ 
    แต่ละบรรทัดหลังจากนั้นเก็บจำนวนผู้ติดเชื้อของแต่ละจังหวัด ตาม province_of_isolation เรียงจังหวัดตามพจนานุกรม
    โดยในแต่ละจังหวัดเป็นจำนวนผู้ติดเชื้อที่รายงานในแต่ละวันตามข้อมูลใน announce_date (เรียงวันตามที่อ่านมาจากไฟล์)
    '''
    date = get_unique_value(filename, 'announce_date')
    province = sorted(get_unique_value(filename, 'province_of_isolation'))
    data = read_csv(filename)

    DATA = dict()
    for line in data[1::]:
        line = line.strip().split(",")
        if line[1] not in DATA:
            DATA[line[1]] = dict()
            for p in province:
              DATA[line[1]][p] = 0
        DATA[line[1]][line[7]] += 1  

    WRITE = list()
    WRITE += ["province_of_isolation," + ",".join(date)]
    for p in province:
      WRITE += [str(p)]
      for d in date:
          WRITE[-1] += ',' + str(DATA[d][p])
    write_csv(fileout, WRITE) 
