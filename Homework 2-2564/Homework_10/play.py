def play(row,col,down,tiles,board):
    V, New_board = place_tiles(row, col, down, tiles, board)
    words1 = get_all_words(board)
    words2 = get_all_words(New_board)  
    if not V or (len(words2[1]) > 0): return -1
    score = 0
    for w in words2[0]:
      if w not in words1[0]: 
        for c in w:
          score += get_value(c)
      else: words1[0].remove(w)
    return score + (int(len(tiles) >= 7) * 50)
