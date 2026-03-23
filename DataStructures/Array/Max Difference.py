from array import *

numbers = array('i', [2,4,5,6,7,21,5])

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

difference = max_num - min_num

print("Наибольшая разница двух чисел массива: ", difference)
