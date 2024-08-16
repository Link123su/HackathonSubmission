from random import choice, shuffle
import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Word🔠 Guessing🤔 Game🎮",
    page_icon="🔠",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# this function will display sparrow dialog
# -----------------------------------------
@st.dialog("Mr.Sparrow")
def sparrow(option) -> None:
    # creating columns to display sparrow image and text
    # -----------------------------------------
    col4, col5 = st.columns([1, 1])
    # -----------------------------------------

    # displaying sparrow image
    # -----------------------------------------
    with col4:
        st.image("images\\Mr.Sparrow.png")
    # -----------------------------------------

    # displaying results
    # -----------------------------------------
    with col5:
        match option:
            case "check":
                # if user guessed correct word
                # -----------------------------------------
                if user_input == st.session_state.word:
                    st.balloons()  # displaying balloons
                    st.subheader(":green[You guessed it!]")  # displaying success msg
                    st.success("Correct Guess!")
                # -----------------------------------------

                # else displaying error msg
                # -----------------------------------------
                else:
                    st.subheader(":red[Wrong Guess]")
                    st.error("Wrong Guess")
                # -----------------------------------------

            # displaying correct word 
            case "show":
                st.subheader(f"The correct word is: :green[{st.session_state.word}]")
    # -----------------------------------------
# -----------------------------------------

# word list
# -----------------------------------------
word_list = ["relate", "endorse", "root", "wave", "moral", "sentiment", "payment", "faithful", "foster", "direction",
             "coma", "crowd", "piano", "receipt", "inspiration", "shoot", "porter", "pound", "boat", "specimen", "chart",
             "communication", "disorder", "means", "obscure", "cassette", "perfect", "contraction", "computing", "cave",
             "steward", "chorus", "publication", "gloom", "marine", "groan", "know", "grace", "wake", "summer",
             "interference","site", "plain", "dip", "finished", "flow", "average", "child"]
# -----------------------------------------

# storing generated random word in sessions
# -----------------------------------------
if 'word' not in st.session_state:
    st.session_state.word = choice(word_list)  # choosing a random word
    letters = [letter for letter in st.session_state.word]  # list containing letters of word
    shuffle(letters)  # shuffle above list
    st.session_state.letters = letters  # storing shuffled letters list
# -----------------------------------------

st.divider()
# displaying title
# -----------------------------------------
st.markdown("<h1 style='text-align: center; color: #349eeb;'>Guess the Word Game</h1>", unsafe_allow_html=True)
# -----------------------------------------
st.divider()

# displaying letters
# -----------------------------------------
st.subheader(f"Letters: :green[{"".join(st.session_state.letters).replace("", " ")}]")
# -----------------------------------------

st.divider()

# taking user input
# -----------------------------------------
user_input = st.text_input("Guess the word: ")
# -----------------------------------------

st.divider()

# creatinf columns
# -----------------------------------------
col1, col2, col3 = st.columns([1, 1, 1])
# -----------------------------------------

# displaying check button
# -----------------------------------------
with col1:
    check_btn = st.button(":green[Check]", on_click=lambda: sparrow("check"))
# -----------------------------------------

# displaying reset button
# -----------------------------------------
with col2:
    reset_btn = st.button(":blue[Next Word]")
# -----------------------------------------

# displaying show button
# -----------------------------------------
with col3:
    show_btn =st.button(":red[Show Word]", on_click=lambda: sparrow("show"))
# -----------------------------------------

st.divider()

# if reset button clicked
# -----------------------------------------
if reset_btn:
    st.session_state.word = choice(word_list)
    letters = [letter for letter in st.session_state.word]
    shuffle(letters)
    st.session_state.letters = letters
# -----------------------------------------

# displaying note
# -----------------------------------------
st.write("Sometimes Mr.Sparrow changes the word while you are guessing. :)")
# sparrow is very funny, right?
# -----------------------------------------

# -------------------------------THE END------------------------------- #
