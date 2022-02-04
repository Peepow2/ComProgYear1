def replace_kth_letter_in_str(original_str, k, ch):
    return original_str[0:k] + ch + original_str[k+1:]

def check_kth_letter(word, k, ch):
    correct = '?????'
    wrong_position = '*****'
    if word[k] == ch: 
        correct = replace_kth_letter_in_str(correct, k, ch)
    if (word[k] != ch) and (ch in word): 
        wrong_position = replace_kth_letter_in_str(wrong_position, k, ch)
    if ch in word:
        if word[0] == ch:
            word = replace_kth_letter_in_str(word, 0, '-')
        elif word[1] == ch:
            word = replace_kth_letter_in_str(word, 1, '-')
        elif word[2] == ch:
            word = replace_kth_letter_in_str(word, 2, '-')
        elif word[3] == ch:
            word = replace_kth_letter_in_str(word, 3, '-')
        else:
            word = replace_kth_letter_in_str(word, 4, '-')
    return correct, wrong_position, word
