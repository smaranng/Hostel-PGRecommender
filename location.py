import requests
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text
import math

app = Flask(__name__)

# Database configuration
db_uri = 'mysql+mysqldb://root:@127.0.0.1/pghms'
engine = create_engine(db_uri)

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    location = data.get('location')
    
    # Use Nominatim API to get latitude and longitude of the location
    nominatim_url = f'https://nominatim.openstreetmap.org/search?format=json&q={location}'
    headers = {
        'User-Agent': 'HostelFinderApp/1.0 (contact@example.com)'
    }
    response = requests.get(nominatim_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error contacting geocoding service: {response.status_code} - {response.text}")
        return jsonify({'error': 'Error contacting geocoding service'}), 500
    
    try:
        geocode_data = response.json()
    except ValueError:
        print(f"Error decoding geocoding service response: {response.text}")
        return jsonify({'error': 'Error decoding geocoding service response'}), 500
    
    if not geocode_data:
        return jsonify({'error': 'Location not found'})
    
    destination_lat = float(geocode_data[0]['lat'])
    destination_lon = float(geocode_data[0]['lon'])
    
    print(f"Searching for hostels near lat: {destination_lat}, lon: {destination_lon}")
    
    # SQL query to fetch hostels from the database
    sql_query = """
    SELECT id, name, lat, lon, location, image_url, map_embed_url
    FROM hostels
    """
    with engine.connect() as connection:
        result = connection.execute(text(sql_query))
        hostels = []
        for row in result:
            hostel = {
                'id': row['id'],
                'name': row['name'],
                'latitude': row['lat'],
                'longitude': row['lon'],
                'location': row['location'],
                'image_url': row['image_url'],
                'map_embed_url': row['map_embed_url'],
                'distance': haversine(destination_lon, destination_lat, float(row['lon']), float(row['lat']))
            }
            hostels.append(hostel)
            print(f"Hostel found: {hostel}")
    
    # Sort hostels by distance from the destination
    filtered_hostels = sorted(hostels, key=lambda x: x['distance'])
    
    # Filter hostels that are within a certain radius, for example, 20 km
    filtered_hostels = [hostel for hostel in filtered_hostels if hostel['distance'] <= 20]

    return jsonify({'hostels': filtered_hostels, 'destination': {'lat': destination_lat, 'lon': destination_lon}})

if __name__ == '__main__':
    app.run(debug=True)