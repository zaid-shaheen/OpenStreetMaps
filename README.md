# OpenStreetMaps
### To run Nominatim locally on your Linux device follow these steps:

## Install Docker:
To install Docker go to <a href="https://docs.docker.com/desktop/setup/install/linux/">How to install Docker on Linux</a>.

## Automatic import
Run this command to download the required data, initialize the database, and start Nominatim:
```
docker run -it \
  -e PBF_URL=http://download.geofabrik.de/asia/jordan-latest.osm.pbf \
  -e REPLICATION_URL=https://download.geofabrik.de/asia/jordan-updates \
  -p 8080:8080 \
  --name nominatim \
  mediagis/nominatim:4.3
```
Port 8080 is the nominatim HTTP API port and 5432 is the Postgres port, which you may or may not want to expose.

If you want to check that your data import was successful, you can use the API with the following URL: <br> http://localhost:8080/search?q=amman

## Configuration:
### General Parameters
- `PBF_URL`: Which is OpenStreetMap (OSM) data extracts, the data is downloaded during initialization, imported, and removed from disk afterward, the data extracts can be freely downloaded from <a href="https://download.geofabrik.de/">Geofabrik's<a> server. It cannot be used together with `PBF_Path`.

- `PBF_Path`: Which OSM extract to import from the .pbf file inside the container. It cannot be used together with `PBF_URL`.

- `REPLICATION_URL`: Where to get updates from, for example, Geofabrik's update for Jordan extract is available at `https://download.geofabrik.de/asia/jordan-updates`, other places at Geofabrik follow the pattern `https://download.geofabrik.de/<CONTENENT>/<COUNTRY-updates>/`.

## How to use the API:
The two main endpoints used in OpenStreetMap Nominatim are: `/search` for turning addresses into geographic coordinates (geocoding), and `/reverse` for the opposite process (reverse geocoding).

## OpenStreetMap geocoding example
To convert an address into latitude and longitude in OSM Nominatim:

Endpoint `GET`: `https://nominatim.openstreetmap.org/search?q={address_string}&format={output_format}`.

- `{address_string}` is the address you are trying to geocode. Try to include as much information as possible, including the country, city, and postal code.

- `{output_format}` determines the structure of the response and must be one of `xml`, `json`, `jsonv2`, `geojson`, `geocodejson`, the default being `jsonv2`.


#### Next, we'll attempt to geocode the location of Amman, Khalda Circle:

Method `GET`: https://nominatim.openstreetmap.org/search?q=amman+khalda+circle&format=jsonv2

Output:
```
[
  {  
    "place_id": 41838022,
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
    "osm_type": "way",
    "osm_id": 149867780,
    "lat": "31.994694000000003",
    "lon": "35.83034305615034",
    "category": "highway",
    "type": "tertiary",
    "place_rank": 26,
    "importance": 0.0534043373769741,
    "addresstype": "road",
    "name": "Khalda Circle",
    "display_name": "Khalda Circle, Sweileh, Al-Jami'ah Sub-District, Al-Jami'ah District, Amman, 11831, Jordan",
    "boundingbox": [
    "31.9944556",
    "31.9949343",
    "35.8300606",
    "35.8306252"
    ]
  }
]
```

#### To geocoding using our local server use: <br>
Method `GET`: http://localhost:8080/search?q=amman+khalda+circle&format=jsonv2 . The output will be the same.

## OpenStreetMap reverse geocoding example

Let's try the same thing but backward, and reverse geocode the coordinates `"lat": "31.994694000000003"`, `"lon": "35.83034305615034"` that were returned in the earlier example.

Endpoint `GET`: `https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format={output_format}`

- `{lat}` and `{lon}` are the latitude and longitude of the point you are trying to reverse geocode.

- `{output_format}` determines the structure of the response and must be one of `xml`, `json`, `jsonv2`, `geojson`, `geocodejson`, the default being `jsonv2`.

Method `GET`: https://nominatim.openstreetmap.org/reverse?lat=31.994694000000003&lon=35.83034305615034&format=jsonv2

Output:
```
{
  "place_id": 41705088,
  "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
  "osm_type": "way",
  "osm_id": 684673568,
  "lat": "31.9946938",
  "lon": "35.8303421",
  "category": "man_made",
  "type": "tunnel",
  "place_rank": 30,
  "importance": 0.0000710040436407571,
  "addresstype": "man_made",
  "name": "Khalda Tunnel",
  "display_name": "Khalda Tunnel, Wasfi Al-Tall Street, Sweileh, Al-Jami'ah Sub-District, Al-Jami'ah District, Amman, 11831, Jordan",
  "address": {
  "man_made": "Khalda Tunnel",
  "road": "Wasfi Al-Tall Street",
  "district": "Sweileh",
  "county": "Al-Jami'ah Sub-District",
  "state_district": "Al-Jami'ah District",
  "state": "Amman",
  "ISO3166-2-lvl4": "JO-AM",
  "postcode": "11831",
  "country": "Jordan",
  "country_code": "jo"
  },
  "boundingbox": [
  "31.9942429",
  "31.9951447",
  "35.8302314",
  "35.8304528"
  ]
}
```
#### To reverse geocoding using our local server use: <br>
Method `GET`: http://localhost:8080/reverse?lat=31.994694000000003&lon=35.83034305615034&format=jsonv2 . The output will be the same.

> [!NOTE]
> If you want to know more about medigis and nominatim docker read this <a href="https://github.com/mediagis/nominatim-docker/tree/master/4.3?ref=blog.afi.io">documentation</a>.
