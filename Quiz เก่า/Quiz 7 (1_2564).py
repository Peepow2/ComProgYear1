def is_undergrad(sid):
    return (sid[2] in '034')

def get_faculty(sid):
    if sid[-2::] == '21':   return "ENG"
    if sid[-2::] == '22':   return "ART"
    if sid[-2::] == '23':   return "SCI"
    return "OTHER"

def get_status(sid):
    st = []
    if sid[2] in '034': st += ['U']
    if sid[2] in '178': st += ['G']
    st += [get_faculty(sid)]    
    return st

# ------------------------ Driver Code ------------------------ #
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader

