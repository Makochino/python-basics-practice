class BankAccount:
    def __init__(self, number, amount):
        self.account_number = number
        self.balance = amount
        print("Вас приветствует банковское приложение!!!")
        print(self)  # Теперь красиво выводит баланс

    def add(self, amount):
        self.balance += amount
        print(f"✅ Ваш баланс пополнен. Новый баланс: {self.balance:.2f} руб.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅ Вы сняли {amount:.2f} руб. Новый баланс: {self.balance:.2f} руб.")
        else:
            print(f"❌ Недостаточно средств! Баланс: {self.balance:.2f} руб.")

    def __str__(self):
        """ Красивый вывод информации о счёте """
        return f"💳 Номер счёта: {self.account_number}\n💰 Баланс: {self.balance:.2f} руб."

# Создаём счёт
account1 = BankAccount(12354312, 1000)

while True:
    operation = input("\nВыберите операцию (добавить, снять): ").strip().lower()

    if operation in ["добавить", "снять"]:
        try:
            amount = float(input("Введите сумму: ").strip())
            if amount <= 0:
                print("❌ Ошибка: сумма должна быть больше 0!")
                continue

            if operation == "добавить":
                account1.add(amount)
            else:
                account1.withdraw(amount)

        except ValueError:
            print("❌ Ошибка: введите число!")

    else:
        print("❌ Ошибка: такой операции нет!")

    again = input("\nХотите выполнить операцию снова? (введите 'exit' для выхода): ").strip().lower()
    if again == "exit":
        print("🚪 Вы вышли из приложения. До свидания!")
        break
