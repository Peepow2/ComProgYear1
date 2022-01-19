def count_chars(s, chars):
    rec = []
    for c in chars:
        rec += [s.count(c)]   
    return rec

exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป
