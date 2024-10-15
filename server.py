import yaml
from flask import Flask, request, jsonify
from flask_cors import CORS
from LLMChat import ChatAssistant

app = Flask(__name__)

with open('config/SERVER_CONFIG.yaml', 'r') as file:
    config = yaml.safe_load(file)

app.config.update(
    PORT=config['server']['port'],
    DEBUG=config['server']['debug']
)

CORS(app)
chat_assistant = ChatAssistant("config/OAI_CONFIG_LIST.json")

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/v1/chat', methods=['POST'], strict_slashes=False)
def chat():
    data = request.json
    user_message = data.get('query', '')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Use the ChatAssistant class to handle the chat
    response = chat_assistant.initiate_chat(user_message)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
