import requests
import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Quotes✒ Generator",
    page_icon="✒",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# generating random quote and storing in cache
# -----------------------------------------
@st.cache_data
def generate_quote() -> str:
    # getting quote from api
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        return quote, author  # returning quote and author

    else:
        return 'Failed to fetch a quote', "n"  # returning this msg if failed to generate quote
# -----------------------------------------


st.divider()
# displaying title
# -----------------------------------------
st.markdown("<h1 style='text-align: center; color: #349eeb;'>Random Quote Generator</h1>", unsafe_allow_html=True)
# -----------------------------------------
st.divider()

# storing data in variable
# -----------------------------------------
quote, author = generate_quote()
# -----------------------------------------

# displaying quote and author
# -----------------------------------------
st.subheader(f"Quote: :green[{quote}]")
st.subheader(f"Author: :red[{author}]")
# -----------------------------------------

st.divider()

# creating generate btn
# -----------------------------------------
generate_btn = st.button(":green[Generate]")
# -----------------------------------------

# if generate butto is clicked
# -----------------------------------------
if generate_btn:
    st.cache_data.clear()  # clearing cache
# -----------------------------------------

st.divider()

# creating columns to display smart cat image and text
# -----------------------------------------
col1, col2 = st.columns([1, 1])
# -----------------------------------------

# displaying image
# -----------------------------------------
with col1:
    st.image("images\\Mr.Smart Cat.png")
# -----------------------------------------

# displaying cat's msg
# ----------------------------------------- 
with col2:
    st.subheader(":blue[Meow! Mr.Smart Cat has found a quote for you. Did you like it?]")
    yes_button = st.button(":rainbow[Yes!]")

    if yes_button:
        st.balloons()
# -----------------------------------------

# -------------------------------THE END------------------------------- #
