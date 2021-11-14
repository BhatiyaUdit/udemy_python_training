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


def color_gen(elevationq):
    if elevationq < 1500:
        return 'green'
    elif 1500 <= elevationq < 3000:
        return 'orange'
    else:
        return 'red'


initial_location = [39.6500015, -107.0309982]
map = folium.Map(location=initial_location, zoom_start=5, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("MyMap")
marker_locations = coordinates

for marker_location, elevation, vol_name in zip(marker_locations, elev, name):
    color = color_gen(elevation)
    feature_group.add_child(
        folium.CircleMarker(location=tuple(marker_location),
                            popup=f"{vol_name} is at {elevation} m",
                            color="grey",
                            fill_color=color,
                            fill="true",
                            fill_opacity="0.6",
                            radius=8
                            )
    )

map.add_child(feature_group)

map.save("maps/MapWithMultipleCircleMarkersFromFileWithPopUpDifferentColors.html")
# https://github.com/lennardv2/Leaflet.awesome-markers/blob/2.0/develop/examples/with-bootstrap.html
