import streamlit as st

# Set the page layout

# Home Title
st.title("🏠 Home")

# Logo Banner with reduced size
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://cdn.jsdelivr.net/gh/AadishY/EcoSnap@main/Logo/Squarecorner.png" width="700">
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
st.markdown("<h2 style='color: #2e8b57;'>🌿 EcoSnap: Your Eco-Friendly AI Assistant</h2>", unsafe_allow_html=True)


st.markdown("<h5 style='color: #3e8e41;'>An AI-powered application to classify waste and find proper disposal steps.</h5>", unsafe_allow_html=True)

# Description Section
st.markdown("""
EcoSnap is your go-to tool for managing waste effectively and embracing eco-friendly practices. Our innovative features are designed to make sustainability both easy and impactful:

- **EcoSnap** 📸: Snap a photo of waste items to classify them and receive detailed disposal instructions. ♻️
- **EcoAlt** 🌱: Discover eco-friendly alternatives to everyday products and reduce your carbon footprint. 🌍
- **EcoTalk** 🗣️: Chat with our AI assistant to get answers to your environmental questions and tips on sustainable living. 🌿

Our mission is to foster environmental awareness and provide practical solutions for a greener future. Together, we can make a difference! 🌟
""", unsafe_allow_html=True)


# Navigation Buttons (not in the same line, one below the other)
if st.button("Go to EcoSnap 📸"):
    st.switch_page("ch/EcoSnap.py")

if st.button("Go to EcoAlt 🌱"):
    st.switch_page("ch/EcoAlt.py")

if st.button("Go to EcoTalk 🗣️"):
    st.switch_page("ch.EcoTalk.py")

st.write("---")
# About Us Section
st.markdown("<h2 style='color: #4682b4;'>About Us</h2>", unsafe_allow_html=True)

st.markdown("""
#### **Aadish Kumar Yadav: Elden Lord** 🌟  
<img src="https://i.pinimg.com/originals/ec/5f/37/ec5f377a267f9e999a5f4b13bd0fb102.gif" 
             style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover;" />
              <br>
Hello! I am **Aadish Kumar Yadav**, a Class 11th Science student at Red Rose Public School, Lucknow, India. My passion for technology and sustainability led me to develop **EcoSnap**. 🌱<br>
As the main developer, I believe that every small action can contribute to a significant change. By harnessing technology, my goal is to simplify the process of making eco-friendly decisions and foster a more sustainable lifestyle.

#### **Aditya Sameer Pandey: Secretary** 🌟
<img src="https://raw.githubusercontent.com/AadishY/EcoSnap/main/Logo/Screenshot%202024-08-31%20191741.png" 
             style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover;" />
              <br>
I am **Aditya Sameer Pandey**, also a Class 11th Science student at Red Rose Public School, Lucknow. My dedication to sustainability and technology drives my work on **EcoSnap**. 🌍<br>
Working alongside Aadish, I focus on enhancing the functionality and user experience of EcoSnap. Our joint efforts aim to promote sustainable practices and inspire positive environmental actions.

#### **Our Project** 🚀  
We created EcoSnap for the Sustainable Innovators competition, aiming to deliver a user-friendly application that encourages green choices. We are enthusiastic about making a positive environmental impact and inviting others to join us in our mission. 🌿

For more details about our projects and collaborations, you can visit my <a href="https://github.com/AadishY">
    <img src="https://img.shields.io/badge/Github-Profile-green" alt="GitHub">
</a>

Thank you for visiting our page and supporting our efforts to make the world a greener place! Your interest and involvement are crucial in driving the change towards a more sustainable future. 🌏
""", unsafe_allow_html=True)


st.write("---")

st.markdown("<h2 style='color: #6a5acd;'>Credit</h2>", unsafe_allow_html=True)

st.markdown("""
We would like to extend our gratitude to the following:

- **Google Gemini** 🧠: For providing advanced image recognition capabilities.
- **Groq** 🚀: For powering our text models with high performance.
- **Streamlit** 🌐: For enabling us to create this web application from python with ease.
""")
st.write("---")
st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #32cd32;'>Thank You!</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
We deeply appreciate your support for EcoSnap! 🌟
**Your interest** helps drive our mission for a sustainable future. 🌍 Together, we can make a positive impact on the environment. 🌿
Thank you for joining us on this journey! 💪
""", unsafe_allow_html=True)
