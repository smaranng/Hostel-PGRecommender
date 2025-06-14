import streamlit as st
from geopy.geocoders import Nominatim
import requests

# Function to get coordinates from an address
def get_coordinates(address):
    geolocator = Nominatim(user_agent="pg_hostel_locator")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Function to fetch nearby places using Google Places API
def fetch_nearby_places(lat, lon, radius=1000):
    api_key = "667d7d630e85e294595271fvpc2e31b"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius={radius}&type=lodging&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        return results
    else:
        return []

# Function to recommend the best place based on rating
def recommend_best_place(places):
    if not places:
        return None
    places.sort(key=lambda x: x.get('rating', 0), reverse=True)
    return places[0]

# Streamlit application
st.title("Find Nearby PGs and Hostels")

# Use a unique key for each widget to avoid DuplicateWidgetID error
address = st.text_input("Enter location", key="address_input")
if st.button("Search", key="search_button"):
    lat, lon = get_coordinates(address)
    if lat is not None and lon is not None:
        places = fetch_nearby_places(lat, lon)
        best_place = recommend_best_place(places)
        if best_place:
            st.write("Best Place Found:")
            st.write(f"Name: {best_place.get('name')}")
            st.write(f"Rating: {best_place.get('rating')}")
            st.write(f"Address: {best_place.get('vicinity')}")
        else:
            st.write("No places found.")
    else:
        st.write("Invalid address entered.")
