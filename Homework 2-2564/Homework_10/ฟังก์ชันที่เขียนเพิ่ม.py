def convert(i, j, W, pos, words, board):
    if board[i][j] == '' or j == 14:
        W = (W + board[i][j]).strip()
        if len(W) > 1:
            words[(is_valid(W) + 1) % 2].append([W, pos[0][0], pos[0][1], 1])
        W = "" ; pos = []
    else:
        W += board[i][j]
        pos.append([i, j])
    return pos, W, words

def get_all_words_with_postion(board):
    words = [[], []]
    pos = list()
    W = ""
    for i in range(15):
        for j in range(15): 
          pos, W, words = convert(i, j, W, pos, words, board)  
        for j in range(15): 
          pos, W, words = convert(j, i, W, pos, words, board)
    return [sorted(words[0]), sorted(words[1])]
