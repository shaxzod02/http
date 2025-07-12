import socket

HOST = ""
PORT = 8000
# This script creates a TCP server that listens on the specified host and port.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print(f"Connected established with this IP:", addr)
        data = conn.recv(1024)
        print("Client:", data)
        conn.sendall(b"Hello, client!")
    
