import requests
from bs4 import BeautifulSoup

# The Actual website is changed so using cached version

# in the example URL is not protected and can be used directly
# also pages have different URLS

response_century_21 = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

# print(response_century_21.content)

soup = BeautifulSoup(response_century_21.content, "html.parser")

print(soup.prettify())