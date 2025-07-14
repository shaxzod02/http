import socket
import threading
import json
from typing import List

HOST = ""
PORT = 8000

STATUS_CODES = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    404: "Not Found",
    504: "Service Error",
}

MEMORY = {}

class Request:
    def __init__(self, method, path, version, headers={}, body=""):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Request({self.method} {self.path} {self.version})"


def parse_headers(headers: List[str]) -> dict:
    parsed_headers = {}
    for header in headers:
        if ": " in header:
            key, value = header.split(": ", 1)
            parsed_headers[key] = value
    return parsed_headers


def parse_request(raw_request: str) -> Request:
    try:
        parts = raw_request.split("\r\n\r\n", 1)
        header_section = parts[0]
        body = parts[1] if len(parts) > 1 else ""

        header_lines = header_section.split("\r\n")
        request_line = header_lines[0].split(" ")
        method, path, version = request_line

        headers = parse_headers(header_lines[1:])

        return Request(method, path, version, headers, body)
    except Exception as e:
        print(f"Failed to parse request: {e}")
        return Request("GET", "/", "HTTP/1.0", {}, "")


def generate_response(request: Request, code: int, message: str, body: str) -> str:
    resp = [f"HTTP/1.0 {code} {message}\r\n"]
    resp.append("Content-Type: text/html\r\n")
    resp.append(f"Content-Length: {len(body.encode())}\r\n\r\n")
    resp.append(body)
    return "".join(resp)


def handle_client(conn, addr):
    with conn:
        print(f"[+] Connection established with {addr}")
        data = conn.recv(1024)
        if not data:
            return

        request = parse_request(data.decode())
        print(request)

        response = ""

        if request.method == "GET":
            if request.path in MEMORY:
                response = generate_response(request, 200, STATUS_CODES[200], MEMORY[request.path])
            else:
                response = generate_response(request, 404, STATUS_CODES[404], "<h1>Data not found</h1>")

        elif request.method == "POST":
            try:
                parsed_body = json.loads(request.body)
                MEMORY[request.path] = json.dumps(parsed_body, indent=2)
                response = generate_response(request, 201, STATUS_CODES[201], "<h1>Data created</h1>")
            except json.JSONDecodeError:
                response = generate_response(request, 400, STATUS_CODES[400], "<h1>Invalid JSON</h1>")

        elif request.method == "DELETE":
            if request.path in MEMORY:
                del MEMORY[request.path]
                response = generate_response(request, 200, STATUS_CODES[200], "<h1>Data deleted</h1>")
            else:
                response = generate_response(request, 404, STATUS_CODES[404], "<h1>Data not found</h1>")

        else:
            response = generate_response(request, 400, STATUS_CODES[400], "<h1>Unsupported Method</h1>")

        conn.sendall(response.encode())


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("Listening on port http://127.0.0.1:8000")
        sock.bind((HOST, PORT))
        sock.listen(5)

        while True:
            conn, addr = sock.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()
