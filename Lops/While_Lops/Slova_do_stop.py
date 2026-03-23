skolko = 0

while True:
    slovo = str(input("Введите слово: "))
    if slovo != "стоп":
        skolko += 1
    else:
        break

print(f"Количество введенных слов: {skolko}")