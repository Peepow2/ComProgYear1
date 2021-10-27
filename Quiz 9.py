def update(points, uses, reward):
    for c in uses:
        points[c] -= uses[c]
    for c in points:
        points[c] = int(points[c] * (100 + reward)/100)
    return points

exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader

