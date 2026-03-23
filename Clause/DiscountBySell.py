sell = float(input("Введите сумму продажи: "))
if sell > 0:
    if sell <= 4999:
        discount = (sell // 100) * 5
    elif sell <= 14999:
        discount = (sell // 100) * 12
    elif sell <= 24999:
        discount = (sell // 100) * 20
    else:
        discount = (sell // 100) * 30
    print("Скидка", discount)
    print("Сумма с учетом скидки", sell - discount)
else:
    print("Некорректная сумма")
