import requests

r = requests.get("https://api.playclan.hu/oxygenmusic")
print("\n")
print("Oxygen Music")
print("Most szól: "+r.content.decode())
