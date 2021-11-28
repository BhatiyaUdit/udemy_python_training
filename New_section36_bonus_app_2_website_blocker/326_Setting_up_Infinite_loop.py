import time
from datetime import datetime

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

redirect_site = '127.0.0.1'
restricted_sites = ['www.facebook.com', 'facebook.com']

while True:
    print("Inside infinite loop...")
    current_date = datetime.now()
    lower_limit = datetime(current_date.year, current_date.month, current_date.day, 8)
    upper_limit = datetime(current_date.year, current_date.month, current_date.day, 18)
    if lower_limit < current_date < upper_limit:
        print("Working Hours")
    else:
        print("Fun Hours")
    time.sleep(2)
