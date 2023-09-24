import streamlit as st

st.title("Geolocation Example")

# JavaScript code to access the Geolocation API
geolocation_code = """
<script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        document.getElementById("location").innerHTML = "Latitude: " + latitude + "<br>Longitude: " + longitude;
    }

    // Call the getLocation function when the page loads
    getLocation();
</script>
"""

# Use Streamlit's components to embed HTML with JavaScript
st.components.v1.html(geolocation_code)

# Display the location information
st.markdown("<div id='location'>Location: Loading...</div>", unsafe_allow_html=True)
print("hello world")
