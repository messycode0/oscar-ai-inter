import sys
import time
import random

# Import main Oscar API
import oscar_api.oscar

# yes
is_remote = False
exited = False
serverip = "192.168.1.100"

#Default port is 5000
server_port = 5000

def main(argv):
    print(argv)

    if argv[1] == "-r" or argv[1] == "--remote":
        oscar = oscar_api.oscar.Oscar(serverip, server_port)
        is_remote = True
    else:
        oscar = oscar_api.oscar.Oscar()

    while exited == False:
        line_break("input=")
        input = str(input("Oscar >>"))

        if input == "/exit":
            exited == True
            break
        line_break("output")

        if is_remote:
            slow_type(oscar.io_call_ol_remote(input))
        else:
            slow_type(oscar.io_call_ol_local(input))
            

        line_break()

    pass

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