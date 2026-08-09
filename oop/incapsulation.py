class BankAccount:

    name = "Sandeep Kumar"

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(15000)

account.deposit(2000)
print(f" Total Balance Amount  : {account.get_balance()}")
print(f"Account Holder Name : {BankAccount.name}")

