def find_parent(st, str1):
    en = len(str1)
    for i in range(st, en):
        if str1[i] in "([{<":
            return i, str1[i]
    return -1, ' '

def find_pairs(st, op, str1):
    if op == '(':
        for i in range(st, len(str1)):
            if str1[i] == ')':
                return i
    if op == '[':
        for i in range(st, len(str1)):
            if str1[i] == ']':
                return i
    if op == '{':
        for i in range(st, len(str1)):
            if str1[i] == '}':
                return i
    if op == '<':
        for i in range(st, len(str1)):
            if str1[i] == '>':
                return i
    return -1

def IsNum(ss):
    if ss == "":
        return False
    for c in ss:
        if c not in "0123456789":
            return False
    return True

def clean(INPUT, OUTPUT):
    fp = open(INPUT, 'r'); fout = open(OUTPUT, 'w');
    All_sub = []; idx = 0; cnt = 1;
    templine = fp.readlines()
    All_sub = str("")
    for temp in templine:
        All_sub += str(temp)
    All_sub = All_sub.split("\n\n")
    for temp in All_sub:
        Last, op = find_parent(0, temp)
        op_pairs = find_pairs(Last + 1, op, temp)
        index = [-1];
        while Last != -1 and op_pairs != -1:
            index += [Last, op_pairs];
            Last, op = find_parent(op_pairs + 1, temp)
            op_pairs = find_pairs(Last + 1, op, temp)
        index += [len(temp), -1]
        out = str("")
        for i in range(0, len(index) - 1, 2):
            out += temp[index[i] + 1:index[i+1]]
        out = out.split("\n")
        size = len(out); i = 0;
        while i < size:
            if out[i].strip() == '':
                out.pop(i);
                size -= 1;
            i += 1
        out += ["xxxx"]
        size = len(out) - 1; i = 0;
        while i < size:
            if "-->" in out[i] and (out[i+1] != 'xxxx'):
                if cnt != 1:
                    fout.write("\n")
                fout.write(str(cnt) + '\n' + out[i] + '\n')
                cnt += 1;    
            if (not IsNum(out[i].strip())) and ("-->" not in out[i]) and (out[i] != 'xxxx'):
                fout.write(out[i] + '\n')
            i += 1
    fp.close(); fout.close();        

# -------------------- Driver Code -------------------- #
# clean('test1.txt', 'test1_cleaned.txt')
