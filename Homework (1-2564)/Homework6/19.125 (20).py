""" Python Language
 # Task: Homework6 List Processing
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
def filter_similarity(data, t, u_or_s):
  # uid1 uid2 sid1 sid2 t
    temp_list = list()
    ret_list = list()
    size = len(data)
    for i in range(size):
        if data[i][4] >= t:
            if u_or_s == 'u':
                temp_list += [[data[i][0], data[i][1]]]
            if u_or_s == 's':
                temp_list += [[data[i][2], data[i][3]]]
    temp_list.sort()
    temp_list += [[0, 0]]
    en = len(temp_list) - 1
    for i in range(en):
        if temp_list[i] != temp_list[i+1]:
            ret_list += [temp_list[i]]
    return ret_list
# -------------------------------------------------------------------------------------- End filter_similarity
def find_groups(sim_pairs):
  wg = list()
  size = len(sim_pairs)
  for i in range(size):
      idx1 = find_group_index(sim_pairs[i][0], wg)
      idx2 = find_group_index(sim_pairs[i][1], wg)
      if idx1 == -1 and idx2 == -1:
        wg.append(list(sim_pairs[i]))
      elif idx1 >= 0 and idx2 == -1:
        wg[idx1] += [sim_pairs[i][1]]
      elif idx1 == -1 and idx2 >= 0:
        wg[idx2] += [sim_pairs[i][0]]
      elif idx1 != idx2:
        if idx1 > idx2:
          idx1, idx2 = idx2, idx1
        wg[idx1] += wg[idx2]
        wg.pop(idx2)
        size =- 1
  for temp in wg:
    temp.sort()
  wg.sort()
  return wg
# -------------------------------------------------------------------------------------- End find_groups
def find_number_of_similar_users(user_pairs, n):
    temp = list()
    for e in user_pairs:
        temp += e
    temp.sort()
    user = []; freq = []; 
    cnt = 0; k = temp[0]
    for e in temp:
        if e == k:
            cnt += 1
        else:
            user += [k]
            freq.append(cnt * -1) 
            k = e
            cnt = 1
    user.append(k)
    freq.append(cnt * -1)
    temp_freq = sorted(freq) 
    user1 = []
    size = len(temp_freq)
    
    for e in range(size):
        idx = freq.index(temp_freq[e])
        user1 += [user[idx]]
    
    for e in user:
        if e not in user1:
            user1 += [e]
    ret_list = [user1[0]]
    cnt = user1[0]
    size = len(user1)
    for i in range(size):
        if (user1[i]  != cnt) and (user1[i] not in ret_list):
            ret_list += [user1[i]]
            cnt = user1[i]
        else:
            pass
    return ret_list[:n:]
# -------------------------------------------------------------------------------------- End find_number_of_similar_users
