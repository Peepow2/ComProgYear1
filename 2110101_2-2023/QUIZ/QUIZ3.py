# Quiz_3_1 Investment Rating
Rating = dict()
Company = list()
x = input().split()
while x[0] != 'END':
    Rating[x[0]] = x[1].strip('+').strip('-')
    Company.append(x[0])
    x = input().split()

group = dict()
ALL_Money = 0
x = input().split()
while x[0] != 'END':
    r = 'None'
    for c in Company: # Find Rating
        if x[0][0:len(c)] == c: 
            r = Rating[c]
            break
        
    if r not in group:
        group[r] = 0
        
    group[r] += int(x[1])
    ALL_Money += int(x[1])
    x = input().split()

for r in ['AAA','AA','A','BBB','BB','B','CCC','CC','C','D','None']:
    if r in group:
        print(r, group[r], str(round(group[r]*100/ALL_Money, 2)) + '%')
# --------------------------------------------------------------------------------- #
# Quiz_3_2 Seating Map
def print_seats(assignments, n_rows, n_cols):
    SEAT = list()
    form = ('-- ' * n_cols).split() # Form of seat in one row
    for i in range(n_rows):
        SEAT.append(list(form))
    
    for s in assignments:
        c = int(s[1] - 1) % n_cols
        r = int(s[1] - 1) // n_cols
        SEAT[r][c] = s[0]
    
    for line in SEAT:
        print('| ' + ' | '.join(line) + ' |')
    
exec(input().strip()) # DO NOT remove this line
# --------------------------------------------------------------------------------- #
# Quiz_3_3 CU Eng Sport
player = dict()
x = input().split()
sport = list()
while x[0] != 'END':
    player[x[0]] = int(x[1]) # player[sport] = Number
    sport.append(x[0]) 
    x = input().split()

SF_PN = dict() # SF_NP[sport][department] = {NAME1, NAME2}
x = input().split()
while x[0] != 'END':
    for c in x[-1].split(','):
        if c not in SF_PN:
            SF_PN[c] = dict()
        if x[1] not in SF_PN[c]:
            SF_PN[c][x[1]] = set()
        SF_PN[c][x[1]].add(x[0])
    x = input().split()

for s in sorted(sport):
    st = s + ':'
    if s in SF_PN: 
        for d in sorted(SF_PN[s]):
            team = len(SF_PN[s][d]) // player[s]
            sub = len(SF_PN[s][d]) % player[s]
            if team != 0:
                st += d + '(' + str(team) + ',' + str(sub) + ')'
    print(st)
# --------------------------------------------------------------------------------- #
