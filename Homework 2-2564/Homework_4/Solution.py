# ให้เขียนโปรแกรมในเซลล์นี้เท่านั้น ห้ามลบ/แก้ไข ข้อความในบรรทัดแรกนี้ 

import random
import string

def get_word():
    # สามารถเพิ่มคำใน words ได้
    words = ["HAPPY", "IMAGE", "TOURS", "FLOOD", "BLOCK", 
             "STORE", "AMONG", "TWEET", "OFTEN", "STILL",
             "STYLE", "LIGHT", "MIGHT", "WOULD", "SEVEN"]
    return random.choice(words).upper()

def get_five_letter_word():
    # คืนค่าเป็นคำที่มีความยาว = 5
    print('  Guess a five-letter word >> ', end='')
    guess = input()
    while len(guess) != 5:
        print('  Please enter a five-letter word >> ', end='')
        guess = input()
    return guess.upper()
            
def show_game_status(correct, wrong, not_used):
    correct = color_text(correct, 'green')
    wrong = color_text(wrong, 'yellow')
    print('  Correct letters - [{}]'.format(correct))
    print('  Wrong position - [{}]'.format(wrong))
    print('  Letters not used - [{}]'.format(not_used))

def check_guess_word(puzzle_word, guess_word):
    # ตรวจอักขระคำที่ทาย (guess_word) เทียบกับโจทย (puzzle_word)
    # โดยจะตรวจทีละตัวอักขระ ตั้งแต่ 0, 1, 2, 3, 4
    used = ''
    correct = '?????'
    wrong_position = '*****'
    for k in range(5):
        ch = guess_word[k]
        correct_kth, wrong_position_kth, puzzle_word = check_kth_letter(puzzle_word, k, ch)

        # รวม correct, wrong_position กับ ผลของการ check ครั้งก่อนหน้า
        correct = combine_word(correct, correct_kth, '?')
        wrong_position = combine_word(wrong_position, wrong_position_kth, '*')
        used += ch
    return correct, wrong_position, used

def replace_letter(original, old_letter, new_letter):
    # คืนค่าเป็นสตริงที่เปลี่ยน อักขระใน original จาก old_letter ไปเป็น new_letter
    # original เป็นสตริงที่ไม่มีตัวอักขระซ้ำกันแน่ ๆ
    if old_letter in original:
        k = original.find(old_letter)
        original = original[:k] + new_letter + original[k+1:]
    return original    

def replace_letters(letters, letters_to_remove):
    # เปลี่ยนทุกอักขระใน letters ที่อยู่ใน letters_to_remove ให้เป็น '-'
    for ch in letters_to_remove:
        # เปลี่ยนอักขระ ch ใน letters ให้เป็น '-'
        letters = replace_letter(letters, ch, '-')
    return letters

#------------------------------------------------------------------------
# เพิ่มรายละเอียดใน function ข้างล่างนี้
#------------------------------------------------------------------------
def combine_word(s1, s2, default_ch):
    result = ""
    result += chr(ord(s1[0]) + ord(s2[0]) - ord(default_ch))
    result += chr(ord(s1[1]) + ord(s2[1]) - ord(default_ch))
    result += chr(ord(s1[2]) + ord(s2[2]) - ord(default_ch))
    result += chr(ord(s1[3]) + ord(s2[3]) - ord(default_ch))
    result += chr(ord(s1[4]) + ord(s2[4]) - ord(default_ch))
    return result

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

def color_text(text, color):
    # สีที่ใช้แสดง ห้ามเปลี่ยน
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

    return text
#------------------------------------------------------------------------
# สิ้นสุดส่วนที่นิสิตต้องทำ
#------------------------------------------------------------------------

def main():
    # ห้ามแก้ไขหรือเพิ่มเติม code ใน main()
    solve = False
    puzzle_word = get_word()

    print("Do you want to show the puzzle word? [enter y or n]")
    show_puzzle = (input().upper() == 'Y')
    if show_puzzle:
        print('Puzzle word:', puzzle_word)

    correct_letters = '?????' 
    letters_wrong_position = '*****'
    letters_never_used = string.ascii_uppercase
    show_game_status(correct_letters, letters_wrong_position, letters_never_used)

    MAX_TRIES = 6
    for i in range(MAX_TRIES):
        print('-'*30)
        print('Try #', i+1)
        guess_word = get_five_letter_word()
        
        correct_letters, letters_wrong_position, used = check_guess_word(puzzle_word, guess_word)
        letters_never_used = replace_letters(letters_never_used, used)

        show_game_status(correct_letters, letters_wrong_position, letters_never_used)
        if guess_word == puzzle_word:
            solve = True
            break
        
    if solve:
        print('You got it in {}/{}'.format(i+1, MAX_TRIES))
    else:
        print('You cannot solve this puzzle after', MAX_TRIES, 'times.')

main()
