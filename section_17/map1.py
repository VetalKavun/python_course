import folium
import pandas


def get_color_for_height(height):
    if height <= 2000:
        return "green"
    elif height > 3000:
        return "red"
    else:
        return "orange"


map1 = folium.Map(location=[43, -107], tiles="Stamen Terrain")
data_set = pandas.read_csv("volcanoes_usa.txt", sep=",")
lat = data_set["LAT"]
lon = data_set["LON"]
elev = data_set["ELEV"]

html = """<h4>Volcano information:</h4>
Height: %s m
"""

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=10, fill_color=get_color_for_height(el),
                                     fill_opacity=0.7, color="grey"))

map1.add_child(fg)
map1.save("Map1.html")
