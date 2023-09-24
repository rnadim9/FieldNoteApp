import streamlit as st
import pymongo
import folium

# RMongoDB connection URI
client = pymongo.MongoClient("mongodb+srv://roxannanadim:7eWirSgMl45wOVpW@cluster1.6m028og.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

# Access MongoDB database
db = client.FieldNotes

# Access MongoDB collection
collection = db.TestEntry

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create a Streamlit page for displaying the map
st.title("Media Locations on Map")

# Fetch geolocation data and media file references from MongoDB

geolocation_data = [collection]  # List of dictionaries with 'latitude', 'longitude', and 'media_file' keys

# Create a map using Folium
m = folium.Map(location=[0, 0], zoom_start=2)  # Adjust the initial map location and zoom level

# Add markers for each geolocation point
for data in geolocation_data:
    latitude = data["latitude"]
    longitude = data["longitude"]
    media_file = data["media_file"]

    # Create a custom HTML popup for the marker
    popup_html = f"<a href='{media_file}' target='_blank'>View Media</a>"

    folium.Marker(
        [latitude, longitude],
        tooltip="Click for Details",
        popup=folium.IFrame(html=popup_html, width=300, height=100),
    ).add_to(m)

# Display the map
st.write(m)
i

# Display a map centered at a specific location
st.map((latitude, longitude), zoom=12)

