import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page settings
# -----------------------------------------
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🐈",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# displaying logo
# -----------------------------------------
st.logo("images\\logo.jpg")
# -----------------------------------------


# main function
def main() -> None:
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


    # this dialog will display cat
    # -----------------------------------------
    @st.dialog("Meet Mr.Cat😸")
    def cat(user_status) -> None:
        # cat's 🐈 requests :)
        # -----------------------------------------

        underweight_msg: str = f"""Meow! I'm Mr.Cat. I'm Underweight just like you.
                                   Can you give me some advice to gain weight?"""

        normal_msg: str = """Meow! I'm Mr.Cat. My BMI Status is Normal just like you.
                             Give me some advice to stay healthy."""

        overweight_msg: str = f"""Meow! I'm Mr.Cat. I'm {user_status} like you.
                              Can you give me some advice to loose weight and stay healthy?"""
        
        # -----------------------------------------

        # creating columns to display cat image and cat's msg
        # -----------------------------------------
        col1, col2 = st.columns([1, 1])
        # -----------------------------------------

        # if user bmi status is Underweight
        # -----------------------------------------
        if user_status == ":red[Underweight]":
            # displaying skinny little cat
            with col1:
                st.image("images\\skinny_cat.png")

            # dsiplaying message
            with col2:
                st.write(underweight_msg)
        # -----------------------------------------

        # else if user bmi status is Normal
        # -----------------------------------------
        elif user_status == ":green[Normal]":
            # displaying Cat
            with col1:
                st.image("images\\Mr.Cat.png")

            # displaying cat's message
            with col2:
                st.write(normal_msg)
        # -----------------------------------------

        # else if user bmi status is Overweight or Obese
        # -----------------------------------------
        elif user_status in [":red[Overweight]", ":red[Obese]"]:
            # displaying fat cat
            with col1:
                st.image("images\\fat_cat.png")

            # displaying fat cat's message
            with col2:
                st.write(overweight_msg)
        # -----------------------------------------

        # rerunning dialog
        # -----------------------------------------
        else:
            st.rerun()
        # -----------------------------------------

        # taking user advice
        # ----------------------------------------- 
        advice = st.text_input("Advice:")
        # -----------------------------------------

        # if advice is not null
        # -----------------------------------------
        if not advice == "":
            st.subheader(":green[Thank you!]")  # displaying thank you
        # -----------------------------------------
    # -----------------------------------------


    # this function will calculate bmi
    # -----------------------------------------
    def calculate_bmi(weight_in_kg, height_in_mts):
        try:
            # squaring height
            # -----------------------------------------
            squared_height = height_in_mts * height_in_mts
            # -----------------------------------------

            # calculating bmi
            # -----------------------------------------
            bmi = round(weight_in_kg / squared_height, 2)
            # -----------------------------------------

            # returning calculated bmi
            return bmi
        except:
            pass
    # -----------------------------------------

    
    # return status
    # -----------------------------------------
    def check_status(user_bmi) -> str:
        
        # empty status
        status = ""

        # if user_bmi is not none
        if not user_bmi is None:
            # if bmi is less than or equal to 18.4 then status is Underweight
            # -----------------------------------------
            if user_bmi <= 18.4:
                status = ":red[Underweight]"  # ignore colour
            # -----------------------------------------

            # if bmi is less than or equal to 24.9 and greater than 18.5 then status is Underweight
            # -----------------------------------------
            elif 18.5 <= user_bmi <= 24.9:
                status = ":green[Normal]"
            # -----------------------------------------

            # if bmi is less than or equal to 25.0 and greater than 39.9 then status is Underweight
            # -----------------------------------------
            elif 25.0 <= user_bmi <= 39.9:
                status = ":red[Overweight]"
            # -----------------------------------------

            # if bmi is greater than or equal to 40.0
            # -----------------------------------------
            elif user_bmi >= 40.0:
                status = ":red[Obese]"
            # -----------------------------------------

            # returning status
            return status
    # -----------------------------------------


    st.divider()
    # displaing title
    # -----------------------------------------
    st.markdown("<h1 style='text-align: center; color: #349eeb;'>BMI Calculator</h1>", unsafe_allow_html=True)
    # -----------------------------------------

    st.divider()

    # taking user inputs
    # -----------------------------------------
    weight = float(st.number_input("Enter Your weight in kilograms: "))  # weight
    height = float(st.number_input("Enter your height in meters: "))  # height
    # -----------------------------------------

    st.divider()

    # creating calculate button
    # -----------------------------------------
    calculate_btn = st.button(":green[Calculate BMI]")
    # -----------------------------------------

    # empty variables
    # -----------------------------------------
    bmi = ""
    status = ""
    # -----------------------------------------

    # if calculated button is clicked
    # -----------------------------------------
    if calculate_btn:
        # calculating bmi and status
        # -----------------------------------------
        bmi = calculate_bmi(weight, height)
        status = check_status(bmi)
        # -----------------------------------------

        # displaying cat dialog
        # -----------------------------------------
        cat(status)
        # -----------------------------------------
    # -----------------------------------------

    st.divider()
    
    # displaying bmi and status
    # -----------------------------------------
    st.subheader(f"Your BMI is: :blue[{bmi}]")
    st.subheader(f"Status: {status}")
    # -----------------------------------------

    st.divider()
# -----------------------------------------

# taking user input
# -----------------------------------------
user_input = st.text_input("Enter Full Form of BMI To Continue:").lower()
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if user_input == "body mass index":
    main()  # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
