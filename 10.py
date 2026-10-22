class BankError(Exception):
    """Базовое исключение"""
class InvalidAmountError(BankError):
    def __init__(self, amount):
        super().__init__(f"Неправильная сумма: {amount}")
        self.amount=amount
class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f"Недостаточно средств: не хватает {amount-balance}")
        self.balance=balance
        self.amount=amount
class AccountBlockedError(BankError):
    def __init__(self, blocked):
        super().__init__(f"Аккаунт заблокирован")
        self.blocked=blocked
def withdraw(balance,amount):
    if amount <=0:
        raise InvalidAmountError(amount)
    if amount>balance:
        raise InsufficientFundsError(balance, amount)
    return balance-amount
balance=float(input("Введите баланс: "))
amount=float(input("Введите сумму: "))
try:
    NewBalance=withdraw(balance, amount)
    print(f"Снятие {amount}: новый баланс {NewBalance}")
except InvalidAmountError as e:
    print(e)
except InsufficientFundsError as e:
    print(e)
except AccountBlockedError as e:
    print(e)
