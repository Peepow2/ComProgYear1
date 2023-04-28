# HW5_TSD (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)
# ดูรายละเอียดและตัวอย่างเพิ่มเติมในคำอธิบายด้านบน

def convert_to_dict(data):
  athletes_by_Year_NOC = {}
  for s in data[1:]:
    if s[9] not in athletes_by_Year_NOC:
      athletes_by_Year_NOC[s[9]] = dict()
    if s[7] not in athletes_by_Year_NOC[s[9]]:
      athletes_by_Year_NOC[s[9]][s[7]] = list()
    
    D = dict()
    for i in range(len(data[0])): 
      D[data[0][i]] = s[i] 
    
    if D not in athletes_by_Year_NOC[s[9]][s[7]]:
      athletes_by_Year_NOC[s[9]][s[7]].append(D)
  return athletes_by_Year_NOC
#======================================
def get_medals_by_team(athletes_by_Year_NOC, year):
  medals = {}
  if year not in athletes_by_Year_NOC: return {}
  for NOC in athletes_by_Year_NOC[year]:
    M = list([0, 0, 0])
    for d in athletes_by_Year_NOC[year][NOC]:
      M[0] += int(d['Medal'] == 'Gold')
      M[1] += int(d['Medal'] == 'Silver')
      M[2] += int(d['Medal'] == 'Bronze')
    medals[NOC] = tuple(M)
  return medals
#======================================
def get_top_five(medals):
  topfive = []
  Medal_NOC = dict()
  for m in medals:
    if medals[m] not in Medal_NOC:
      Medal_NOC[medals[m]] = set()
    Medal_NOC[medals[m]].add(m)

  for MN in sorted(Medal_NOC)[::-1]:
    for N in sorted(Medal_NOC[MN]):
      topfive.append(tuple([N] + list(MN)))
    if len(topfive) >= 5: break
  return topfive
#======================================
def get_medals_trend(athletes_by_Year_NOC, NOC, start, end):
  trend = []
  for y in athletes_by_Year_NOC:
    if start <= int(y) <= end:
      M = get_medals_by_team(athletes_by_Year_NOC, y)
      if NOC in M:
        trend.append(tuple([y] + list(M[NOC])))
  return sorted(trend)
#======================================
def get_sports(athletes_by_Year_NOC, NOC, year):
  sports = set()
  if year in athletes_by_Year_NOC: 
    if NOC in athletes_by_Year_NOC[year]:
      for d in athletes_by_Year_NOC[year][NOC]:
        if d['Medal'] != 'NA':
          sports.add(d['Sport'])
  return sports
#======================================
def get_common_sports(athletes_by_Year_NOC, NOCs, year):
  sports = set()
  NOCS = list(NOCs)
  if len(NOCS) > 0:
    sports = get_sports(athletes_by_Year_NOC, NOCS[0], year)
    for N in NOCS:
      sports = sports & get_sports(athletes_by_Year_NOC, N, year)
  return sports
#======================================
