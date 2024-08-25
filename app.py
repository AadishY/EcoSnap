import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
from streamlit_chat import message  # Import the message function
import time

# Configuration for the generative model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 8192,
}

load_dotenv()  # Load environment variables from .env

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get responses from the Gemini model
def get_gemini_response(prompt, image):
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="You are a sophisticated waste classification assistant programmed and created by Aadish to analyze images of waste and provide detailed, accurate, and professional information related to waste management. Your primary goal is to assist users in understanding how to properly dispose of or utilize various types of waste, while also offering insights into environmental impact."
    )
    #gemini-1.5-flash, gemini-1.5-pro-exp-0801
    try:
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_message = f"Error: {str(e)}"
        st.error(error_message)
        return None

# Initialize the Streamlit app
st.set_page_config(page_title="EcoSnap", layout="wide")
st.header("EcoSnap")

# Apply custom CSS to adjust the input box and file uploader height and width
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 75px !important;
        width: 100% !important;
        resize: none;
    }
    .stFileUploader {
        height: 75px !important;
        width: 100% !important;
    }
    .st-c0 {
    min-height: 75px;
    }
    .aligned-row > div {
        display: flex;
        align-items: center;
    }
    .typing-indicator {
        font-style: italic;
        color: #888;
    }
    .response-container {
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    .response-content {
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container for the input fields and align them in the same line
with st.container():
    col1, col2 = st.columns(2)  # Two columns with equal width
    
    # Change: Swap the input box and file uploader components
    with col1:
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="image_upload", label_visibility="collapsed")
    with col2:
        input_text = st.text_area("Input Prompt (Garbage Name):", key="input", label_visibility="collapsed", placeholder="Enter garbage name here...")

# Prepare the prompt
prompt = f"""
Please analyze the uploaded image and identify the type of waste. If the garbage name provided below is empty, rely on the image to determine the waste type.

Garbage Name {input_text or 'Unknown Waste - Please analyze the image'}
only answer the format questions

Once identified, please classify the waste and provide comprehensive disposal and utilization instructions, you will not inlcude anything above you will just answer in the format given below, you may change the heading if you like, formatted as follows:

1. **Waste Name:** Clearly identify the waste from the image or the provided name.
2. **Type of Waste:** Categorize the waste (e.g., E-waste, Recyclable, Organic, Chemical, etc.).
3. **Dustbin Color:** Specify the correct color of the dustbin for disposal. Provide a brief explanation of the reason behind using this dustbin color.
4. **Resin Identification Code (RIC):** If possible, provide the relevant waste code or resin identification code, along with a brief explanation of its significance. If unsure, omit this step. In short.
5. **Disposal and Utilization Instructions:** Offer detailed, step-by-step instructions on how to properly dispose of or utilize the waste at home. Include creative and professional advice on recycling, reusing, or other sustainable practices. If the waste is not suitable for home management, guide the user on how to responsibly dispose of it at a designated recycling center or facility.
6. **Environmental Awareness:** Add a concise section emphasizing the importance of proper waste disposal. Highlight the environmental benefits, such as waste reduction, resource conservation, or carbon savings, and how these actions contribute to environmental protection.
7. **Carbon Footprint Savings:** Provide an estimation of the carbon footprint savings achieved by correctly disposing of the waste. If possible, include numeric values to quantify the reduction in emissions or resource conservation. Keep this explanation brief but informative in short.
(You may change the **title:** according to your need)

**Important:** The bot is strictly programmed to address waste and garbage-related inquiries only. If the user poses questions unrelated to waste management or provides an irrelevant image, politely prompt them to focus on waste and garbage items.
"""

# Check if an image is uploaded
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)

# Button to submit
submit = st.button("Let Aadish Cook 🧑🏻‍🍳...")

# Display the typing indicator while waiting for the response
if submit:
    if not input_text and not uploaded_file:
        st.warning("Please provide either text input or an image before proceeding.")
    else:
        with st.spinner("EcoSnap is thinking... 🧠"):
            time.sleep(1)  # Simulate a delay for visual effect
            response = get_gemini_response(prompt, image)

        if response:
            # Create columns to separate the image and response
            col1, col_gap, col2 = st.columns([1, 0.1, 3])  # Adjusted for wider bot response

            # Display the uploaded image in the first column
            with col1:
                if uploaded_file is not None:
                    st.image(image, caption="Uploaded Image", use_column_width=True)

            # Display the response in the second column, covering full width
            with col2:
                st.markdown(f'<div class="response-container"><div class="response-content">{response}</div></div>', unsafe_allow_html=True)
