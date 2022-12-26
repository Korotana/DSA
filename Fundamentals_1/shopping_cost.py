
# https://mycode.prepbytes.com/problems/fundamentals/SHOPCST

items_price = [input().split(" ") for i in range(int(input()))]

def get_cost(quantity, price):

    if quantity > 100.0:
        price = quantity * price * 0.80
        return price
    return quantity * price * 1.0

for quantity, price in items_price:
    print(get_cost(int(quantity), int(price)))