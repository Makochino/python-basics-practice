def max_min(numbers):
    if not numbers:
        return None, None
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

numbers = [3, 1, 4, 1, 5, 9, 2]

maximum, minimum = max_min(numbers)
    

print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")