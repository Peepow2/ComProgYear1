def get_play(board, new_board):
    x = y = d = 0
    v = -1
    s = ''
    for i in range(15):
        for j in range(15):   
          if board[i][j] != new_board[i][j]: 
            s += new_board[i][j]
            v = i; h = j;
            if x == 0 and y == 0: x = j; y = i
    if y < v and len(s) > 1: d = 1
    return [y, x, d, s]
