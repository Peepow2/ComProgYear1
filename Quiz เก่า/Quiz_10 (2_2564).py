def m_sum(m, axis):
    if axis == 0:
        L = [0] * len(m[0])
        for i in range(len(m)):
            for j in range(len(m[i])):
                L[j] += m[i][j]
        return L
    else: return [sum(r) for r in m]
                
exec(input().strip()) #ต้องมีบรรทัดนี้เมื่อส่งไป grader
