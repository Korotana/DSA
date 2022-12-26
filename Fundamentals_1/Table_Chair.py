chairs_and_prices = [input() for i in range(int(input()))]


def get_min_price(chairs, r1, r2, r3):
    min_price = 0
    chair = 0
    if chairs % 4 == 0:
        return min_price
    chairs_needed = 4 - chairs % 4
    while chairs_needed != 0:
        if chairs_needed == 1:
            min_price += r1
            chair += 1
        elif chairs_needed == 2:
            min_price += r2
            chair += 2
        else:
            min_price += r3
            chair += 3
    return min_price


for each in chairs_and_prices:
    print(get_min_price(int(each[0]), int(each[2]), int(each[4]), int(each[6])))

# incomplete