import requests
from bs4 import BeautifulSoup

# The Actual website is changed so using cached version

# in the example URL is not protected and can be used directly
# also pages have different URLS

response_century_21 = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

# print(response_century_21.content)

soup = BeautifulSoup(response_century_21.content, "html.parser")

# print(soup.prettify())

soup_divs = soup.find_all("div", {"class": "propertyRow"})
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(soup_divs[0])

property_prices = [div.find("h4", {
    "class": "propPrice"
}).text.strip() for div in soup_divs]

print(property_prices)

property_details = []
for div in soup_divs:
    property_detail = {'price': div.find("h4", {"class": "propPrice"}).text.strip()
                       # ,'bed_count': div.find("div", {"class": "infoLine1"}).text.strip()
                       }
    property_details.append(property_detail)

print(property_details)
