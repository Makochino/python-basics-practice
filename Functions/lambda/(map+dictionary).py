prices = {"apple": 100,
          "banana": 65,
          "cheese": 150}

wopper = 0

while wopper < 1:
    for key, value in prices.items():
        prices[key] = round(value * 1.1)
    wopper += 1

print(prices)
