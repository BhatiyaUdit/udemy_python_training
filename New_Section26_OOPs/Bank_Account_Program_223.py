class BankAccount:
    def __init__(self):
        print("INSIDE SELF")
        with open('balance_223.txt', 'r') as account:
            balance = int(account.read())
            self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open('balance_223.txt', 'w') as file:
            file.write(str(self.balance))
