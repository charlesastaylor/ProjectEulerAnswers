"""Problem 31 - Coin sums"""

coins = reversed([1, 2, 5, 10, 20, 50, 100, 200])
pos_way = []
ways = set()
while True:
    for coin in coins:
        # print(coin)
        pos_way.append(coin)
        if sum(pos_way) == 200:
            ways.add(tuple(sorted(pos_way)))
            del pos_way[-1]
            continue
        if sum(pos_way) > 200:
            del pos_way[-1]
            continue
        print(ways)
        break
    