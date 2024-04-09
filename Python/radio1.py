import requests

r = requests.get("https://api.playclan.hu/radio1")
print("\n")
print("Rádió 1")
print("Most szól: "+r.content.decode())
