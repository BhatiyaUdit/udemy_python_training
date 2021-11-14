def check_temp(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    else:
        return "Cold"


user_ip = input("Inpput temp : ")
user_ip_float = float(user_ip)


print(check_temp(user_ip_float), type(user_ip_float) , user_ip_float)