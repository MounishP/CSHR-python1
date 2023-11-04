class Bank:
    def __init__(self):
        self.accounts = []

    def createAccount(self, accountHolder, initialBalance=0):
        account = Account(accountHolder, initialBalance)
        self.accounts.append(account)
        return account

    def getAccount(self, accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account
        return None


class Account:
    accountCounter = 32100441100001

    def __init__(self, accountHolder, initialBalance):
        self.accountHolder = accountHolder
        self.balance = initialBalance
        self.accountNumber = Account.accountCounter
        Account.accountCounter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited amount is {amount}. New balance: {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New Balance: {self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"

    def checkBalance(self):
        return f"Account balance for {self.accountHolder}: {self.balance}"


class Transaction(Account):
    def __init__(self, accountHolder, initialBalance = None):
        if initialBalance is not None:
            super().__init__(accountHolder, initialBalance)
        else:
            super(Transaction, self).__init__(accountHolder, 0)

    def performDeposit(self, amount):
        return self.deposit(amount)

    def performWithdrawal(self, amount):
        return self.withdraw(amount)

    def performCheckBalance(self):
        return super().checkBalance()


# Sample
bank = Bank()

# Create accounts
mounishAccount = bank.createAccount("Mounish", 1000)
ravaliAccount = bank.createAccount("Ravali")

# #Perform transactions
mounish_transactions = Transaction("Mounish", 1000)
mounishDeposit = mounish_transactions.performDeposit(300)
mounishWithdraw = mounish_transactions.performWithdrawal(500)
mounishBalance = mounish_transactions.performCheckBalance()
print(mounishDeposit)
print(mounishWithdraw)
print(mounishBalance)

ravaliTransactions = Transaction("Ravali")
print(ravaliTransactions.performCheckBalance())
print(ravaliTransactions.performDeposit(867565))
print(ravaliTransactions.performWithdrawal(2345))