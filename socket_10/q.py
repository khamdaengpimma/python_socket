# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"10/7*5-3")
    data = s.recv(1024)

print(f"Received {data!r}")