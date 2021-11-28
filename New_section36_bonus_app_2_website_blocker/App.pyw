import time
from datetime import datetime

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
hosts_temp = './hosts'
linux_path = '/etc/hosts'

redirect_site = '127.0.0.1'
restricted_sites = ['www.facebook.com', 'facebook.com', 'www.google.com']

while True:
    print("Inside infinite loop...")
    current_date = datetime.now()
    lower_limit = datetime(current_date.year, current_date.month, current_date.day, 8)
    upper_limit = datetime(current_date.year, current_date.month, current_date.day, 16)
    if lower_limit < current_date < upper_limit:
        print("Working Hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in restricted_sites:
                if website not in content:
                    file.write("\n" + redirect_site + " " + website)
    else:
        print("Fun Hours")
        with open(hosts_path, 'r+') as file_fun:
            content_lines = file_fun.readlines()
            file_fun.seek(0)
            file_fun.truncate()
            for line in content_lines:
                if not any(website in line for website in restricted_sites):
                    file_fun.write(line)
    time.sleep(2)
