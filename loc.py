from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(location):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location_data = geolocator.geocode(location)
        if location_data:
            return (location_data.latitude, location_data.longitude)
        else:
            print(f"Could not get coordinates for {location}")
            return None
    except Exception as e:
        print(f"Error getting coordinates for {location}: {e}")
        return None

def calculate_distance(loc1, loc2):
    try:
        return geodesic(loc1, loc2).kilometers
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return None

# Define locations
rajajinagar = "Rajajinagar, Bangalore"

pg_locations = [
    "PG1, Jayanagar",
    "PG2, Jayanagar, Bangalore",
    "PG3, Jayanagar, Bangalore",
    # Add more PG locations as needed
]

# Get coordinates of Rajajinagar
coord_rajajinagar = get_coordinates(rajajinagar)
if not coord_rajajinagar:
    exit()

# Initialize variables to track the shortest distance and PG
shortest_distance = float('inf')
nearest_pg = None

# Iterate through each PG location in Jayanagar
for pg_location in pg_locations:
    # Get coordinates of the current PG location
    coord_pg = get_coordinates(pg_location)
    if not coord_pg:
        continue
    
    # Calculate distance from Rajajinagar to current PG
    distance = calculate_distance(coord_rajajinagar, coord_pg)
    if distance is not None:
        print(f"Distance from {rajajinagar} to {pg_location}: {distance:.2f} km")
        
        # Update shortest distance and nearest PG if applicable
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_pg = pg_location

# Print the nearest PG and its distance
if nearest_pg:
    print(f"\nThe nearest PG to {rajajinagar} is {nearest_pg} at a distance of {shortest_distance:.2f} km.")
else:
    print(f"\nCould not determine the nearest PG from {rajajinagar}.")
