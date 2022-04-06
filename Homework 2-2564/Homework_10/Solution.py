# Function 1: get_all_words
# Return SORTED lists of CAPITALIZED words as [valid_words,invalid_words] of every words in the board, DUPLICATES are acceptable 
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
    return words
# ------------------------------------------------------------------------
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

# Function 2: get_play
# Return [row,col,down,tiles] such that calling place_tiles(row,col,down,tiles,board)[1] would result in new_board
def get_play(board, new_board):
    s = ''
    pos = list()
    for i in range(15):
        for j in range(15):   
          if board[i][j] != new_board[i][j]: 
            s += new_board[i][j]
            pos.append([j, i])
    d = 0
    if pos[0][1] < pos[-1][1]: d = 1
    return [pos[0][1], pos[0][0], d, s]

# Function 3: play
# Return score | score is score from the play
# If play is not valid, return -1
def play(row,col,down,tiles,board):
    V, New_board = place_tiles(row, col, down, tiles, board)
    words1 = get_all_words_with_postion(board)
    words2 = get_all_words_with_postion(New_board)  
    if not V or (len(words2[1]) > 0): return -1
    score = 0
    for w in words2[0]:
      if w not in words1[0]: 
        for c in w[0]:
          score += get_value(c)
    return score + (len(tiles) >= 7) * 50

# Function 4 : best_play
# Return [score, row, col, down]  highest score achievable with these tiles on current board
def best_play(tiles,board):
    All_play = [[-1, -1, -1, -1]]
    for i in range(15):
      for j in range(15):
        for d in range(2):
          All_play.append([play(i, j, d, tiles, board), i, j, d])
    All_play.sort()
    for l in All_play:
      if l[0] == All_play[-1][0]: return l
