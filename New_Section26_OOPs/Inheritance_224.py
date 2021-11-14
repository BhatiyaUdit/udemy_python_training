from Bank_Account_Program_223 import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, fee):
        BankAccount.__init__(self)
        print(__name__, "INIT ")
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
