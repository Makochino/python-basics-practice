ones = {
    0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
    6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
}

teens = {
    10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
    14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 
    17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"
}

tens = {
    2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
    6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"
}

hundreds = {
    1: "сто", 2: "двести", 3: "триста", 4: "четыреста",
    5: "пятьсот", 6: "шестьсот", 7: "семьсот", 
    8: "восемьсот", 9: "девятьсот"
}

def number_to_words(num):
    if num < 10:  
        return ones[num]
    elif num < 20:  
        return teens[num]
    elif num < 100:  
        tens_digit = num // 10
        ones_digit = num % 10
        return tens[tens_digit] + (" " + ones[ones_digit] if ones_digit != 0 else "")
    else:  
        hundreds_digit = num // 100
        remainder = num % 100
        if remainder == 0:
            return hundreds[hundreds_digit]
        else:
            return hundreds[hundreds_digit] + " " + number_to_words(remainder)

num = int(input("Введите число (0-999): "))
if 0 <= num <= 999:
    print("Вывод:", number_to_words(num))
else:
    print("Число вне диапазона!")