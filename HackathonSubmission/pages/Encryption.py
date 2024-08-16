from random import choice
from string import ascii_letters, digits, punctuation 
import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Text Encryptor",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# main function
# -----------------------------------------
def main():

    # this function will decrypt the given text
    # -----------------------------------------
    def decrypt(msg) -> str:
        decrypted = ""  # decrpyted message will be stored here
        word_list = []  # empty word list

        for i in msg.split(" "):  # looping through every word
            i = i[3:-3]  # slicing word
            word_list.append(f"{i[::-1]} ")  # appending sliced word to word list

        return decrypted.join(word_list)  # converting list to string and returning it
    # -----------------------------------------


    # this function will encrypt the given text
    # -----------------------------------------
    def encrypt(msg) -> str:
        encrypted = ""  # encrpyted message will be stored here
        word_list = []  # empty word list

        for i in msg.split(" "):  # looping through every word
            # generating random letters
            # -----------------------------------------
            a = choice(random_list) + choice(random_list) + choice(random_list)
            b = choice(random_list) + choice(random_list) + choice(random_list)
            # -----------------------------------------
            i = a + i[::-1] + b  # appending generated letters
            word_list.append(f"{i} ")  # appending word to list

        return encrypted.join(word_list)  # converting encrypted list to string and returning it
    # -----------------------------------------

    # this list contains letters, numbers and punctuations
    # -----------------------------------------
    random_list = [*ascii_letters, *digits, *punctuation]
    # -----------------------------------------

    st.divider()
    # displaying title
    # -----------------------------------------
    st.markdown("<h1 style='text-align: center; color: #349eeb;'>Message Encryptor🔐</h1>", unsafe_allow_html=True)
    # -----------------------------------------
    st.divider()

    # taking user input
    # -----------------------------------------
    text = st.text_area("Enter text:")
    # -----------------------------------------

    # displaying options
    # -----------------------------------------
    option = st.radio(
        "Select: ",
        ["**Encrypt**", "**Decrypt**"]
    )
    # -----------------------------------------

    # displaying encrypt and decrypt buttons
    # -----------------------------------------
    button = st.button(f":green{option}")
    # -----------------------------------------

    result = ""  # empty result string

    # if button is clicked
    # -----------------------------------------
    if button:
        # if text is not none
        if not text == "":
            match option:
                case "**Encrypt**":
                    result = encrypt(text)  # storing encrypted text in result variable

                case "**Decrypt**":
                    result = decrypt(text)  # storing decrypted text in result variable
    # -----------------------------------------

    # displaying result
    # -----------------------------------------
    st.text_area("Result: ", result)
    # -----------------------------------------
# -----------------------------------------

# taking user_input
# -----------------------------------------
user_input = st.text_input("Who made this website?", placeholder="Answer to continue").lower()
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if "pythonic" in user_input and "mind" in user_input:
    st.success("Correct!")  # displaying success msg
    main()  # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
