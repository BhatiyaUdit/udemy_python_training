# password length check
def check_pass(passs):
    if len(passs) >= 8:
        return True
    else:
        return False


print(check_pass("sssasa"))
