import streamlit as st
import random
################################ PAGE SETUP #########################
# Set up the page
st.set_page_config(
    page_title="Superhero Name",
    layout="wide", # or wide
    page_icon="🦸‍♂️", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)
############################## APLICATION ############################
# Predefined list of superhero catchphrases

# Predefined list of superhero catchphrases
catchphrases = [
    "Saving the world, one step at a time!",
    "With great power comes great responsibility!",
    "Justice is my middle name!",
    "Evil doesn’t stand a chance!",
    "I’m not just a hero, I’m a legend!"
]

# Title
st.title("Superhero Name Creator 🦸‍♂️🦸‍♀️")

# Inputs
color = st.text_input("What's your favorite color?")
animal = st.text_input("What's your favorite animal?")
lucky_number = st.number_input("Enter a random lucky number:", min_value=0, step=1)

# Dropdown for superpower
superpower = st.selectbox(
    "Choose your superpower:",
    ["Flying", "Invisibility", "Super Strength", "Telepathy", "Time Travel"]
)

# Generate Superhero Name
if color and animal and lucky_number:
    superhero_name = f"{color} {animal} of {lucky_number}"
    st.subheader(f"Your Superhero Name: {superhero_name}")
    st.write(f"Superpower: {superpower}")

    # Add a Superhero Motto
    st.write(f"Motto: *Unleash the power of the {color} {animal}!*")

# Bonus: Generate Random Catchphrase
if st.button("Generate Random Superhero Catchphrase"):
    st.write(f"Catchphrase: *{random.choice(catchphrases)}*")