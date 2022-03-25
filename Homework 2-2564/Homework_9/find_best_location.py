def find_best_location(senders, receivers, address, discount , dispatch_centers):
    price = dict(); location = dict(); L = list()
    for dc in dispatch_centers:
        price[dc] = calculate_fee(senders, receivers, address, discount, dispatch_centers[dc])
    for dc in price:
        location[dc] = 0
        for p in price[dc]:
            location[dc] += price[dc][p]
    for i in location: L.append([location[i], i])
    return min(L)[::-1]
