import requests

lat = 31.853656
lon = 35.749980

response = requests.get(url=f'http://localhost:8080/reverse?lat={lat}&lon={lon}&format=json')
data = response.json()
# print(data)
try:
      shop = data['address']['shop']
except KeyError:
      shop = "None"
try:
      road = data['address']['road']
except KeyError:
      road = "None"
try:
      neighbourhood = data['address']['neighbourhood']
except KeyError:
      neighbourhood = "None"
try:
      suburb = data['address']['suburb']
except KeyError:
      suburb = "None"
try:
      county = data['address']['county']
except KeyError:
      county = "None"
try:
      city = data['address']['city']
except KeyError:
      city = "None"
try:
      state = data['address']['state']
except KeyError:
      state = "None"
try:
      state_district = data['address']['state_district']
except KeyError:
      state_district = "None"
try:
      postcode = data['address']['postcode']
except KeyError:
      postcode = "None"
try:
      iso = data['address']['ISO3166-2-lvl4']
except KeyError:
      iso = "None"
try:
      country = data['address']['country']
except KeyError:
      country = "None"

print(f"\nplace_id: {data['place_id']}\n"
      f"osm_type: {data['osm_type']}\n"
      f"lat: {data['lat']}\n"
      f"lon: {data['lon']}\n"
      f"display_name: {data['display_name']}\n"
      f"\nAddress:\n"
      f"shop: {shop}\n"
      f"road: {road}\n"
      f"neighbourhood: {neighbourhood}\n"
      f"suburb: {suburb}\n"
      f"county: {county}\n"
      f"city: {city}\n"
      f"country: {country}\n"
      f"state: {state}\n"
      f"state_district: {state_district}\n"
      f"postcode: {postcode}\n"
      f"ISO3166-2-lvl4: {iso}\n")
