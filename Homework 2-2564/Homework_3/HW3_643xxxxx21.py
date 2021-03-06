""" Python Language
 # Task: Homework3 Exam_Seating
 # Code: Peerawich Sodsuay
 # Warning: Don't copy this code to submit.
 # If you do it, your score will be cancel immediately.
"""
def generate_seating_sequence(group1,group2,seats_p_row):
    No_seat = 4 * seats_p_row
    seating_sequence = [" -"] * No_seat
    seating_sequence[0:2*len(group1):2] = group1
    seating_sequence[1:2*len(group2)+1:2] = group2 
    return seating_sequence
#------------------------------------------------------------#    
def group_reverse_order(group):
    reverse_group = group[::-1]
    return reverse_group 
#------------------------------------------------------------#
def display_exam_seating(seating_sequence):
    seat = int(len(seating_sequence) / 4)
    line1 = [""] + seating_sequence[0 * seat: 1 * seat] + [""]
    line2 = [""] + seating_sequence[1 * seat: 2 * seat] + [""]
    line3 = [""] + seating_sequence[2 * seat: 3 * seat] + [""]
    line4 = [""] + seating_sequence[3 * seat: 4 * seat] + [""]
    
    ll = "-" * ((3 * seat) + 1)
    space = " " * int((len(ll) - 11) / 2)
    print(ll + '\n' + "|" + space + "Exam Room" + space + "|" + '\n' + ll)
    print("|".join(line1) + '\n' + ll)
    print("|".join(line2) + '\n' + ll)
    print("|".join(line3) + '\n' + ll)
    print("|".join(line4) + '\n' + ll)
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
