prices = {"apple": 100, "banana": 50, "milk": 80}

result = dict(map(lambda pair: (pair[0], round(pair[1] * 1.1)), prices.items()))

print(result)