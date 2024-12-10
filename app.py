from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "OPENAI_sk-proj-ORvqD_2HYj8Ny8cC7xUl9XZXR2YXSjqI4oDX4ertEtqrn5B3OWAFSnL-HduFPkdMc_IX_YFgIPT3BlbkFJHpCqH-2NfTfUA2UEgsXX_x7LWAKP-YDVeZY3kk9gjZFSLWjIQVVBTK6arZNg73iAjLnIqZzRoAAPI_KEY"  # API kalitini atrof-muhit o'zgaruvchisi orqali olish

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

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Xatolikni tekshirish
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

@app.route('/api', methods=['GET'])
def handle_request():
    user_message = request.args.get('text')
    message = """Assalomu alaykum! Sizning muammoniz fuqarolik huquqi sohasiga tegishli. Quyidagilarni qilishni tavsiya
                <br>
                qilaman: <br>
                <br>
                1. Dalillarni yig'ish: <br>
                - Sotuv shartnomasining asl nusxasi. <br>
                - To'lov amalga oshirilmaganligini isbotlaydigan dalillar (masalan, bank hisoboti yoki boshqa yozuvlar).
                <br>
                <br>
                2. Xaridor bilan bog'lanish: <br>
                - To'lovni eslatish uchun rasmiy ogohlantirish xatini yuboring. Bu xat yozma yoki elektron shaklda
                bo'lishi mumkin. <br>
                <br>
                3. Sudgacha nizoni hal qilish: <br>
                - Xaridor bilan muzokaralar o'tkazing. Agar kelishuvga erisha olmasangiz, nizoni sud orqali hal qilishga
                <br>
                tayyorgarlik ko'ring. <br>
                <br>
                4. Sudga murojaat qilish: <br>
                - Agar yuqoridagilar ishlamasa, yashash joyingizdagi sudga da'vo arizasi bilan murojaat qiling. <br>
                Shartnoma asosida xaridorni majburiyatlarini bajarishga undash mumkin. <br>
                <br>
                5. Huquqiy maslahat: <br>
                - Advokat yoki yurist bilan maslahatlashing, ular sizning huquqlaringizni to‘liq himoya qilishga yordam
                <br>
                beradi. <br>

                <br>

                Qonun asoslari:<br>
O‘zbekiston Respublikasi Fuqarolik Kodeksi (28-modda va boshqa tegishli moddalar). <br>
              </p>"""
    return jsonify({"response":message})
    # if user_message:
    #     response = send_message(user_message)
    #     return jsonify({"response": response})
    # else:
    #     return jsonify({"error": "No text provided"}), 400

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True,port=1212,host="0.0.0.0")
