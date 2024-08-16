import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="MasterMind Game🎮",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------

st.divider()
# displaying title
# -----------------------------------------
st.markdown("<h1 style='text-align: center; color: #349eeb;'>MasterMind Game</h1>", unsafe_allow_html=True)
# -----------------------------------------
st.divider()

# displaying note
# -----------------------------------------
st.subheader("You have you download this app to use.")
# -----------------------------------------

# reading file and displaying download button
# -----------------------------------------
with open("pages\\MasterMindGame.zip", "rb") as f:
    st.download_button("Download App", f, file_name="MasterMindGame.zip")
# -----------------------------------------

# displaying note
# -----------------------------------------
st.write("Note: App will be located in dist folder.\nApp will take some time to open.")
# -----------------------------------------

# -------------------------------THE END------------------------------- #
