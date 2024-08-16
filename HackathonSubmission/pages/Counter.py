import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Counter App",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------

# this html code to remove 'X' button from dialog
# -----------------------------------------
st.html(
    '''
        <style>
            div[aria-label="dialog"]>button[aria-label="Close"] {
                display: none;
            }
        </style>
    '''
)
# -----------------------------------------

# creating dialog to display hamster
# -----------------------------------------
@st.dialog("Mr.Hamster")
def hamster(count):
    # creating columns to display image and challenge text
    # -----------------------------------------
    col1, col2 = st.columns([1, 1])
    # -----------------------------------------

    # displaying hamster image
    # -----------------------------------------
    with col1:
        st.image("images\\Mr.Hamster.png", width=200)
    # -----------------------------------------

    # displaying challenge
    # -----------------------------------------
    with col2:
        # if count is 1
        if count == 1:
            st.write("Mr.Hamster has a challenge for you.")
            st.write(":red[Count until the counter reaches 100.]")
        
        # else if count is 100
        elif count == 100:
            st.write("Mr.Hamster has another challenge for you.")
            st.write(":red[Count until the counter reaches 300.]")
        
        # if count is 300
        else:
            st.write(":green[You are such a genius]")
            st.balloons() 
    # -----------------------------------------
# -----------------------------------------


# this function will increase counter by 1
# -----------------------------------------
def increase():
    st.session_state.count += 1 
# -----------------------------------------


# this function will decrease counter by 1
# -----------------------------------------
def decrease():
    st.session_state.count -= 1
# -----------------------------------------


# this function will reset counter to 0
# -----------------------------------------
def reset():
    st.session_state.count = 0
# -----------------------------------------


# creating counter
if 'count' not in st.session_state:
    st.session_state.count = 0

# displaying title
st.markdown("<h1 style='text-align: center; color: #349eeb;'>Counter App</h1>", unsafe_allow_html=True)
st.divider()

# displaying counter
st.markdown(f"<h1 style='text-align: center; color: #White;'>{st.session_state.count}</h1>", unsafe_allow_html=True)

st.divider()
# creating column to place all the buttons in a single line
# ------------------------------------
col1, col2, col3 = st.columns([1, 1, 1])
# ------------------------------------

# creating buttons
# ------------------------------------
with col1: 
    increase_btn = st.button("Increase", on_click=increase)
with col2:
    reset_btn = st.button("Reset", on_click=reset)
with col3:
    decrease_btn = st.button("Decrease", on_click=decrease)
st.divider()
# ------------------------------------

# calling hamster function
if st.session_state.count in [1 , 100, 300]:
    hamster(st.session_state.count)

# -------------------------------THE END------------------------------- #
