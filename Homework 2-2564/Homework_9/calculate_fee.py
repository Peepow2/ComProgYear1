def get_distance(address1, address2):
    address1 = int(address1.strip().replace("/",""))
    address2 = int(address2.strip().replace("/",""))
    return abs(address1-address2)

def expenses(dist, discount):
    mx = -999
    if dist == 0: return 0
    for k in discount:
        if mx <= k and k <= dist: mx = k
    return max(min(dist, 10) * 2 + max(dist - 10, 0) * 3 - discount[mx], 0)
    
def calculate_fee(senders, receivers, address, discount, dispatch_center_addr):
    out = dict(); dis = dict()
    for s in senders:
        if s not in dis: dis[s] = 0
        if s in receivers:
            for r in receivers[s]:
                dis[s] += get_distance(dispatch_center_addr, address[r])
    for s in dis:
        out[s] = expenses(dis[s], discount)
    return out
  
# ---------------------- Test ---------------------- #
senders = ['โมบิว','เอแคลร์','เจเจ']
receivers = {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}
address = {'เจเจ' : '00/001' ,'โมบิว' : '00/011','กู๊ด':'00/005' ,'เอแคลร์': '00/015'}
discount = {1: 0 , 3: 9, 4: 10, 8: 7}
dispatch_center_addr = '00/000'

print(calculate_fee(senders, receivers, address, discount, dispatch_center_addr))
# {'โมบิว' : 0, 'เอแคลร์' : 0,'เจเจ' : 61}
