import requests

lat = 30.257230
lon = 28.483885

response = requests.get(url=f'http://localhost:8080/reverse?lat={lat}&lon={lon}&format=json')
data = response.json()

elements = ['shop', 'road', 'neighbourhood', 'suburb', 'county', 'city', 'state', 'state_district', 'country', 'postcode', 'ISO3166-2-lvl4']

print(f"\nplace_id: {data['place_id']}\n"
      f"osm_type: {data['osm_type']}\n"
      f"lat: {data['lat']}\n"
      f"lon: {data['lon']}\n"
      f"display_name: {data['display_name']}\n"
      f"\nAddress:\n")

for element in elements:
      try:
            place = data['address'][element]
            print(f"{element}: {place}")
      except KeyError:
            print(f"{element}: None")
