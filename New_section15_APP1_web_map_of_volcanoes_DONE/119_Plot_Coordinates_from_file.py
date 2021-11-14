import pandas
import folium

df = pandas.read_csv("./Volcanoes.csv")
# print(df)

lat = list(df['LAT'])
long = list(df['LON'])

# print(lat, long)

coordinates = []

for lt, ln in zip(lat, long):
    coordinates.append([lt, ln])

print(coordinates)

initial_location = [39.6500015, -107.0309982]
map = folium.Map(location=initial_location, zoom_start=5, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("MyMap")
marker_locations = coordinates

for marker_location in marker_locations:
    marker_icon = folium.Icon(color="red")
    print("Location ", marker_location, marker_icon)
    feature_group.add_child(folium.Marker(location=marker_location, popup="My Marker", icon=marker_icon))

map.add_child(feature_group)

map.save("maps/MapWithMultipleMarkersFromFile.html")
