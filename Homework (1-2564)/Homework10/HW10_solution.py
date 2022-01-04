""" Python Language
 # Task: Homework10 Super Powerful and Justify Blockchain
 # Code: Peerawich Sodsuay 
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
# (1)
# Sorting Transaction by timestamp
def sorting_transaction(transaction_list):
    out = copy_list(transaction_list)
    temp = []; 
    for c in out:
        temp.append([c[3], c])
    temp.sort();
    out = [];
    for t in temp:
        out.append(t[1])
    return out
# ----------------------------------------------------------------------
# (2)
# Hash all transaction into one hash string
def hash_transaction_list(transaction_list):
    trans = copy_list(transaction_list)
    trans = sorting_transaction(trans)
    out = ""
    for t in trans:
        out += t[-1]
    return hash_sha256(out)
# ----------------------------------------------------------------------
def find_user(name, LIST):
    idx = 0
    for t in LIST:
        if t[0] == name:
            return idx;
        idx += 1
    return -1 
# ----------------------------------------------------------------------
def update(oon, rub, money, ledgers):
    idx1 = find_user(oon, ledgers)
    idx2 = find_user(rub, ledgers)

    if oon == ('0' * 64):
        if idx2 >= 0:
            ledgers[idx2][1] += money
        else:
            ledgers.append([rub, money])
        return [True, ledgers]

    if idx1 >= 0:
        if ledgers[idx1][1] < money:
             return [False, ledgers]
        if ledgers[idx1][1] >= money:
            if idx2 == -1:
                ledgers[idx1][1] -= money
                ledgers.append([rub, money])
            else:
                ledgers[idx1][1] -= money
                ledgers[idx2][1] += money
        return [True, ledgers]
    return [False, ledgers]
# ----------------------------------------------------------------------
# (3)
# Update the ledger from transaction_list
def update_ledger(ledger, transaction_list):
    LEDGER = copy_list(ledger)
    trans = copy_list(transaction_list)
    trans = sorting_transaction(trans)

    for itr in trans:
        not_fail, LEDGER = update(itr[0], itr[1], itr[2], LEDGER)
        if not not_fail:
            return [ledger, [False, itr]]
    return [LEDGER, [True, []]]
# ----------------------------------------------------------------------
def find_first(block):
    size = len(block)
    for i in range(size):
        found = False
        for j in range(size):
            if block[i][2] == block[j][3]:
                found = True
        if not found:
            return block[i]
# ---------------------------------------------------------------------- 
# (4)
# Sorting block in to chain
def sorting_block(block_list):
    if block_list == []: return []
    block = copy_list(block_list)
    ret = []
    first = find_first(block)
    ret.append(first)
    for t in ret:
        for c in block:
            if t[3] == c[2]:
                ret.append(c)
    return ret
# ----------------------------------------------------------------------
# (5)
# Check the chain that transaction is valid to what number block
def maximum_valid_block(block_list):
    block = copy_list(block_list)
    block = sorting_block(block)
    LEDGER = []; cnt = 0
    for sub in block:
        sub[0] = sorting_transaction(sub[0])
    for itr in block:
        LEDGER, state = update_ledger(LEDGER, itr[0])
        fail = not state[0]
        if fail:
            return cnt
        cnt += 1
    return cnt
# ----------------------------------------------------------------------
# (6)
def block_ledger(block_list, block_no):
    block = copy_list(block_list)
    block = sorting_block(block)
    LEDGER = []
    LAST = maximum_valid_block(block)
    for i in range(0, min(LAST, block_no)):
        LEDGER, state = update_ledger(LEDGER, block[i][0])    
    return [LEDGER, min(LAST, block_no)]
# ----------------------------------------------------------------------
