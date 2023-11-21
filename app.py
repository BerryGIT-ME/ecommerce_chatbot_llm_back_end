from flask import Flask, jsonify, request
from dotenv import load_dotenv
from llm.llm_agent import ai_chat
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'The api is live!!!'})

@app.route('/api', methods=['POST'])
def chat_handler():
    data = request.get_json()
    messages = data['messages']

    response_text = ai_chat(messages)
    return jsonify({"role": "assistant", "content": response_text})

if __name__ == '__main__':
   app.run(debug=True)