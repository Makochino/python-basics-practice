#basic list comprehension 
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

#with else condition
numbers = [1,2,3,4,5,6]
odd_even_numbers = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(odd_even_numbers)

