def m_sum(m, axis):
    if axis == 0: m = zip(*m)
    return [sum(e) for e in m]            
exec(input().strip()) #ต้องมีบรรทัดนี้เมื่อส่งไป grader
