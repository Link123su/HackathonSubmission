from random import randint
import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Number🔢 Guessing🤔 Game🎮",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# main function
def main() -> None:
    # displaying title
    # -----------------------------------------
    st.title("Number Guessing Game")
    # -----------------------------------------
    st.divider()

    # specifying range
    # -----------------------------------------
    LOWEST_NUMBER = 1
    HIGHEST_NUMBER = 100
    # -----------------------------------------

    # generating a random number and storing it in cache
    # -----------------------------------------
    @st.cache_data
    def random_number():
        return randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    # -----------------------------------------

    random_number = random_number()  # this variable will store random_number

    # taking user input
    # -----------------------------------------
    guess = st.number_input(f"Guess a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER}.", format="%0f")
    # -----------------------------------------

    # creating display button
    # -----------------------------------------
    guess_btn = st.button(":green[Guess]")
    # -----------------------------------------

    hint = ""  # empty hint cariable

    # validating user guess
    # -----------------------------------------
    if guess_btn:
        # if user guess is not in specified range, it shows a warning
        if guess < LOWEST_NUMBER or guess > HIGHEST_NUMBER:
            st.warning("Guess a number in valid range.")

        # if the guess is greater than correct number, it shows a hint
        elif guess > random_number:
            hint = f"The number is less than {guess}"

        # if the guess is less than correct number, it shows a hint
        elif guess < random_number:
            hint = f"The number is greater than {guess}"

        # if user guess is correct then it displays a congratulatory message  
        else:
            st.balloons()  # displaying balloons
            st.write(f"Yes! Number was {random_number}")
            st.subheader(":green[Congratulation! You Won!]")
    # -----------------------------------------

        # creating container to display cool cat and hint
        # -----------------------------------------
        hint_container = st.container()
        # -----------------------------------------

        # creating columns to display cat image and hint
        # -----------------------------------------
        col1, col2 = hint_container.columns([1, 1])
        # -----------------------------------------
        
        # displaying some info about cool cat
        # -----------------------------------------
        hint_container.write("Mr.Cool Cat will give you hints.")
        # -----------------------------------------

        # displaying cat image
        # -----------------------------------------
        with col1:
            hint_container.image("images\\Mr.Cool Cat.png")
        # -----------------------------------------

        # displaying hint
        # -----------------------------------------
        with col2:
            st.subheader(f":green[{hint}]")
        # -----------------------------------------

    st.divider()

    # adding reset button
    # -----------------------------------------
    reset_btn = st.button(":red[Double click to Reset]")
    # -----------------------------------------

    # clearing cache
    # -----------------------------------------
    if reset_btn:
            st.cache_data.clear()
    # -----------------------------------------

# taking user input
# -----------------------------------------
user_input = st.text_input("Enter what Mr.Cool Cat likes to do: Hint:[Check home page]",
                           placeholder="Answer to Continue")
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if "read" in user_input and "book" in user_input:
    st.success("✔")  # showing success message
    main()  # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
