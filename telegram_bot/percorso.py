from geopy.geocoders import Nominatim
import sqlite3
from letturaDb import  descrizioneItBot, descrizioneEngBot, posizioneBotx, posizioneBoty

geolocator = Nominatim(user_agent="VrCard")
list = []
list = posizioneBotx("Chiese")

location = geolocator.geocode(list[0][0])

print(location.latitude, location.longitude)