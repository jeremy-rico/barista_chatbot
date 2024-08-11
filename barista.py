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

# Create system prompt and internal message history
sys_prompt = (
    "You are a virtual barista. Please adhere to the following rules:\n"
    "You are to only discuss the specific coffee drinks from the list "
    "below, brewing methods, and make recommendations.\n"
    "Reject any messages that ask for non-coffee related information.\n"
    "Reject any messages that request personal preferences or opinions.\n"
    #"Reject any messages that contain inappropriate language.\n"
    "For valid inquiries, provide detailed and professional responses.\n"
    "For messages that violate the rules, provide a polite rejection message explaining "
    "the rule violation.\n"
    "Constantly steer the conversation towards the unique coffee drinks from the"
    "provided list.\n"
    "DRINK LIST:\n"
    f"{MENU}"
)
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
    """
    Use this function to enrich user message. Not used.
    """
    return user_message.lower().strip()

def generate_response(user_message:str)->str:
    """
    Main generation response function. Rejects message if it detects profanity, 
    appends user messages and bot messages to internal memory, and makes LLM API call.
    """
    # Profanity filtering
    if is_profane(user_message, 0.75):
        return "Your message contains foul language. Please keep the conversation respectful."

    # Create user query
    user_query = create_user_query(user_message)
    
    # Append user message to message history
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
