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
    seat = int(len(seating_sequence) / 4)
    line1 = [""] + seating_sequence[0 * seat:1 * seat] + [""]
    line2 = [""] + seating_sequence[1 * seat:2 * seat] + [""]
    line3 = [""] + seating_sequence[2 * seat:3 * seat] + [""]
    line4 = [""] + seating_sequence[3 * seat:4 * seat] + [""]

    ll = "-" * len("|".join(line1))
    space = " " * int((len(ll) - 10) / 2)
    print(ll)
    print("|" + space + "Exam Room" + space + "|" + '\n' + ll)
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
