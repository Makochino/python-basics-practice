class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Вы успешно закинули: {amount}$ на ваш баланс :)"
        else:
            return f"Сумма на депозит должна быть больше 0 !!!"
        
    def withdraw(self, amount):
        if amount <= 0:
            return "Сумма снятия должна быть больше нуля"
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Вы успешно сняли: {amount}$ с вашего баланса :)"
        else:
            return f"Сумма на снятие должна быть равна или же меньше, чем количество денег на счёту!!!"
        
    def get_balance(self):
        return f"Ваш текущий баланс: {self.__balance}"
    
first_account = BankAccount()
print(first_account.deposit(1000))
print(first_account.withdraw(250))
print(first_account.get_balance())
first_account._BankAccount__balance = 3000
print(first_account.get_balance())
first_account.__balance = 2500 # We can't access this way. Only using variant from the 25th line.
print(first_account.get_balance())
        