from geopy.geocoders import ArcGIS
from process_csv import process_csv_start


# arcGis = ArcGIS()
#
# data = arcGis.geocode("3666 21st St San Francisco CA 94114 USA")
# print(data.latitude)


data, error = process_csv_start()

print(data)

dict_data = data.T.to_dict()

print(dict_data)