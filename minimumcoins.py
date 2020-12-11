def minimum_coins(c, v, list):
    change = 0
    new_v = v
    for i in c:
        change += new_v // i
        new_v = new_v % i
    list.append(change)
    c.pop(0)
    if c == []:
        minimum = min(list)
        print(minimum)
    else:
        minimum_coins(c, v, list)


coins = [11, 9, 6, 5, 1]
V = 11
list = []

minimum_coins(coins, V, list)
