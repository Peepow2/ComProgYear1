def get_distance(address1, address2):
    address1 = int(address1.strip().replace("/",""))
    address2 = int(address2.strip().replace("/",""))
    return abs(address1-address2)

def expenses(dist, discount):
    mx = -999
    if dist == 0: return 0
    for k in discount: if mx <= k <= dist: mx = k
    return max(min(dist, 10) * 2 + max(dist - 10, 0) * 3 - discount[mx], 0)
# ---------------------------------------------------------------------------------------------- #
def get_sending_addresses(senders, receivers, address):
  return [str(address[r]) for s in senders if receivers.get(s, 'empty') != 'empty' for r in receivers[s]]

def get_item_count(sending_addresses):
    OUT = dict()
    for sa in sending_addresses:
        if OUT.get(sa, 'empty') != 'empty':
            OUT[sa] = 0
        OUT[sa] += 1
    return OUT
  
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
  
def find_best_location(senders, receivers, address, discount , dispatch_centers):
    price = dict(); location = dict(); L = list()
    for dc in dispatch_centers:
        price[dc] = calculate_fee(senders, receivers, address, discount, dispatch_centers[dc])
    for dc in price:
        location[dc] = sum([int(price[dc][e]) for e in price[dc]])
    return min([[location[i], i] for i in location])[::-1]
