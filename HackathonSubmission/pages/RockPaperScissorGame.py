import streamlit as st
from random import choice

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Rock👊 Paper📃 Scissor✂ Game🎮",
    page_icon="👊📃✂",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# This function checks the result
def check_result(user_choice, computer_choice) -> str:

    if user_choice == computer_choice:
        return "It's a Tie!"
    
    elif user_choice == "Rock":
        match computer_choice:
            case "Paper":
                st.session_state.computer_score += 1
                return ":red[Computer Won!]"
            
            case "Scissor":
                # display balloons
                st.balloons()
                st.session_state.user_score += 1
                return ":green[You Won!]"

    elif user_choice == "Paper":
        match computer_choice:
            case "Scissor":
                st.session_state.computer_score += 1
                return ":red[Computer Won!]"
            
            case "Rock":
                # display balloons
                st.balloons()
                st.session_state.user_score += 1
                return ":green[You Won!]"
            
    else:
        match computer_choice:
            case "Rock":
                st.session_state.computer_score += 1
                return ":red[Computer Won!]"
            
            case "Paper":
                # display balloons
                st.balloons()
                st.session_state.user_score += 1
                return ":green[You Won!]"


if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# This list contains all valid options
# ------------------------------------
options_list = ["Rock", "Paper", "Scissor"]
# ------------------------------------

# Adding title
# ------------------------------------
st.title("Rock👊 Paper📃 Scissor✂ Game")
st.divider()
# ------------------------------------

# creating column to place all the buttons in a single line
# ------------------------------------
col1, col2, col3 = st.columns([1, 1, 1])
# ------------------------------------

# creating buttons
# ------------------------------------
with col1: 
    rock_btn = st.button("Rock", type="primary")
with col2:
    paper_btn = st.button("Paper", type="primary")
with col3:
    scissor_btn = st.button("Scissor", type="primary")
# ------------------------------------

# creating variables to display results
# ------------------------------------
result_txt = "Result: "
user_choice_txt = "You: "
computer_choice_txt = "Computer: "
# ------------------------------------

# if buttons are clicked
# ------------------------------------
if rock_btn:
    # randomly choosing an option for option_list
    computer = choice(options_list)

    # updating variables to display result
    user_choice_txt += "Rock"
    computer_choice_txt += computer
    result = check_result("Rock", computer)
    result_txt += str(result)

if paper_btn:
    # randomly choosing an option for option_list
    computer = choice(options_list)

    # updating variables to display result
    user_choice_txt += "Paper"
    computer_choice_txt += computer
    result = check_result("Paper", computer)
    result_txt += str(result)

if scissor_btn:
    # randomly choosing an option for option_list
    computer = choice(options_list)

    # updating variables to display result
    user_choice_txt += "Scissor"
    computer_choice_txt += computer
    result = check_result("Scissor", computer)
    result_txt += str(result)
# ------------------------------------
# divider
st.divider()

# displaying result and choices of user and computer
# ------------------------------------
st.subheader(result_txt)
st.subheader(f":orange[{user_choice_txt}]")
st.subheader(f":orange[{computer_choice_txt}]")
st.subheader(f"Your Score: :blue[{st.session_state.user_score}]")
st.subheader(f"Computer Score: :blue[{st.session_state.computer_score}]")
# ------------------------------------

# -------------------------------THE END------------------------------- #
