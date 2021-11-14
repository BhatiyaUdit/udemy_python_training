from Bank_Account_Program_223 import BankAccount


account = BankAccount()
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()