import streamlit as st
import requests
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://roxannanadim:7eWirSgMl45wOVpW@cluster1.6m028og.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access to MongoDB
db = client.FieldNotes

# Access  MongoDB collection
collection = db.TestEntry
geolocation_collection = db.GeolocationData

    # Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Note", "Map"])

if page == "Note":
    
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
            latitude = st.number_input("Latitude")
            longitude = st.number_input("Longitude")
            
    #set uploaded_file to none
    uploaded_file = None

    # Media Upload
    media_option = st.selectbox("Select Media Type", ["None", "Photo", "Video", "Audio"])
    if media_option != "None":
        uploaded_file = st.file_uploader(f"Upload {media_option}", type=["jpg", "png", "mp4", "wav"])

    # Save Button to database
    if st.button("Save Note"):
        if note_title and note_text:
            # Generate a unique ID based on the current date and time
            note_id = datetime.now().strftime("%Y%m%d%H%M%S")
        # Create a note document
            note = {
                "_id": note_id,
                "title": note_title,
                "content": note_text,
            }

            # Create a geolocation document
            geolocation_data = {
                "_id": note_id,
                "latitude": latitude,
                "longitude": longitude,
            }

            # Check if a media file was uploaded and add it to the note document if needed

            # Insert the note into the 'collection' and the geolocation data into 'geolocation_collection'
            result_note = collection.insert_one(note)
            result_geolocation = geolocation_collection.insert_one(geolocation_data)

            # Check if both inserts were successful
            if result_note.inserted_id and result_geolocation.inserted_id:
                st.success(f"Note and Geolocation data saved with IDs: {result_note.inserted_id}, {result_geolocation.inserted_id}")
            else:
                st.error("Note or Geolocation data could not be saved.")

    # Display uploaded media
    if uploaded_file:
        st.write("Uploaded Media:")
        if media_option == "Photo":
            st.image(uploaded_file)
        elif media_option == "Video":
            st.video(uploaded_file)
        elif media_option == "Audio":
           st.audio(uploaded_file)


elif page == "Map":
    if page == "Map":
        st.title("Map Page")

     

