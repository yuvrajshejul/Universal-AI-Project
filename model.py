import json
import random

# Load the dataset
with open('dataset.json', 'r') as file:
    dataset = json.load(file)

def generate_response(user_input):
    user_input = user_input.lower()
    
    for entry in dataset['data']:
        for symptom in entry['symptoms']:
            if symptom.lower() in user_input:
                response_templates = [
                    f"It seems like you're dealing with {entry['disease']}. Here are some Ayurvedic home remedies you can try: {', '.join(entry['ayurvedic_home_remedies'])}",
                    f"Based on your symptoms, it could be {entry['disease']}. Consider these Ayurvedic home remedies: {', '.join(entry['ayurvedic_home_remedies'])}",
                    f"You might be experiencing {entry['disease']}. Ayurvedic tradition recommends the following home remedies: {', '.join(entry['ayurvedic_home_remedies'])}",
                    f"Your symptoms align with {entry['disease']}. Here are some Ayurvedic home remedies that may help: {', '.join(entry['ayurvedic_home_remedies'])}",
                    f"From what you've described, it seems like {entry['disease']}. Give these Ayurvedic home remedies a try: {', '.join(entry['ayurvedic_home_remedies'])}",
                ]
                return random.choice(response_templates)

    # If no specific match is found, generate a generic response
    generic_responses = [
        "I'm not sure about that. Please consult a healthcare professional.",
        "It's important to see a doctor for accurate diagnosis and advice.",
        "I recommend seeking professional medical help for your symptoms.",
        "Your health is important. Consider consulting with a healthcare professional for personalized advice.",
        "I'm not a doctor, but it's always a good idea to consult with a healthcare professional regarding your symptoms.",
    ]
    return random.choice(generic_responses)
