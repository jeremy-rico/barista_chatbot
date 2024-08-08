#import re
import profanity_check as pc

#from profanity_check import predict
from openai import OpenAI
from flask import Flask, render_template, request, jsonify

# Coffee info
MENU = {
    "Mocha Magic": {
        "price": 4.50,
        "description": "A rich blend of espresso, chocolate, and steamed milk."
    },
    "Vanilla Dream": {
        "price": 4.00,
        "description": "A smooth vanilla-flavored latte with a hint of sweetness."
    },
    "Caramel Delight": {
        "price": 4.75,
        "description": "A caramel-flavored coffee with a touch of cream."
    },
    "Hazelnut Harmony": {
        "price": 4.25,
        "description": "A delightful mix of hazelnut and coffee, topped with foam."
    },
    "Espresso Elixir": {
        "price": 3.00,
        "description": "A concentrated shot of pure espresso."
    },
    "Latte Lux": {
        "price": 3.75,
        "description": "A luxurious latte with perfectly steamed milk."
    },
    "Cappuccino Charm": {
        "price": 3.50,
        "description": "A classic cappuccino with a thick layer of foam."
    }
}

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
    This function uses the profanity check model to give the message a profane score 
    between 0 and 1. If the score is above the threshold, it is marked as profane. 
    Default thresh is 0.5
    """
    score = pc.predict_prob([message])[0]
    print(f"profanity score: {score}")
    return score > thresh

# Check for personal opinions
#might use might not
def asks_for_personal_opinion(message):
    #check for intent with nltk
    return

#check intent
# might use might not
def is_related_to_coffee(message):
    return

# main generation response. Needs cleaning.
def generate_response(user_message):
    # Rule Enforcement
    if is_profane(user_message):
        return "Your message contains foul language. Please keep the conversation respectuful."

    message_history.append({"role": "user", "content": user_message.lower().strip()})

    completion = client.chat.completions.create(
        model = model,
        messages = message_history,
    )


    bot_reply = completion.choices[0].message.content
    assistant_message = {"role": "assistant", "content": bot_reply}
    message_history.append(assistant_message)

    return bot_reply

if __name__ == '__main__':
    app.run(debug=True)
