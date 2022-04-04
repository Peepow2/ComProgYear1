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
