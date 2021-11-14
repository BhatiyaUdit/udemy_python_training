user_ip = input("Enter your name : ")

message = f'Hello {user_ip} !'

# alternative
message2 = "Hello other format %s !" % user_ip

print(message)

print(message2)

# another alternative
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))

