# check if a string in list of strings contain 'ba' or 'ab'


passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded', 'abb',
             'aaf', 'ffaec']

for password in passwords :
    if 'ab' in password or 'ba' in password:
        print(password)
