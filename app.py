import os
import random
import time
from flask import Flask, request, render_template, redirect, jsonify
from groq import Groq
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Initialize the GoogleTranslator
translator = GoogleTranslator(source='auto', target='hi')

# Set up the Groq API
os.environ['GROQ_API_KEY'] = "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"
client = Groq()

#####################################################################
# Navigation bar

@app.route("/", methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route("/new_home", methods=['GET'])
def new_home():
    return render_template('new_home.html')

@app.route("/hospit", methods=['GET'])
def hospit():
    return render_template('Nearest_hospt.html')

@app.route("/chatbot", methods=['GET'])
def chatbot():
    return render_template('home.html')

@app.route("/lets_chat", methods=['GET'])
def form():
    return render_template('home.html')

###############################################################

# Schemes

@app.route("/schemes", methods=['GET'])
def scheme():
    return render_template('schemes.html')

@app.route("/scheme1", methods=['GET'])
def scheme1():
    return render_template('scheme1.html')

@app.route("/scheme2", methods=['GET'])
def scheme2():
    return render_template('scheme2.html')

@app.route("/scheme3", methods=['GET'])
def scheme3():
    return render_template('scheme3.html')

@app.route("/scheme4", methods=['GET'])
def scheme4():
    return render_template('scheme4.html')

##########################################################################

# Login and registration

@app.route("/user_log", methods=['GET'])
def user_log():
    return render_template('User_login.html')

@app.route("/hospit_log", methods=['GET'])
def hospit_log():
    return render_template('Hospital_login.html')

@app.route("/hospit_reg", methods=['GET'])
def hospit_reg():
    return render_template('hospital_registration.html')

@app.route("/user_reg", methods=['GET'])
def user_reg():
    return render_template('User_registration.html')

##########################################################################

# Authentication

# Sample username and password (for demonstration purposes only)
sample_username = "admin"
sample_password = "admin123"

# User login authentication

@app.route('/login_process', methods=['POST'])
def login_process():
    entered_username = request.form['username']
    entered_password = request.form['password']

    if entered_username == sample_username and entered_password == sample_password:
        # Authentication successful
        return redirect('/new_home')
    else:
        # Authentication failed, render the login page with an error message
        error_message = "Login failed. Please check your username and password."
        time.sleep(0.3)
        return render_template('User_login.html', error=error_message)

# Sample user credentials (for demonstration purposes only)
registered_users = {'admin': 'admin123'}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Check if the username is already registered
    if username in registered_users:
        return "Username already registered. Choose a different username."

    # Check if passwords match
    if password == confirm_password:
        # Add the user to the registered users (in-memory example)
        registered_users[username] = password
        return render_template('User_login.html')
    else:
        return "Password and Confirm Password do not match."

###############################################################

# Function to interact with GROQ API and get Ayurvedic cure
def get_ayurvedic_cure(user_input):
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

# Route to handle the generation of chatbot responses
@app.route('/generate_response', methods=['POST'])
def generate_response_endpoint():
    user_input = request.form.get('user_input')
    response = get_ayurvedic_cure(user_input)
    return jsonify({'bot_response': response})

if __name__ == "__main__":
    app.run(debug=True)
