from string import ascii_letters, digits, punctuation
from random import choice, shuffle
import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Password🗝 Generator",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------


# main function
def main() -> None :
    # this function will generate password
    # -----------------------------------------
    def generate_password(min_length, has_numbers, has_specials):
        letters = ascii_letters  # this contains all ascii uppercase and lowercase letters
        numbers = digits  # this contain all digits from 0 to 9
        specials = punctuation  # this contain punctuation

        # creating a empty password variable
        password = ""

        # it will continue to run as long as length of the password is less than or equal to min_length
        while len(password) <= min_length:
            # appending a random letter to our password string
            password += choice(letters)

            # it will append a random digit to password string if has_numbers is true
            if has_numbers:
                password += choice(numbers)

            # it will append a random punctuation to password string if has_specials is true
            if has_specials:
                password += choice(specials)

        # converting password string to variable to shuffle it
        password = list(password)
        shuffle(password)

        # converting password back to string and returning it
        return "".join(password)
    # -----------------------------------------


    # adding title
    # -----------------------------------------
    st.title("Password Generator🔐")
    # -----------------------------------------
    st.divider()

    # taking user_input
    # -----------------------------------------
    pwd_length = st.number_input("Enter Length of The Password: ", format="%0f")
    # -----------------------------------------

    # adding checkboxes
    # -----------------------------------------
    contain_number = st.checkbox("Want Numbers in your password?")
    contain_specials = st.checkbox("Want special character in your password?")
    # -----------------------------------------

    # adding generate button
    # -----------------------------------------
    generate_btn = st.button(":green[Generate Password]")
    # -----------------------------------------

    # it will execute when generate button is clicked
    # -----------------------------------------
    if generate_btn:
        # this function will dispaly rabbit dialog
        @st.dialog("Mr.Rabbit has generated a password for you.")
        def check():
            # display rabbit image
            # -----------------------------------------
            st.image("images\\Mr.Rabbit.png")
            # -----------------------------------------

            # validating length of the password
            # ----------------------------------------- 
            if 3 < pwd_length <= 100:
                # generating password and storing it in a variable
                generated_pwd = generate_password(pwd_length, contain_number, contain_specials)
                # displaying generated password
                st.subheader(":blue[Generated Password is:]")
                st.code(f"{generated_pwd}")
                st.success("✔")
            else:
                # showing warning if the pwd_length is too short or too long
                st.warning("The length of password must be greater than 3\nand less than or equal to 100")
            # -----------------------------------------

        check()  # calling check function
    st.divider()
    # -----------------------------------------


# taking user input
# -----------------------------------------
user_input = st.text_input("Enter what Mr.Rabbit likes to eat. Hint: check home page.").lower()
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if "avocado" in user_input:
    st.success("Correct!")  # displaying success msg
    main() # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
