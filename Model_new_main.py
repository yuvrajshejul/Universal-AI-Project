import os
import streamlit as st
from groq import Groq
# from deeptrans import Translator
from deep_translator import GoogleTranslator

t = GoogleTranslator(source='auto', target='hi')

# translaating from english to hindi
t = GoogleTranslator(source='auto', target='hi')

# Set up Streamlit app title and page layout
st.set_page_config(
    page_title="Ayurvedic Cure Recommender",
    page_icon=":herb:",
    # layout="wide"
)
st.sidebar.success("SELECT THE PAGE FROM ABOVE")


# Function to interact with GROQ API and get Ayurvedic cure
def get_ayurvedic_cure(user_input):
    os.environ['GROQ_API_KEY'] = "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"

    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Generate personalized Ayurvedic remedies for various health issues based on user input. Provide comprehensive solutions and instructions on preparation and usage of the recommended remedy without requiring additional information from the user."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    output = ""
    for chunk in completion:
        output += chunk.choices[0].delta.content or ""
    return output

# Set up Streamlit app title
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px; text-align: center;'>
        <h1 style='color: #333;'>🧬🩺 Universal-AI</h1>
    </div>
    """,
    unsafe_allow_html=True
)
# Create a text input box for user input
user_input = st.text_input("Enter Your Disease Below")

# Check if the user has entered any input
if user_input:
    # Call the function to get Ayurvedic cure based on user input
    ayurvedic_cure = get_ayurvedic_cure(user_input)
    
    # Display the Ayurvedic cure
    st.write("Ayurvedic Cure:")
    st.write(ayurvedic_cure)

    # Create a button to translate the response to Hindi
    if st.button("Translate to Hindi"):
        # Translate the response to Hindi
        translated_text = t.translate(ayurvedic_cure)
        
        # Display the translated text
        st.write("Translated Text (Hindi):")
        st.write(translated_text)