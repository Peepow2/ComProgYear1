def get_all_words_with_postion(board):
    words = [[], []]
    pos = list()
    W = ""
    for i in range(15):
        for j in range(15):
            if board[i][j] == '' or j == 14:
                W = (W + board[i][j]).strip()
                if len(W) > 1: words[(is_valid(W) + 1) % 2].append([W, pos[0][0], pos[0][1], 0])
                W = "" ; pos = []
            else:
                W += board[i][j]
                pos.append([i, j])
    
        for j in range(15):
            if board[j][i] == '' or j == 14:
                W = (W + board[j][i]).strip()
                if len(W) > 1: words[(is_valid(W) + 1) % 2].append([W, pos[0][0], pos[0][1], 1])
                W = "" ; pos = []
            else:
                W += board[j][i]
                pos.append([j, i])
    return [sorted(words[0]), sorted(words[1])]
