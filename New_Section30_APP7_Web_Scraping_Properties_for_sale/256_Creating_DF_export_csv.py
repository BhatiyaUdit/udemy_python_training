import requests
from bs4 import BeautifulSoup
import pandas

response_century_21 = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
soup = BeautifulSoup(response_century_21.content, "html.parser")
soup_divs = soup.find_all("div", {"class": "propertyRow"})

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

    # To Extract the lot size add nested loop to find the feature group with the text LOT SIZE and get value

    column_groups = div.find_all("div", {"class": "columnGroup"})
    lot_size = None
    for column_group in column_groups:
        feature_group = column_group.find("span", {"class": "featureGroup"})
        if feature_group:
            # print("feature group is present", feature_group)
            if "lot size" in feature_group.text.lower():
                feature_name = column_group.find_all("span", {"class": "featureName"})
                lot_size = "".join([val.text for val in feature_name])
                # print("Lot Size ::: ", lot_size)
                break

    property_detail = {
        'price': price
        , 'address_line_1': add_lines[0].text.strip()
        , 'address_line_2': add_lines[1].text.strip()
        , 'bed_count': bed_count
        , 'full_bath_count': full_bath_count
        , 'sq_footage': sq_footage
        , 'half_bath_count': half_bath_count
        , 'lot_size': lot_size
    }
    property_details.append(property_detail)
    # print(property_detail)


df = pandas.DataFrame(property_details)
print(df)

df.to_csv("./property_data.csv")