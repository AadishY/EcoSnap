import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set the page layout

# Home Title
st.title("🏠 Home")

# Logo Banner with reduced size
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/AadishY/EcoSnap/main/Logo/Squarecorner.png" width="700">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/AadishY/EcoSnap">
            <img src="https://img.shields.io/badge/Source%20Code-GitHub-green" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Title and Description in the center
st.markdown("<h2>🌿 EcoSnap: Your Eco-Friendly AI Assistant</h2>", unsafe_allow_html=True)
st.markdown("<h5>An AI-powered application to classify waste and find proper disposal steps.</h4>", unsafe_allow_html=True)

# Description Section
st.markdown("""
EcoSnap is a comprehensive tool designed to assist users in managing waste more effectively and adopting eco-friendly habits. Our key features include:

- **EcoSnap** 📸: Capture images of waste items to classify them and receive proper disposal methods.
- **EcoAlt** 🌱: Discover environmentally friendly alternatives to everyday products to reduce your carbon footprint.
- **EcoTalk** 🗣️: Chat with our eco-friendly AI assistant to get answers to your environmental questions and receive guidance on sustainable practices.

This project aims to make a significant impact on environmental sustainability by promoting awareness and offering practical solutions.
""")

# Navigation Buttons (not in the same line, one below the other)
if st.button("Go to EcoSnap 📸"):
    switch_page("EcoSnap")

if st.button("Go to EcoAlt 🌱"):
    switch_page("EcoAlt")

if st.button("Go to EcoTalk 🗣️"):
    switch_page("EcoTalk")

st.write("---")

# About Us Section
st.header("About Us")
st.markdown("""
Hello! I am **Aadish Kumar Yadav**, a Class 11th Science student at Red Rose Public School, Lucknow, India. I am passionate about technology and sustainability, which led me to develop EcoSnap.

👨‍💻 As the main developer of EcoSnap, I believe that small actions can lead to big changes, and technology is a powerful tool to bring about this change. My goal is to make it easier for everyone to make environmentally conscious decisions.

🤝 I am joined by my teammate, **Aditya Sameer Pandey**, who is also a Class 11th Science student from Red Rose Public School. Aditya shares the same passion for sustainability and contributes significantly to our project.

🌱 We developed EcoSnap for the Sustainable Innovators competition, aiming to create a user-friendly application that encourages sustainable living practices. 

For more details about my projects and collaborations, you can visit my [GitHub Profile](https://github.com/AadishY).

Thank you for visiting our page and for your interest in making the world a greener place!
""")
