import socket
import threading
from _thread import start_new_thread

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def handler(conn, addr, xid):
    print(f"{xid}: Connected by", addr)
    byt = 0
    while True:
        data = conn.recv(1024)
        if not data:
            break
        byt += len(data)
        conn.sendall(data)
    print(f"{xid}: number bytes received and sent: {byt}")
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    xids = 0
    while True:
        try:
            conn, addr = s.accept()
            xids += 1
            start_new_thread(handler, (conn, addr, xids))
        except KeyboardInterrupt as ki:
            break
print(f"serviced {xids} clients")
