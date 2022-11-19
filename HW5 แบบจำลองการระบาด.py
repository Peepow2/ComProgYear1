# HW5_Infection_Analysis

def get_coordinates(population, vaccinated):
    OUT = dict()
    for itr in population:
      if itr['vaccinated'] == vaccinated:
        OUT[itr['id']] = itr['coordinate']
    return OUT
# --------------------------------------------------------- # 
def get_all_unjabbed_pairs(population, radius):
    OUT = list()
    unjabbed = get_coordinates(population, False)
    for itr1 in unjabbed:
      x1 = unjabbed[itr1][0]
      y1 = unjabbed[itr1][1]
      for itr2 in unjabbed:
        x2 = unjabbed[itr2][0]
        y2 = unjabbed[itr2][1]

        if (((y1 - y2)**2) + (x1 - x2)**2) <= radius**2 and (itr1 < itr2): 
          OUT.append(tuple((itr1, itr2))
    return sorted(OUT)
# --------------------------------------------------------- #   
def first_hop(population, id, radius): 
    OUT = list()
    hop = get_all_unjabbed_pairs(population, radius)
    coor = get_coordinates(population, False)
    X1, Y1 = coor[id]
    for XY in coor:
      X2, Y2 = coor[XY]
      if (((Y1 - Y2)**2) + (X1 - X2)**2) <= radius**2 and XY != id: 
        OUT.append(XY)
    return sorted(OUT)
# --------------------------------------------------------- # 
def get_adjacency_set(pairs):
    OUT = dict()
    for a, b in pairs:
      if a not in OUT: OUT[a] = set() 
      if b not in OUT: OUT[b] = set() 

      OUT[a].add(b)
      OUT[b].add(a)
    return OUT      
# --------------------------------------------------------- #                   
def get_infectable_ids(pairs,seed):
      graph = get_adjacency_set(pairs)
      visited = dict()
      for u in graph: visited[u] = False
      OUT = set()
      Q = [seed]
      while len(Q) != 0:
        u = Q[0]
        Q.pop(0)
        for v in graph[u]:
          if visited[v] == False:
            OUT.add(v)
            Q.append(v)
            visited[v] = True
      return OUT
# --------------------------------------------------------- #     
