import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)
    except ConnectionRefusedError:
        print("oops, no server listening.")
        data = None
    except Exception as e:
        print(f"some error happened: {e}")
        data = None

print("Received", repr(data))
