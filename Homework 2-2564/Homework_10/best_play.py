def best_play(tiles,board):
    All_play = [[-1, -1, -1, -1]]
    for i in range(15):
      for j in range(15):
        for d in range(2):
          All_play.append([play(i, j, d, tiles, board), i, j, d])
    All_play.sort()
    for i in All_play:
      if i[0] == All_play[-1][0]: return i
    return [-1, -1, -1, -1]
