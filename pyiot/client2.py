import socket
import time
import threading
from _thread import start_new_thread

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def sender(cid):
    try:
        print(f"{cid} client thread starting")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            finished = False
            numtimes = 0
            s.connect((HOST, PORT))
            while not finished:
                numtimes += 1
                txt = b"Morning from client"
                s.sendall(txt)
                time.sleep(10)
                if numtimes > 4:
                    finished = True
        print(f"{cid} client thread finishing")
    except Exception as e:
        print(f"Exception in client {e}")


children = 2
count = 0
while count < children:
    count += 1
    print(f"starting thread {count}")
    # start_new_thread(sender, (count,))
    sender(count)
