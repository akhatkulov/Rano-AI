from flask import Flask, request, jsonify,render_template
import requests
import json

app = Flask(__name__)

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "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"

def send_message(message):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }

    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + API_KEY
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["message"]["content"]

@app.route('/api', methods=['GET'])
def handle_request():
    user_message = request.args.get('text')
    if user_message:
        response = send_message(user_message)
        return jsonify({"response": response})
    else:
        return "No text provided"


@app.route('/chat')
def chat():
    return render_template('chat.html')
if __name__ == '__main__':
    app.run()
