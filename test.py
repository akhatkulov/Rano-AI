from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

# Flask ilovasini yaratish
app = Flask(__name__)

# GPT-J modelini yuklash
model_name = "EleutherAI/gpt-j-6B"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Matn generatsiya qilish funksiyasi
def generate_text(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=max_length, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# GET so'rovi bilan matn generatsiya qilish
@app.route('/generate', methods=['GET'])
def generate():
    prompt = request.args.get('prompt', '')
    if prompt:
        response_text = generate_text(prompt)
        return jsonify({"response": response_text})
    else:
        return jsonify({"error": "No prompt provided"}), 400

# Flask ilovasini ishga tushurish
if name == 'main':
    app.run(debug=True)