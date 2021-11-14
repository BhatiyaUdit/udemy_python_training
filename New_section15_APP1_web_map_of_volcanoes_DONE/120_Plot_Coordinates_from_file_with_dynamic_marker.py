import pandas
import folium

df = pandas.read_csv("./Volcanoes.csv")
# print(df)

lat = list(df['LAT'])
long = list(df['LON'])
elev = list(df['ELEV'])
name = list(df['NAME'])
# print(lat, long)

coordinates = []
for lt, ln, el in zip(lat, long, elev):
    coordinates.append([lt, ln])

print(coordinates)

initial_location = [39.6500015, -107.0309982]
map = folium.Map(location=initial_location, zoom_start=5, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("MyMap")
marker_locations = coordinates

for marker_location, elevation, vol_name in zip(marker_locations, elev, name):
    marker_icon = folium.Icon(color="red", icon="star", prefix="fa", spin="true")
    print("Location ", marker_location, marker_icon)
    feature_group.add_child(
        folium.Marker(location=marker_location, popup=f"{vol_name} is at {elevation} m", icon=marker_icon))

map.add_child(feature_group)

map.save("maps/MapWithMultipleMarkersFromFileWithPopUp.html")
# https://github.com/lennardv2/Leaflet.awesome-markers/blob/2.0/develop/examples/with-bootstrap.html
