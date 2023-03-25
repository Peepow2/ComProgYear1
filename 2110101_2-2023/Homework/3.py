def get_sid_section(stu_rec):
    S = stu_rec.split(',')
    return [str(S[0]), str(int(S[1]))]

def get_sid_sections(stu_recs):
    return sorted([get_sid_section(c) for c in stu_recs])

def get_section(sid_sections, sid):
    for s in sid_sections:
        if sid == s[0]:
            return str(s[1])
    return '0'

def get_stu_points(grader_points):
    student = list()
    ADD_Index = list()
    for s in grader_points:
        NTS = s.split(',')
        if NTS[0] not in ADD_Index:
            ADD_Index += [NTS[0]]
            student += [[NTS[0], [0]]]
            
    for s in grader_points:
        NTS = s.split(',')
        idx = ADD_Index.index(NTS[0])
        student[idx][1].append(int(NTS[2]))
                
    for i in range(len(student)):
        student[i] = [student[i][0], max(student[i][1])]
    return sorted(student)

def get_stu_section_points(stu_points, sid_sections):
    return sorted([[get_section(sid_sections, S[0])] + S[::-1] for S in stu_points])

def get_section_point_count(stu_section_points, min_point):
    L = list()
    ADD_Index = list()
    for S in stu_section_points:
        if S[0] not in ADD_Index:
            ADD_Index.append(S[0])
            L.append([S[0], 0])
            
        if S[1] >= min_point:
            idx = ADD_Index.index(S[0])
            L[idx][1] += 1
    return sorted(L)
