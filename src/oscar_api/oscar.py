
import ollama 
import requests

class OscarAI:
    def __init__(self, serverip="0.0.0.0", port="5000"):
        self.serverip = serverip
        self.server_port = port
        
    def io_call_ol_local(self, input): 
        response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': f'You are an ai named Oscar, you will get a promt, make sure you answer very simple, and very short, dont want something very long... Your input is: {input}',
        },
        ])
        return response['message']['content']

    def io_call_ol_remote(self, input):
        url = f'http://{self.serverip}:{self.server_port}/ask'
        payload = {'question': input}
        response = requests.post(url, json=payload)
        return response.json().get('answer')