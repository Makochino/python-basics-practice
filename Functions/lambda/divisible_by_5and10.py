numbers = [10, 15, 20, 25, 30]

divisible_numbers = list(filter(lambda num: num % 10 == 0, numbers))
print(divisible_numbers)