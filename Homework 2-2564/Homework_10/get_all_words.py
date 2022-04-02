def get_all_words(board):
    words = [[], []]
    check = list()
    for i in range(15):
        write = False
        for j in range(15):
            if write == False: check.append("")
            write = board[i][j] != ''
            if write: check[-1] += board[i][j]
                
        write = False
        for j in range(15):
            if write == False: check.append("")
            write = (board[j][i] != '')
            if write: check[-1] += board[j][i]
            
    for c in sorted(check):
        if len(c) > 1:
            if is_valid(c): words[0].append(c)
            else: words[1].append(c)
    return words
