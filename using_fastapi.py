from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/location_info/{lat}/{lon}")
def read_item(lat: float, lon: float):

    response = requests.get(url=f'http://localhost:8080/reverse?lat={lat}&lon={lon}&format=json')
    data = response.json()

    final_data = {
        "place_id" : f"{data['place_id']}",
        "osm_type" : f"{data['osm_type']}",
        "lat" : f"{data['lat']}",
        "lon" : f"{data['lon']}",
        "display_name" : f"{data['display_name']}",
    }

    elements = ['shop', 'road', 'neighbourhood', 'suburb', 'county', 'city', 'state', 'state_district', 'country',
                'postcode', 'ISO3166-2-lvl4']

    for element in elements:
          try:
                place = data['address'][element]
                final_data[f"{element}"] = f"{place}"
          except KeyError:
                final_data[f"{element}"] = "None"

    return final_data