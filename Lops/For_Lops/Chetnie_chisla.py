chislo = int(input("Введите число: "))
total = 0

for i in range(2, chislo + 2):
    while total < chislo:
        total += 2
        print(total) 
