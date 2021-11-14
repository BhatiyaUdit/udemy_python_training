import folium

initial_location = [38.58, 99.09]
map = folium.Map(location=initial_location, zoom_start=5, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("MyMap")
marker_locations = [[27.6, 80.1], [38.6, 99.1], [45.6, 80.1]]

# All Marker object needs a diffrent icon object as well

for marker_location in marker_locations:
    marker_icon = folium.Icon(color="red")
    print("Location ", marker_location, marker_icon)
    feature_group.add_child(folium.Marker(location=marker_location, popup="My Marker", icon=marker_icon))

map.add_child(feature_group)

map.save("maps/MapWithMultipleMarkers.html")
