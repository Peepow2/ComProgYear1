def play(row,col,down,tiles,board):
    V, New_board = place_tiles(row, col, down, tiles, board)
    if not V: return -1
    words1 = get_all_words(board)
    words2 = get_all_words(New_board)
    score = 0
    for w in words2[0]:
      if w not in words1[0]: 
        for c in w:
          score += get_value(c)
      else: words1[0].remove(w)
    if len(tiles) >= 7: score += 50
    return score
