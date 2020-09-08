import folium

map = folium.Map(location=[59.396397, 13.534396], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[59.2, 13.3], [59.4, 13.7], [59.6, 13.9]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi Marvin, I'm a Marke!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")