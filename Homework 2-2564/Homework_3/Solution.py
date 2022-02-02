""" Python Language
 # Task: Homework3 Exam_Seating
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
def generate_seating_sequence(group1,group2,seats_p_row):
    seat = 2 * seats_p_row
    G1 = group1 + [' -'] * (seat - len(group1))
    G2 = group2 + [' -'] * (seat - len(group2))
    
    seating_sequence = [""] * (4 * seats_p_row)
    seating_sequence[0::2] = G1
    seating_sequence[1::2] = G2
    return seating_sequence
#------------------------------------------------------------#    
def group_reverse_order(group):
    reverse_group = group[::-1]
    return reverse_group 
#------------------------------------------------------------#    
def display_exam_seating(seating_sequence):
    s = len(seating_sequence) // 4
    line1 = seating_sequence[0*s:1*s]
    line2 = seating_sequence[1*s:2*s] 
    line3 = seating_sequence[2*s:3*s] 
    line4 = seating_sequence[3*s:4*s]

    hypen = "-" * (3*s + 1)
    space = " " * ((3*s - 10) // 2)
    print(hypen)
    print("|" + space + "Exam Room" + space + "|"); print(hypen)
    print("|" + "|".join(line1) + "|"); print(hypen)
    print("|" + "|".join(line2) + "|"); print(hypen)
    print("|" + "|".join(line3) + "|"); print(hypen)
    print("|" + "|".join(line4) + "|"); print(hypen)    
    return 
#------------------------------------------------------------#    
def main():
    group1 = input().split(",")
    group2 = input().split(",")
    seats_p_row = int(input())
    is_reverse = int(input())
    
    if is_reverse:
        group1 = group_reverse_order(group1)
        group2 = group_reverse_order(group2)
        
    if len(group1) > 2*seats_p_row or len(group2) > 2*seats_p_row:
        print("Room is too small. Get a bigger exam room!")
        return
    
    if seats_p_row < 4 or seats_p_row % 2 != 0:
        print("seats_p_row has to be more than 4 and has an even number.")
        return
    
    seating_sequence = generate_seating_sequence(group1,group2,seats_p_row)
    display_exam_seating(seating_sequence)
   
main()
