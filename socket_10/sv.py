import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 2050  # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    data = data.decode()
                    try:
                        value = eval(data)
                        res = data + " = " + str(value)
                        print(res)
                        conn.sendall(res.encode())
                    except Exception as e:
                        print(f"Error evaluating expression: {e}")
            except ConnectionResetError:
                print(f"Client {addr} disconnected")
