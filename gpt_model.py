import openai

# Set your OpenAI API key here


def generate_response(prompt):
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


# Example usage
user_input = "What are the symptoms of the flu?"
bot_response = generate_response(user_input)
print(f"User: {user_input}")
print(f"Chatbot: {bot_response}")
