
import requests

# Function to fetch geolocation using Google Geolocation API
def get_user_location():
    try:
        API_KEY = 'AIzaSyC6DrPvw4hcB-LrFGUAZ48uj83mJXkWeLc'
        GEOLOCATION_API_URL = f'https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}'

        response = requests.post(GEOLOCATION_API_URL)
        data = response.json()

        if 'location' in data:
            latitude = data['location']['lat']
            longitude = data['location']['lng']
            return latitude, longitude
        else:
            st.warning("Location not found.")
            return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Geolocation
if st.checkbox("Include Geolocation"):
    latitude, longitude = get_user_location()
    if latitude is not None and longitude is not None:
        st.markdown(f"Geolocation: Latitude: {latitude}, Longitude: {longitude}")
    else:
        st.markdown("Geolocation: Not Available")
