import folium
from geopy.geocoders import Nominatim
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
map_url = 'http://127.0.0.1:5500/views/map.html'

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
@app.get('/search')
def search_country(country: str): 
    geolocator = Nominatim(user_agent="geo-map")
    location = geolocator.geocode(country)
    if location: 
        lat = location.latitude
        longitude = location.longitude 
        clcoding = folium.Map(location=[lat, longitude], zoom_start=25, font_size=10)

        # Title of map
        marker = folium.Marker([lat, longitude], popup=country)
        marker.add_to(clcoding)

        with open('views/map.html', 'w') as f: 
            f.write(clcoding._repr_html_())
        
        return {
            'code': 200, 
            'status': 'success'
        }
    else: 
        return {
            'code': 404, 
            'status': 'fail'
        }
