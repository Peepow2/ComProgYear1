def get_all_words(board):
    words = [[], []]
    W = ""
    for i in range(15):
        for j in range(15):
            if board[i][j] == '': W += ' '
            else: W += board[i][j]
        W += ' '
        
        for j in range(15):
            if board[j][i] == '': W += ' '
            else: W += board[j][i]
        W += ' '
    
    for c in sorted(W.split()):
        if len(c) > 1: words[(is_valid(c) + 1) % 2].append(c)
    return words
