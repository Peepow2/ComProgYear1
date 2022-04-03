def get_all_words(board):
    words = [[], []]
    W = ""
    for i in range(15):
        W += ' '
        for j in range(15):
            if board[i][j] != '': W += board[i][j]
            else: W += ' '
        W += ' '
        for j in range(15):
            if board[j][i] != '': W += board[j][i]
            else: W += ' '
    
    for c in sorted(W.split()):
        if len(c) > 1: words[(is_valid(c) + 1) % 2].append(c)
    return words
