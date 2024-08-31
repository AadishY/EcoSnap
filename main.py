import streamlit as st
from streamlit_extras.badges import badge


# --- PAGE SETUP ---
st.set_page_config(
    
    layout="wide",
    page_title="EcoSnap",
    page_icon=":earth_africa:",
)
st.markdown(
    """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var buttons = document.querySelectorAll("button");
        buttons.forEach(function(button) {
            if (button.innerText.includes('Fork')) {
                button.style.display = 'none';
            }
        });
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Define pages
about_page = st.Page(
    "ch/home.py",
    title="Home",
    icon="🏠",
    default=True,
)
project_1_page = st.Page(
    "ch/EcoSnap.py",
    title="EcoSnap",
    icon="📸",
)
project_2_page = st.Page(
    "ch/EcoAlt.py",
    title="EcoAlt",
    icon="🌱",
)
project_3_page = st.Page(
    "ch/EcoTalk.py",
    title="EcoTalk",
    icon="🗣️",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown(
    '''
    Created by Aadish ✨ <a href="https://github.com/AadishY">
    <img src="https://img.shields.io/badge/Click_Here_To_See_My-Profile-blue" alt="GitHub">
    </a>
    ''', unsafe_allow_html=True
)



pg.run()  # Run navigation outside of the sidebar context
