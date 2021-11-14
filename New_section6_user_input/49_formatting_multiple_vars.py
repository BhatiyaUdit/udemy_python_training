user_ip = input("Enter your name : ")
user_ip_last = input("Enter your last_name : ")

message = f'Hello {user_ip} {user_ip_last}!'

# alternative
message2 = "Hello other format %s %s!" % (user_ip,user_ip_last)

print(message)

print(message2)