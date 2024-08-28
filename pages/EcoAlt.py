import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

# Streamlit page configuration
st.set_page_config(
    page_title="EcoTalk",
    page_icon="",
    layout="wide",  # Set layout to wide
)

# Streamlit page title
st.title("EcoTalk")

# Predefined input prompt template
input_prompt_template = '''
Provide eco-friendly alternatives for the following item: {item_name}.
The response should be in bullet points and focus only on eco-friendly accurate  alternatives with a description of those items. 
If the input is not a valid item name, do not respond.
'''

# Use st.chat_input for user input
user_input = st.chat_input("Enter the name of the item:")

# Check if user has entered an item name
if user_input:
    # Format the input prompt with the item name
    input_prompt = input_prompt_template.format(item_name=user_input)

    # Send the formatted prompt to the LLM and get a response
    messages = [
        {"role": "system", "content": '''
        Respond only to valid item names with a description of those items. Provide eco-friendly accurate alternatives in bullet points.
        If the input is not valid item name respond politely by guiding them to focus items names to receive accurate assistance.
        '''},
        {"role": "user", "content": input_prompt}
    ]

    response = client.chat.completions.create(
        model="gemma2-9b-it",
        temperature=1.2,
        max_tokens=8000,
        top_p=1,
        messages=messages
    )

    # Get the assistant's response
    assistant_response = response.choices[0].message.content

    # Display the LLM's response if it's valid
    if assistant_response.strip():
        st.markdown(assistant_response)
