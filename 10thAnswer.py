class Bank:
    def __init__(self):
        self.accounts = []


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance


class Transaction(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)


bank = Bank()
account1 = Transaction("12345", 1000)
account2 = Transaction("67890", 500)
bank.accounts.append(account1)
bank.accounts.append(account2)
account1.deposit(200)
account1.withdraw(100)
print(account1.check_balance())  # Outputs 1100
