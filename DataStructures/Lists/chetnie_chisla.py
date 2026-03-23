numbers = [1, 2, 3, 4, 5, 6]

def suma_chisel(numbers):
    bebra = 0
    for num in numbers:
        if num % 2 == 0:
            bebra += 1
    return bebra

print(f"Количество чётных чисел: {suma_chisel(numbers)}")

   

