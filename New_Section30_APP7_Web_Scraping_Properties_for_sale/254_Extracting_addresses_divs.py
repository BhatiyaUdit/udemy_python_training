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
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(soup_divs[0])

property_prices = [div.find("h4", {"class": "propPrice"}).text.strip() for div in soup_divs]

print(property_prices)

property_details = []
for div in soup_divs:
    price = div.find("h4", {"class": "propPrice"}).text.strip()
    add_lines = div.find_all("span", {"class": "propAddressCollapse"})

    bed_count_span = div.find("span", {"class": "infoBed"})
    bed_count = bed_count_span.find("b").text if bed_count_span else None

    full_bath_count_span = div.find("span", {"class": "infoValueFullBath"})
    full_bath_count = full_bath_count_span.find("b").text if full_bath_count_span else None

    sq_footage_span = div.find("span", {"class": "infoSqFt"})
    sq_footage = sq_footage_span.find("b").text if sq_footage_span else None

    half_bath_count_span = div.find("span", {"class": "infoValueHalfBath"})
    half_bath_count = half_bath_count_span.find("b").text if half_bath_count_span else None

    property_detail = {
        'price': price
        , 'address_line_1': add_lines[0].text.strip()
        , 'address_line_2': add_lines[1].text.strip()
        , 'bed_count': bed_count
        , 'full_bath_count': full_bath_count
        , 'sq_footage': sq_footage
        , 'half_bath_count': half_bath_count
    }
    property_details.append(property_detail)
    print(property_detail)
