import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="ToDo App",
    page_icon="✅",
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
st.markdown("<h1 style='text-align: center; color: #349eeb;'>ToDo App</h1>", unsafe_allow_html=True)
# -----------------------------------------
st.divider()

# displaying note
# -----------------------------------------
st.subheader("You have you download this app to use.")
# -----------------------------------------

# reading zip file and displaying download button
# -----------------------------------------
with open("pages\\ToDoApp.zip", "rb") as f:
    st.download_button("Download App", f, file_name="ToDoApp.zip")
# -----------------------------------------

# displaying note
# -----------------------------------------
st.write("Note: App will be located in dist folder.\nApp will take some time to open.")
# -----------------------------------------

# -------------------------------THE END------------------------------- #
