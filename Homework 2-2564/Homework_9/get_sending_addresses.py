def get_sending_addresses(senders, receivers, address):
    out = list()
    for s in senders:
        if receivers.get(s, 'empty') != 'empty':
            out += [str(address[r]) for r in receivers[s]]
    return out
    # return [[str(address[r]) for r in receivers[s]] for s in senders if receivers.get(s, 'empty') != 'empty'][0]

print(get_sending_addresses(['พีพี', 'ยูนะ'], {'พีพี': ['อ๋อง', 'ไออุ่น', 'ยีน'], 'ยูนะ': ['อ๋อง', 'โบกี้', 'ปาย']}, {'พีพี' : '00/001' , 'ยูนะ' : '00/011', 'อ๋อง': '00/015', 'ไออุ่น': '00/025', 'ยีน': '00/005', 'โบกี้': '00/035', 'ปาย': '01/005'}))
