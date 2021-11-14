# Step 1 load source code in python

import requests
from bs4 import BeautifulSoup

data = requests.get("https://pythonizing.github.io/data/example.html", headers={
    'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

print(data.text)

print(data.content)

# beautiful soup will parse the html code and return python data

soup = BeautifulSoup(data.content, "html.parser")
print(soup)
print(type(soup))
print(soup.prettify())
# find will return first div -> return TAG element
all_divs = soup.find_all("div", {"class": "cities"})

print(all_divs)
print(type(all_divs))  # returns result_set not normal list

for div in all_divs:
    all_h2_in_div1 = div.find_all("h2")
    print("h2 :: ", all_h2_in_div1)
    print("text :: ", all_h2_in_div1[0].text)

for div in all_divs:
    all_h2_in_div1 = div.find_all("p")
    print("h2 :: ", all_h2_in_div1)
    print("text :: ", all_h2_in_div1[0].text)
