import streamlit as st
import requests
from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://roxannanadim:7eWirSgMl45wOVpW@cluster1.6m028og.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access your MongoDB database (replace 'your_database' with your actual database name)
db = client.FieldNotes

# Access your MongoDB collection (replace 'your_collection' with your actual collection name)
collection = db.TestEntry

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


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
note_title = st.text_area("Note Title")
note_text = st.text_area("Enter notes here")

# Geolocation
if st.checkbox("Include Geolocation"):
    latitude, longitude = get_user_location()
    if latitude is not None and longitude is not None:
        st.write(f"Geolocation: Latitude: {latitude}, Longitude: {longitude}")
    else:
        st.write("Geolocation: Not Available")

uploaded_file = None
# Media Upload
media_option = st.selectbox("Select Media Type", ["None", "Photo", "Video", "Audio"])
if media_option != "None":
    uploaded_file = st.file_uploader(f"Upload {media_option}", type=["jpg", "png", "mp4", "wav"])

# Save Button
# Save the note data to your database or storage
if st.button("Save Note"):
    if note_title and note_text:

        # Generate a unique ID based on the current date and time
        note_id = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create a note doc from user input
        note = {
            "_id": note_id,  # Use the generated ID as the document's ID
            "title": note_title,
            "content": note_text,
            "latitude": latitude,  # Separate key for latitude
            "longitude": longitude,  # Separate key for longitude
        }

        # Insert into MongoDB
        result = collection.insert_one(note)

        if result.inserted_id:
            st.success(f"Note saved with ID: {result.inserted_id}")
        else:
            st.error("Note could not be saved.")
    else:
        st.warning("Please provide a title and content for the note.")


# Display uploaded media
if uploaded_file:
    st.write("Uploaded Media:")
    if media_option == "Photo":
        st.image(uploaded_file)
    elif media_option == "Video":
        st.video(uploaded_file)
    elif media_option == "Audio":
       st.audio(uploaded_file)


