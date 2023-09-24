import streamlit as st
import requests
import pymongo
from pymongo import MongoClient

#rachels mongodb uri
# mongo_uri = "mongodb+srv://rnd22:<RaeRae13!>@cluster0.nmrig91.mongodb.net/?retryWrites=true&w=majority

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

# Title and description
st.title("Field Biologist Notebook")
st.write("Add notes with geolocation data, photos, videos, and audio.")

# Note input
note_title = st.text_area("Title")
note_text = st.text_area("Enter notes here")


# Initialize uploaded_file to None
uploaded_file = None

# Geolocation
latitude, longitude = get_user_location()
if latitude is not None and longitude is not None:
    st.write(f"Geolocation: Latitude: {latitude}, Longitude: {longitude}")
else:
    st.write("Geolocation: Not Available")
    
if st.checkbox("Manually Enter Geolocation"):
    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")
    
# Media Upload
media_option = st.selectbox("Select Media Type", ["None", "Photo", "Video", "Audio"])
if media_option != "None":
    uploaded_file = st.file_uploader(f"Upload {media_option}", type=["jpg", "png", "mp4", "wav"])

# Save Button
if st.button("Save Note"):
    if uploaded_file is not None:  # Check if uploaded_file is not None before using it
        # Save the note data to your database or storage
        st.success("Note with media saved successfully!")
    else:
        # Handle the case where no media file is uploaded
        st.success("Note without media saved successfully!")

# Display uploaded media
if uploaded_file:
    st.write("Uploaded Media:")
    if media_option == "Photo":
        st.image(uploaded_file)
    elif media_option == "Video":
        st.video(uploaded_file)
    elif media_option == "Audio":
        st.audio(uploaded_file)
