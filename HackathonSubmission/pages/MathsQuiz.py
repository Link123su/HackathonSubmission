import streamlit as st
from random import randint, choice

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Maths➗ Quiz",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------

# main function
# -----------------------------------------
def main():

    # function to display gorilla dialog
    # -----------------------------------------
    @st.dialog("Mr.Gorilla is giving you chocolate")
    def gorilla() -> None:
        # creating columns to place image and button
        # -----------------------------------------
        col5, col6 = st.columns([1, 1])
        # -----------------------------------------

        # displaying image
        # -----------------------------------------
        with col5:
            st.image("images\\gorilla_giving_chocolate.png")
        # -----------------------------------------

        # displaying button
        # -----------------------------------------
        with col6:
            take_btn = st.button(":green[Take Chocolate🍫]")
        # -----------------------------------------

            # if take button is clicked
            # -----------------------------------------
            if take_btn:
                st.rerun()  # closing dialog
             # -----------------------------------------
    # -----------------------------------------


    # this function returns a random question
    # -----------------------------------------
    def random_question() -> str:
        x = randint(1, 100)  # this generates a random number between 1 and 100
        y = randint(1 , 10)  # this generates a random number between 1 and 10

        # list of valid operators
        # -----------------------------------------
        operator = choice(["*", "+", "-"])
        # -----------------------------------------

        # question
        # -----------------------------------------
        qn = f"{x} {operator} {y}"
        # -----------------------------------------
                
        return qn  # returning question 
    # -----------------------------------------


    # this function will check and display results
    def check(user_ans, container) -> None:
        
        # if user enters correct answer
        # -----------------------------------------
        if user_ans == eval(st.session_state.question):
            st.balloons()  # displaying balloons🎈
            container.subheader("Result: :green[Correct Answer]")  # displaying result
            gorilla()  # calling gorilla function
        # -----------------------------------------

        # else
        # -----------------------------------------
        else:
            container.subheader("Result: :red[Wrong Answer]")  # displaying result
        # -----------------------------------------


    # generating random question and storing in session
    if "question" not in st.session_state:
        st.session_state.question = random_question()

    st.divider()
    # displaying title
    # -----------------------------------------
    st.markdown("<h1 style='text-align: center; color: #349eeb;'>Maths Quiz</h1>", unsafe_allow_html=True)
    # -----------------------------------------
    st.divider()

    # displaying question
    # -----------------------------------------
    st.subheader(f"Question: :red[{st.session_state.question}]")
    # -----------------------------------------

    st.divider()

    # taking user input
    # -----------------------------------------
    user_input = st.number_input("Enter your answer: ", format="%0f")
    # -----------------------------------------

    st.divider()

    # creating columns to display buttons
    # -----------------------------------------
    col1, col2 = st.columns([1, 1])
    # -----------------------------------------

    # creating check button
    # -----------------------------------------
    with col1:
        check_button = st.button(":green[Check Answer]")
    # -----------------------------------------

    # creating reset button
    # -----------------------------------------
    with col2:
        reset_button = st.button(":blue[Next Question]")
    # -----------------------------------------

    st.divider()

    # creating empty container
    # -----------------------------------------
    result_container = st.container().empty()
    # -----------------------------------------

    # result will be displayed here
    # -----------------------------------------
    result_container.subheader(f"Result: ")
    # -----------------------------------------

    st.divider()

    # if checked button is clicked
    # -----------------------------------------
    if check_button:
        check(user_input, result_container)  # calling check function
    # -----------------------------------------

    # if reset button is clicked
    # -----------------------------------------
    if reset_button:
        st.session_state.question = random_question()  # changing question
    # -----------------------------------------

    # creating columns to display image and text
    # -----------------------------------------
    col3, col4 = st.columns([1, 1])
    # -----------------------------------------

    # displaying gorilla image
    # -----------------------------------------
    with col3:
        st.image("images\\Mr.Gorilla.png")
    # -----------------------------------------

    # displaying gorilla's message
    # -----------------------------------------
    with col4:
        st.subheader(":blue[Hey! I'm Mr.Gorilla. I'm here to check your answers and give you new question.]")
        st.subheader(":blue[I'll give you chocolate🍫, if your answer is correct]")
    # -----------------------------------------
# -----------------------------------------


# taking user_input
# -----------------------------------------
user_input = st.text_input("Enter the full form of Maths/Math to Continue").lower()
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if user_input == "mathematics":
    main()  # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
