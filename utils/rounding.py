def round_to_tick(price):
    if price < 200: tick = 1
    elif price < 500: tick = 2
    elif price < 2000: tick = 5
    elif price < 5000: tick = 10
    else: tick = 25
    return int(round(price / tick) * tick)
