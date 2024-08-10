import json
import profanity_check as pc

from openai import OpenAI
from flask import Flask, render_template, request, jsonify

# Load data
with open("data/menu.json") as f:
    MENU = json.load(f)

# Define global OpenAI variables
client = OpenAI()
model = 'gpt-4o-mini'
sys_prompt = ("You are a detailed and professional barista. Use the following "
              "menu to provide information and recommendations based on the user's "
              "preferences. Do not give personal preferences or opinions. Constantly "
              "steer the conversation back towards the items on the menu."
              f"{MENU}")

message_history = [{"role": "system", "content": sys_prompt}]


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_reply = generate_response(user_message)
    
    return jsonify({'reply': bot_reply})


def is_profane(message:str, thresh:float=0.5)->bool:
    """
    This function uses the profanity check library to give the message a profane score 
    between 0 and 1. If the score is above the threshold, it is marked as profane. 
    Default threshold is 0.5
    """
    score = pc.predict_prob([message])[0]
    return score > thresh

def create_user_query(user_message:str)->str:
    return user_message.lower().strip()

# main generation response. Needs cleaning.
def generate_response(user_message:str)->str:
    # Rule Enforcement
    if is_profane(user_message):
        return "Your message contains foul language. Please keep the conversation respectuful."

    # Create user query
    user_query = create_user_query(user_message)
    
    # Append User message to message history
    message_history.append({
        "role": "user",
        "content": user_query
    })

    # Invoke model
    completion = client.chat.completions.create(
        model = model,
        messages = message_history,
    )

    # Append model response to message history
    completion_text = completion.choices[0].message.content
    message_history.append({
        "role": "assistant",
        "content": completion_text
    })

    return completion_text

if __name__ == '__main__':
    app.run(debug=True)
