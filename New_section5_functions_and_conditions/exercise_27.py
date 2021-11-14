# temp  check with elif

def check_temp(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    else:
        return "Cold"

print(check_temp(6))

# elif temp >= 15 and temp <= 25:
# can be simplified to 15 <= temp <= 25
