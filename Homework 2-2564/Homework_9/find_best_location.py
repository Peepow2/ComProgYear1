def find_best_location(senders, receivers, address, discount , dispatch_centers):
    price = dict(); location = dict(); 
    for dc in dispatch_centers:
        price[dc] = calculate_fee(senders, receivers, address, discount, dispatch_centers[dc])
    for dc in price:
        location[dc] = sum([int(price[dc][e]) for e in price[dc]])
    return min([[location[i], i] for i in location])[::-1]
