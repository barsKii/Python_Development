#Imports
import folium, pandas

#Definitions
def marker_colour(elevation):
    if lv <= 2000:
        return 'green'
    elif lv <= 3000:
        return 'orange'
    else:
        return 'red'

#Main Method
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.072155, -100.622538], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="USA Volcanoes")

for lt, ln, nm, lv in zip(lat, lon, name, elev):
    lv = int(lv)

    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(str(nm) + "\nElevation: " + str(lv) + "m",
        parse_html=True), fill_color=marker_colour(lv), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Country Populations")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] <= 100000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")



