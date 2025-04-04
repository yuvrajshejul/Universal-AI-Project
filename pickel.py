# chatbot_model.py

import openai
import pickle

class HealthcareChatbot:
    def __init__(self, api_key):
        # Set your OpenAI GPT-3 API key
        openai.api_key = api_key

    def generate_response(self, prompt):
        # Set the prompt for the healthcare chatbot
        prompt = f"Healthcare Chatbot: {prompt}"

        # Call the OpenAI GPT-3 API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",  # You may use a different engine based on your needs
            prompt=prompt,
            max_tokens=150  # Adjust based on desired response length
        )

        # Extract the generated response from the API result
        generated_response = response['choices'][0]['text'].strip()

        return generated_response

# Instantiate the HealthcareChatbot with your OpenAI API key
chatbot = HealthcareChatbot(api_key='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')

# Save the model state to a pickle file
with open('healthcare_chatbot_model.pkl', 'wb') as file:
    pickle.dump(chatbot, file)
