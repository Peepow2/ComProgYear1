sol, c, inc = input().split(",")
ans = input(); c = int(c); inc = int(inc)
score = tuk = pid = no = 0;
ans += "-" * (len(sol) - len(ans))
for i in range(len(ans)):
    if ans[i] == sol[i]:
        score += c; tuk += 1
    elif ans[i] != sol[i] and ans[i] != '-':
        score -= inc; pid += 1
    else: no += 1
print(tuk, pid, no, max(score, 0))
