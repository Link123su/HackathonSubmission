import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page settings
# -----------------------------------------
st.set_page_config(
    page_title="About",
    page_icon="About",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------

# some text
# -----------------------------------------
st.subheader(":green[This website is my submission for the 'Coding with Lewis' Hackathon]")
# -----------------------------------------

st.divider()

# button to subscribe '@CodingWithLewis'
# -----------------------------------------
st.page_link("https://www.youtube.com/@CodingWithLewis", label=":red[Subscribe To Coding With Lewis]")
# -----------------------------------------
st.divider()

# buttons to subscribe and follow '@PythonicMind'
# -----------------------------------------
st.page_link("https://www.youtube.com/@PythonicMind2", label=":red[Subscribe To My Channel]")
st.page_link("https://www.instagram.com/pythonicmind/", label=":rainbow[Follow me on Instagram]")
# -----------------------------------------
st.divider()

# -------------------------------THE END------------------------------- #
