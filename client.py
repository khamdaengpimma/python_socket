import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print("Received:", data.decode())
