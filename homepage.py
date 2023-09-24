import streamlit as st

st.set_page_config(
    page_title="Field Biologist Notebook",
    page_icon="🌿",
)

# Professional app description
st.write("# Welcome to FieldTracker!")

# Display the logo using st.image()
# Display the logo as an icon
logo_url = "https://i.ibb.co/yFRGCQk/Screenshot-2023-09-23-at-5-52-17-PM-removebg-preview.png"
st.markdown(f'<a href="{logo_url}" target="_blank"><img src="{logo_url}" width="100" height="100"></a>', unsafe_allow_html=True)




st.sidebar.success("Select a feature to demo.")

st.markdown(
    """
    FieldTracker is your trusted digital companion for scientific exploration and documentation!

    ### Discover what our app offers:
    🗺️ **Map your observations.** Utilize our geolocation functionality to augment your notes with precise location data.

    📸 **Immortalize the essence of nature.** Seamlessly capture and attach photos to your notes, transforming each entry into a comprehensive visual dossier, perfect for scientific study.
   
    📽️ **Unleash your inner documentarian.** Record videos effortlessly to chronicle the intricate movements of wildlife and the intricacies of natural phenomena, presenting a clear picture of your observations.
   
    🔊 **Listen to sounds of nature.** Record audio notes to preserve the symphonies of the wilderness – the rustling of leaves, the calls of birds – in professional clarity.

    🌟 With a simple click, securely store your notes and media within our digital ecosystem using **MongoDB**.

    🌍 Embark on an exciting journey of scientific exploration and contribute to the ever-expanding body of knowledge about our natural world.

    ### Want to learn more?
    - Visit [our website](https://fieldbiologistnotebook.com)
    - Explore our [user documentation](https://docs.fieldbiologistnotebook.com)
    - Join our [community forum](https://community.fieldbiologistnotebook.com)

    ### For advanced users:
    - Analyze large datasets with our powerful data processing capabilities.
    - Collaborate with fellow scientists in real-time through our integrated collaboration tools.
    - Conduct in-depth statistical analyses and generate insightful visualizations.
    """
)

# Set custom CSS styles
custom_css = """
<style>
    /* Change the background color of the sidebar */
    .sidebar {
        background-color: #333;
        color: white;
    }

    /* Change the background color of the main content area */
    .main {
        background-color: #364156;
    }

    /* Change the font size and color of the title */
    .css-1vcd91e {
        font-size: 24px;
        color: #333;
    }

    /* Change the font size and color of text in the main content area */
    .css-1f6dbht {
        font-size: 16px;
        color: #333;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
