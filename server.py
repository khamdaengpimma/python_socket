import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# List to hold all client connections
clients = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            received_text = data.decode()
            print(received_text)  # Print received message
            broadcast(received_text, client_socket)
        except:
            # Remove the client if there's an error
            clients.remove(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                # Remove the client if it's no longer reachable
                clients.remove(client)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = s.accept()
        print(f"Accepted connection from {client_address}")
        clients.append(client_socket)

        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
