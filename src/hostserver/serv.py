from flask import Flask
import request
import jsonify

from oscar_api.oscar import Oscar  

app = Flask(__name__)

#Default port is 5000
server_port = 5000

oscar = Oscar()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    # Process the question using Ollama
    answer = process_with_ollama(question)
    return jsonify({'answer': answer})

def process_with_ollama(question):
    return oscar.io_call_ol_local(question)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port)
