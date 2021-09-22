import sys
import socket
import time
import threading
from _thread import start_new_thread

from pyiot import errorNotify, errorExit, errorRaise

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def sender(cid):
    print(f"starting sender {cid}")
    try:
        print(f"{cid} client thread starting")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            finished = False
            s.connect((HOST, PORT))
            numtimes = 0
            # print("connection ok")
            while not finished:
                numtimes += 1
                txt = f"Morning from client {cid} / {numtimes}".encode()
                # print(f"sending {txt}")
                s.sendall(txt)
                # print("sent")
                print(s.recv(1024))
                time.sleep(1)
                if numtimes > 3:
                    finished = True
            s.close()
        print(f"{cid} client thread finishing")
    except Exception as e:
        errorNotify(sys.exc_info()[2].tb_lineno, e)
        # print(f"Exception in client {e}")


kids = 12
threads = []
for kid in range(kids):
    threads.append(threading.Thread(target=sender, args=(kid,)))

[t.start() for t in threads]
[t.join() for t in threads]


#
# children = 50
# count = 0
# while count < children:
#     count += 1
#     print(f"starting thread {count}")
#     start_new_thread(sender, (count,))
#     # sender(count)
#
# time.sleep(20)
