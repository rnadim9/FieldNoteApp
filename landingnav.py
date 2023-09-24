import streamlit as st

# Landing page content
st.title("Welcome to the Field Biologist Notebook")
st.write("This is the landing page for your app.")

# Add a link to the note entry page
if st.button("Enter New Note"):
    st.session_state.page = "note_entry"

# Note entry page content
if "page" in st.session_state and st.session_state.page == "note_entry":
    # Your existing note entry page code goes here
    # ...

    # You can include a button to return to the landing page if needed
    if st.button("Back to Landing Page"):
        st.session_state.page = "landing"
