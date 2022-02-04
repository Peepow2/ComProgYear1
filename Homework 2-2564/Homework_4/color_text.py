def color_text(text, color):
    white_on_green = '\033[37;42m'
    white_on_yellow = '\033[34;43m'
    normal = '\033[0;0m'
    
    colored_text = ''
    if text[0] != '*' and text[0] != '?':
        if color == 'green':
            colored_text += white_on_green + text[0] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[0] + normal
    else:
        colored_text += text[0]
    
    if text[1] != '*' and text[1] != '?':
        if color == 'green':
            colored_text += white_on_green + text[1] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[1] + normal
    else:
        colored_text += text[1]
    
    if text[2] != '*' and text[2] != '?':
        if color == 'green':
            colored_text += white_on_green + text[2] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[2] + normal
    else:
        colored_text += text[2]

    if text[3] != '*' and text[3] != '?':
        if color == 'green':
            colored_text += white_on_green + text[3] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[3] + normal
    else:
        colored_text += text[3]

    if text[4] != '*' and text[4] != '?':
        if color == 'green':
            colored_text += white_on_green + text[4] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[4] + normal
    else:
        colored_text += text[4]
    return colored_text
