import streamlit as st

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page setting
# -----------------------------------------
st.set_page_config(
    page_title="Temperature🌡️ Convertor🔃",
    page_icon="🌡️🔃",
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
    # this will convert given temp to Fahrenheit
    # -----------------------------------------
    def to_fahrenheit(number) -> str:
        temp = round(number * (9 / 5) + 32, 1)
        temp = f"{temp}°F🌡️"
        return temp
    # -----------------------------------------


    # this will convert given temp to Celsius
    # -----------------------------------------
    def to_celsius(number) -> str:
        temp = round((number - 32) * (5 / 9), 1)
        temp = f"{temp}°C🌡️"
        return temp
    # -----------------------------------------


    # displaying title
    # -----------------------------------------
    st.title("Temperature Convertor")
    # -----------------------------------------
    st.divider()

    # taking user input
    # -----------------------------------------
    input_number = st.number_input("Enter Temperatue to Convert: ")
    # -----------------------------------------

    # creating radio buttons
    # -----------------------------------------
    option = st.radio(
        "Select Conversion Type",
        ["**Celsius ➡ Fahrenheit**", "**Fahrenheit ➡ Celsius**"])
    # -----------------------------------------

    # adding divder to seperate result
    st.divider()

    # creating empty result variable
    # -----------------------------------------
    result = ""
    # -----------------------------------------

    # converting Celsius to Fahrenheit
    # -----------------------------------------
    if option == "**Celsius ➡ Fahrenheit**":
        result = to_fahrenheit(input_number)
    # -----------------------------------------

    # converting Fahrenheit ➡ Celsius
    # -----------------------------------------
    elif option == "**Fahrenheit ➡ Celsius**":
        result = to_celsius(input_number)
    # -----------------------------------------

    # displaying result
    # -----------------------------------------
    st.subheader(f"Result: :red[{result}]")
    # -----------------------------------------
    st.divider()

    # creating container to display parrot image
    # -----------------------------------------
    parrot_container = st.container()
    # -----------------------------------------

    # creaeting columns to display parrt image and text
    # -----------------------------------------
    col1, col2 = parrot_container.columns([1, 1])
    # -----------------------------------------

    # displaying parrt image
    # -----------------------------------------
    with col1: 
        st.image("images\\Mr.Rio Parrot.png")
    # -----------------------------------------

    # displaying parrot's msg
    # -----------------------------------------
    with col2:
        st.subheader("Hello! I'm Mr.Rio Parrot. I'll help you convert temperature unit.")
    # -----------------------------------------
# -----------------------------------------

# taking user input
# -----------------------------------------
user_input = st.text_input(":red[Enter Mr.Parrot's name to continue. Hint: Check home page]").lower()
# -----------------------------------------

# if user enters correct answer
# -----------------------------------------
if "rio" in user_input:
    main()  # calling main function
# -----------------------------------------

# -------------------------------THE END------------------------------- #
