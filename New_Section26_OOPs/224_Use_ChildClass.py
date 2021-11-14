from Inheritance_224 import CheckingAccount

c = CheckingAccount(2)
print(c.balance)
c.transfer(100)
print(c.balance)
c.commit()
