def get_item_count(sending_addresses):
    OUT = dict()
    for sa in sending_addresses:
        if sa not in OUT:
            OUT[sa] = 0
        OUT[sa] += 1
    return OUT
# ---------------------- Test ---------------------- #
print(get_item_count(['10/000', '00/001', '00/011', '00/011', '00/009']))
# return {'10/000' : 1, '00/001' : 1, '00/011' : 2, '00/009' : 1})
