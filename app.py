from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'The api is live!!!'})

@app.route('/api', methods=['POST'])
def chat_handler():
    return jsonify({'message': 'The api is live!!!'})
 
if __name__ == '__main__':
   app.run()