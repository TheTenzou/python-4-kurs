import os
import pathlib

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from IPython.display import display, HTML
import folium
import pandas as pd


def valid_shop(node):
    for tag in node('tag'):
        if tag['k'] == 'shop' and tag['v'] != 'supermarket':
            return True

    return False


def have_name(node):
    for tag in node('tag'):
        if tag['k'] == 'name':
            return True
    
    return False


def get_shop(node):
    for tag in node('tag'):
        if tag['k'] == 'name':
            return { 'name': tag['v'], 'coordinates': [ float(node['lat']), float(node['lon']) ] }

    return { 'name': 'no name', 'coordinates': [ 'no', 'no' ] }


dirname = os.path.dirname(__file__)
file_name = os.path.join(dirname, 'map.osm')
url = pathlib.Path(file_name).as_uri()

resp = urlopen(url)
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')

list_of_shops = list()
for node in soup.find_all('node'):
    if valid_shop(node) and have_name(node):
        list_of_shops.append(get_shop(node))

my_map = folium.Map(location=[55.6726296, 37.5076253], zoom_start = 16)

for shop in list_of_shops:
    folium.Marker(
        shop['coordinates'],
        popup=shop['name']
    ).add_to(my_map)

my_map.save('map.html')

print(len(list_of_shops))