# appy.py
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_HOST = "http://13.38.23.208:5000/"

def nlp_translator(query):
    r = requests.post(API_HOST, json={"question": query})
    return r.content.decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    response = nlp_translator(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
