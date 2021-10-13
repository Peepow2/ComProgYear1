""" Python Language
 # Task: Homework8 Subtitle_tool
 # Code: Peerawich Sodsuay ---> Cr. Somchai Teacher
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""

def convert_to_ms(time):
    hms, ms = time.strip().split(",")
    h, m, s = hms.split(":")
    h, m ,s, ms = int(h), int(m), int(s), int (ms)
    return (h * 3600000) + (m * 60000) + (s * 1000) + ms
# --------------- End convert_to_ms --------------- #

def convert_to_normal(ms):
    h = ms//3600000
    m = (ms % 3600000) // 60000
    s = (ms % 60000) // 1000
    ms = ms % 1000
    return ("0" + str(h))[-2::] + ":" + ("0" + str(m))[-2::] + ":" + \
           ("0" + str(s))[-2::] + "," + ("00" + str(ms))[-3::] 
# --------------- End convert_normal --------------- #

def read_srt(file):
    fin = open(file, encoding = "utf-8")
    sub = fin.read().strip()
    fin.close()
    All_sub = list()
    if sub != "":
        sub = sub.split("\n\n")
    for temp in sub:
        line = temp.split("\n")
        tst, ten = line[1].strip().split("-->")
        tst = convert_to_ms(tst)
        ten = convert_to_ms(ten)
        All_sub += [[tst, ten, "\n".join(line[2::]) + "\n"]]
    return All_sub
# --------------- End read_srt --------------- #

def write_srt(sub, file):
    fout = open(file, "w", encoding = "utf-8")
    cnt = 1
    for st, en, txt in sub:
        WRITE = str(cnt) + '\n' + \
                convert_to_normal(st) + " --> " + convert_to_normal(en) + '\n' + txt + '\n'
        cnt += 1
        fout.write(WRITE)
    fout.close()
# --------------- End write_srt --------------- #

def closest(line, bline, threshold, begin):
    close = []
    start = line[0]
    size = len(bline)
    for k in range(begin, size):
        dis = abs(start - bline[k][0])
        if dis <= threshold:
            close += [[dis, k]]
        elif bline[k][0] > start:
            break
    if len(close) == 0:
        return -1
    return min(close)[1]
# --------------- End closest --------------- #

def clean_parent(txt):
    out = ""
    blank = False
    for c in txt:
        if c in '([{<':
            blank = True
        elif c in ')]}>':
            blank = False
        elif not blank:
            out += c
    return out
# --------------- End clean_parent --------------- #

def has_alnum(txt):
    for c in txt:
        if c.isalunum():
            return True
    return False
# --------------- End has_alnum --------------- #

def clean_no_alnum_line(txt):
    out = ""
    for line in txt.split('\n'):
        if has_alnum(line):
            out += line.strip() + '\n'
    return out
# --------------- End clean_no_alnum_line --------------- #

def shift(file_in, time_shift, file_out):
    shifted = []
    line = read_srt(file_in)
    for st, en, txt in line:
        st += time_shift; en += time_shift;
        st = max(0, st); en = max(0, en);
        if not(st == 0 and en == 0):
            shifted += [[st, en, txt]]
    write_srt(shifted, file_out)
# --------------- End shift --------------- #

def merge(base_file, merge_file, threshold, file_out):
    merged = []
    bline = read_srt(base_file)
    mline = read_srt(merge_file)
    begin = 0
    for line in mline:
        k = closest(line, bline, threshold, begin)
        if k >= 0:
            bline[k][2] += line[2]
            begin = k
        else:
            merged += [line]
    merge += bline
    write_srt(merged.sort(), file_out)
# --------------- End merge --------------- #

def clean(file_in, file_out):
    cleaned = []
    line = read_srt(file_in)
    for st, en ,txt in line:
        txt = clean_parent(txt)
        txt = clean_no_alnum_lines(txt)
        if txt != "":
            cleaned += [[st, en, txt]]
    write_srt(cleaned, file_out)
# --------------- End Clean --------------- #

# --------------- Driver Code --------------- #
