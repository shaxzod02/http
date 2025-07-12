import socket

HOST = ""
PORT = 8000
# This script creates a TCP server that listens on the specified host and port.

class Request:
    def __init__(self, method, path, version, headers = {}):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers

    def __str__(self):
        return f"Reuest({self.method} {self.path} HTTP/{self.version})"


def parse_request_line(req: str) -> Request:
    parts = req.split("\\r\\n")
    method, path, version = parts[0].split(" ")
    headers = parse_headers(parts[1:])
    return Request(method, path, version, headers)


def parse_headers(headers: list[str]) -> dict:   
    parsed_headers = {}
    for header in headers:
        if ": " in header:
            key, value = header.split(": ")
            parsed_headers [key] = value
    return parsed_headers

        
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("Listening on port http://127.0.1:8000")
        sock.bind((HOST, PORT))
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            print(f"Connected established with this IP:", addr)
        
            while True:
               data = conn.recv(1024)
               request = parse_request_line(data.decode())
               request.method
               
            #    print("Client:", data)
            #    conn.sendall(f"Echo: {data}".encode())


if __name__ == "__main__":
    main()

