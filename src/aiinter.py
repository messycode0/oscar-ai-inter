import ollama
import sys
import time
import random
import requests

# yes
is_remote = False
exited = False
serverip = "192.168.1.100"

#Default port is 5000
server_port = 5000

def main(argv):
    print(argv)

    if argv[1] == "-r" or argv[1] == "--remote":
        is_remote = True

    while exited == False:
        line_break("input=")
        input = str(input("Oscar >>"))
        if input == "/exit":
            exited == True
            break
        line_break("output")
        if is_remote:
            slow_type(io_call_ol_remote(input))
        else:
            slow_type(io_call_ol_local(input))
            

        line_break()

    pass

def io_call_ol_local(input): 
    response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': f'You are an ai named Oscar, you will get a promt, make sure you answer very simple, and very short, dont want something very long... Your input is: {input}',
    },
    ])
    return response['message']['content']

def io_call_ol_remote(input):
    url = f'http://{serverip}:{server_port}/ask'
    payload = {'question': input}
    response = requests.post(url, json=payload)
    return response.json().get('answer')

def line_break(text):
    print(f"==============={text}===============")

typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
        # print("")

if __name__ == "__main__":
    main(sys.argv)