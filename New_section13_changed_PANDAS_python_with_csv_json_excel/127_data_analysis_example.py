from geopy.geocoders import ArcGIS
import pandas

df_csv = pandas.read_csv('./../sample_files/supermarkets.csv')
print(df_csv)

df_csv['full_add'] = df_csv['Address'] + ', ' + df_csv['City'] + ', ' + df_csv['State'] + ', ' + df_csv['Country']

print(df_csv['full_add'])

arcGis = ArcGIS()

df_csv['Location'] = df_csv['full_add'].apply(arcGis.geocode)

print(df_csv['Location'][0])

df_csv['Latitude'] = df_csv['Location'].apply(lambda x: x.latitude)
df_csv['Longitude'] = df_csv['Location'].apply(lambda x: x.longitude)
print(df_csv)

# TODO : Complete study of lambdas with if else and while loops
