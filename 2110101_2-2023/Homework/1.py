def center(r):
    return [r[0] + (r[2]/2), r[1] - (r[3]/2)]

def distance(r1, r2):
    c1, c2 = center(r1), center(r2)
    return ((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2) ** 0.5

def intersection(r1, r2):
    return max(0, min(r1[0] + r1[2], r2[0] + r2[2]) - max(r1[0], r2[0])) * max(0, min(r1[1], r2[1]) - max(r1[1] - r1[3], r2[1] - r2[3]))

def union(r1, r2):
    return (r1[2] * r1[3]) + (r2[2] * r2[3]) - intersection(r1, r2)

def iou(r1, r2):
    return intersection(r1, r2) / union(r1, r2)
