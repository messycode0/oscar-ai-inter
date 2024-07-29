from flask import Flask
import request
import jsonify
import ollama

app = Flask(__name__)

#Default port is 5000
server_port = 5000

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    # Process the question using Ollama
    answer = process_with_ollama(question)
    return jsonify({'answer': answer})

def process_with_ollama(question):
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': f'You are an ai named Oscar, you will get a promt, make sure you answer very simple, and very short, dont want something very long... Your input is: {input}',
    },
    ])
    return response['message']['content']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port)
