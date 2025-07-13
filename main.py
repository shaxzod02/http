import socket

HOST = ""
PORT = 8000

STATUS_CODES = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    404: "Not Found",
    504: "Service Error",
}

class Request:
    def __init__(self, method, path, version, headers = {}, body = ""):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Reuest({self.method} {self.path} HTTP/{self.version})"


def parse_request_line(req: str) -> Request:
    parts = req.split("\\r\\n\\r\\n")
    request_headers_line = parts[0]
    body = parts[1]

    request_line, headers = parse_request_line(request_headers_line)
    method, path, version = request_line
    return Request(method, path, version, headers, body)


def parse_request_line(req: str) -> tuple[list, dict]:
    parts = req.split("\\r\\n")
    request_line = parts[0].split(" ")
    header_lines = parse_headers (parts[1:])
    return request_line, header_lines
    

    


def parse_headers(headers: list[str]) -> dict:   
    parsed_headers = {}
    for header in headers:
        if ": " in header:
            key, value = header.split(": ")
            parsed_headers [key] = value
    return parsed_headers


def generate_response(request: Request, body: str) -> str:
    resp = "HTTP/1.0 200 OK\\r\\n"
    length = len(body)
    for key, value in request.headers.items():
        resp.append(f"{key}: {value}\\r\\n")
    resp.append(f"Content-Length: {length}\r\n\r\n")
    resp.append(body)
    return "".join(resp)

        
def main() -> None:
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
               
               
            #    print("Client:", data)
            #    conn.sendall(f"Echo: {data}".encode())


if __name__ == "__main__":
    main()

