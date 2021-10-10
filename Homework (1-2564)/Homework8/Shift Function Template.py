def convert_to_ms(time):
    ts = 0
    if time[-1] == '\n':
        time = time[0:-1]
    t = time.split(":")
    t += t[2].split(",")
    t.pop(2)
    ts = (int(t[0]) * 3600000) + (int(t[1]) * 60000) + (int(t[2]) * 1000) + int(t[3])
    return ts

def convert_to_normal(time):
    # form 0:00:00,000
    out = str(""); time = int(time)
    if time < 0: time = 0
    
    t = str(time//3600000)
    out += t + ":";
    time -= (time//3600000) * 3600000;

    t = str(time//60000)
    out += ((2 - len(t)) * "0") + t + ":";
    time -= (time//60000) * 60000;

    t = str(time//1000)
    out += ((2 - len(t)) * "0") + t + ",";
    time -= (time//1000) * 1000
    
    t = str(time);
    out += ((3 - len(t)) * "0") + t;
    return out

def IsNum(ss):
    for c in ss:
        if c not in "0123456789":
            return False
    return True

def shift(INPUT, time_shift, OUTPUT):
    fp = open(INPUT, 'r')
    fout = open(OUTPUT, 'w')
    WRITE = str(""); cnt = 1; skip = False
    for line in fp:
        line = line.strip()
        if IsNum(line):
            skip = False;
            if WRITE != "":
                fout.write((str(cnt) + "\n" + WRITE + '\n'))
                WRITE = str(""); cnt += 1;
            
        elif "-->" in line:
            t1, t2 = line.split(" --> ")
            t1 = convert_to_ms(t1);
            t2 = convert_to_ms(t2);
            t1 += time_shift; t2 += time_shift;
            if t1 <= 0 and t2 <= 0:
                WRITE = (""); skip = True;
                continue
            else:
                t1 = convert_to_normal(t1)
                t2 = convert_to_normal(t2)
                WRITE += (str(t1) + " --> " + str(t2) + "\n")
        elif not skip:
            WRITE += (line + "\n")
    if not skip:
        fout.write((str(cnt) + "\n" + WRITE + '\n'))
    fout.close()
    fp.close()

# ---------------------- Driver Code ---------------------- #
# 00:00:00,000
shift('test1.txt', -1500, 'test2_shifted.txt')
fp = open("test1_en.srt" , 'r')
for line in fp:
    print(line)
fp.close()
