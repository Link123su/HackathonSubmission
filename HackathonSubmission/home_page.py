import streamlit as st
from random import randint

# -----------------------------------------
# st.divider() -> displays horizontal line  
# -----------------------------------------

# page settings
# -----------------------------------------
st.set_page_config(
    page_title="UsefulAppsThatYouNeed",
    page_icon="Things",
    layout="wide",
    initial_sidebar_state="expanded",
)
# -----------------------------------------

# adding logo to sidebar
st.logo("images\\logo.jpg")


# main function
def main() -> None:

    # displaing title
    # -----------------------------------------
    st.divider()
    st.markdown("<h1 style='text-align: center; color: #349eeb;'>Useful Apps And Pets That You Need</h1>", unsafe_allow_html=True)
    st.divider()
    # -----------------------------------------

    # some text
    # -----------------------------------------
    text = """Welcome to Useful Apps and Pets - your ultimate hub for innovative solutions and delightful companions!
            Built with passion and creativity, this website is my submission for the "Coding with Lewis" Hackathon. Here, you'll discover a collection of useful apps designed to make your life easier.
            Explore, enjoy, and let us know what you think!
            This website is made by a youtuber 'PythonicMind'. Visit About page to know more."""
    # -----------------------------------------

    # displaying text
    # -----------------------------------------
    st.subheader(":red[Our each App has a unique feature.]")
    st.markdown(f"<h2 style='text-align: left; color: white;'>{text}</h1>", unsafe_allow_html=True)
    st.divider()
    # -----------------------------------------

    # header
    # -----------------------------------------
    st.header(":blue[Meet some cool animals:]", divider=True)
    # -----------------------------------------

    # displaying image
    # -----------------------------------------
    st.image("images\\welcome.png")
    # -----------------------------------------
    st.divider()

    # list of animals name and some information about them
    # -----------------------------------------
    animals = [("Mr.Cat", "Meet me in BMI calculator."),
               ("Mr.Hamster", "Meet me in Counter app."),
               ("Mr.Gorilla", "Meet me in Maths Quiz app."),
               ("Mr.Cool Cat", "Meet me in Number Guessing Game. I like reading books📚."),
               ("Mr.Rabbit", "Meet me in Password Generator app.I like to eat 🥑"),
               ("Mr.Rio Parrot", "My name is Rio.Meet me in Temperature Converter app."),
               ("Mr.Naughty Monkey", "Meet me in ToDo app."),
               ("Mr.Smart Cat", "Meet me in Quote Generator app.")]
    # -----------------------------------------

    # displaying animals images
    # -----------------------------------------
    for animal in animals:
        animal_name = animal[0]  # animal_name
        animal_msg = animal[1]   #animal info

        st.image(f"images\\{animal_name}.png")  #displaying image
        st.info(animal_msg)  # displaying animal info
        st.divider()
    # -----------------------------------------


# storing random_number in session_state
# -----------------------------------------
if "random_number" not in st.session_state:
    st.session_state.random_number = str(randint(1, 100))
# -----------------------------------------

# taking user input
# -----------------------------------------
value = str(st.slider("The Page will only appear when you select a random number.😁", 0, 100))
# -----------------------------------------

# validating user input
# -----------------------------------------
if value == st.session_state.random_number:
    main()  # calling main function if user input is correct
# -----------------------------------------

# -------------------------------THE END------------------------------- #
