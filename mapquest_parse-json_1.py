import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy"
dest = "Frascati, Italy"
key = "yPM6tDNg7nm5QGKZbx8HYjNNU1GnktEM"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)