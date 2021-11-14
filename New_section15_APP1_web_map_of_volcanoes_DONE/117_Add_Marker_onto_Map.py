import folium

initial_location = [38.58, 99.09]
map = folium.Map(location=initial_location, zoom_start=5, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("MyMap")
marker_location = [27.6, 80.1]
marker_icon = folium.Icon(color="green")

feature_group.add_child(folium.Marker(location=marker_location, popup="My Marker", icon=marker_icon))
map.add_child(feature_group)

map.save("maps/MapWithMarker.html")
