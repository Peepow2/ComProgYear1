def m_sum(m, axis): 
  return [sum(e) for e in [zip(*m), m][axis]]           
exec(input().strip()) #ต้องมีบรรทัดนี้เมื่อส่งไป grader
