def create_summary_file(filename,fileout):
    '''
    สร้างไฟล์ที่มีบรรทัดแรกเป็น province_of_isolation,28/2/2022,1/3/2022,2/3/2022,3/3/2022,... เรียงวันที่ไปจนครบตามที่มีในไฟล์ 
    แต่ละบรรทัดหลังจากนั้นเก็บจำนวนผู้ติดเชื้อของแต่ละจังหวัด ตาม province_of_isolation เรียงจังหวัดตามพจนานุกรม
    โดยในแต่ละจังหวัดเป็นจำนวนผู้ติดเชื้อที่รายงานในแต่ละวันตามข้อมูลใน announce_date (เรียงวันตามที่อ่านมาจากไฟล์)
    '''
    # เก็บข้อมูลในรูป DATA[จังหวัด][วันที่] = จำนวน
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

    fout = open(fileout, 'w', encoding = 'utf-8')
    fout.write("province_of_isolation," + ",".join(date) + '\n')
    for p in province:
      fout.write(p)
      for d in date:
        fout.write(',' + str(DATA[d][p]))
      fout.write('\n')
