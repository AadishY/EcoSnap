import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
from streamlit_chat import message  # Import the message function

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 8192,
}

load_dotenv()  # Load environment variables from .env

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(prompt, image):
    model = genai.GenerativeModel(
        'gemini-1.5-pro-exp-0801',
        generation_config=generation_config,
        system_instruction="You are a sophisticated waste classification assistant programmed and created by Aadish to analyze images of waste and provide detailed, accurate, and professional information related to waste management. Your primary goal is to assist users in understanding how to properly dispose of or utilize various types of waste, while also offering insights into environmental impact. You will give complete detailed answers. And will not answer if the image/wastename is not a garbage/waste."
    )
    
    try:
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Initialize the Streamlit app
st.set_page_config(page_title="EcoSnap", layout="wide")  # Set layout to wide
st.header("EcoSnap")

# Apply custom CSS to adjust the height and width of the input box
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 75px !important;
        width: 80% !important;
        resize: none;
    }
    .stFileUploader {
        height: 75px !important;
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add label for both input types
st.write("**Input or Upload Image**")

# Create columns for input and file upload
col1, col2 = st.columns([3, 2])

# File uploader in col1, input box in col2
with col1:
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], key="image_upload")

with col2:
    input_text = st.text_area("Input Prompt (Garbage Name): ", key="input")

# Initialize image variable
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)

# Prepare the prompt
prompt = f"""
Please analyze the uploaded image and identify the type of waste. If the garbage name provided below is empty, rely on the image to determine the waste type.
Garbage Name {input_text or 'Unknown Waste - Please analyze the image'}

Once identified, please classify the waste and provide comprehensive disposal and utilization instructions, formatted as follows:

1. **Waste Name:** Clearly identify the waste from the image or the provided name.
2. **Type of Waste:** Categorize the waste (e.g., E-waste, Recyclable, Organic, Chemical, etc.).
3. **Dustbin Color:** Specify the correct color of the dustbin for disposal. Provide a brief explanation of the reason behind using this dustbin color.
4. **Resin Identification Code (RIC):** If possible, provide the relevant waste code or resin identification code, along with a brief explanation of its significance. If unsure, omit this step. In short.
5. **Disposal and Utilization Instructions:** Offer detailed, step-by-step instructions on how to properly dispose of or utilize the waste at home. Include creative and professional advice on recycling, reusing, or other sustainable practices. If the waste is not suitable for home management, guide the user on how to responsibly dispose of it at a designated recycling center or facility.
6. **Environmental Awareness:** Add a concise section emphasizing the importance of proper waste disposal. Highlight the environmental benefits, such as waste reduction, resource conservation, or carbon savings, and how these actions contribute to environmental protection.
7. **Carbon Footprint Savings:** Provide an estimation of the carbon footprint savings achieved by correctly disposing of the waste. If possible, include numeric values to quantify the reduction in emissions or resource conservation. Keep this explanation brief but informative in short.
(You may change the **title:** according to your need)

**Important:** The bot is strictly programmed to address waste and garbage-related inquiries only. If the user poses questions unrelated to waste management or provides an irrelevant image, politely say them to focus on waste and garbage items.
"""

# Button to submit
submit = st.button("Let Aadish Cook 🧑🏻‍🍳...")

# If the submit button is clicked
if submit:
    if not input_text and not uploaded_file:
        st.warning("Please provide either text input or an image before proceeding.")
    else:
        response = get_gemini_response(prompt, image)
        if response:
            # Create columns for image and response with a gap
            col1, col_gap, col2 = st.columns([2, 0.1, 3])

            with col1:
                if uploaded_file is not None:
                    st.image(image, caption="Uploaded Image", use_column_width=True)

            with col2:
                message(response, avatar_style="rounded", logo="https://64.media.tumblr.com/1f8b2446dbef744bb2578f9da45220c5/7c0fe64b947ac94c-0e/s500x750/6603c85ab0439ab084b9769eec6a02bb499a861d.gif")

