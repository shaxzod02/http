# 🖧 Python Mini HTTP Server

A simple multi-threaded HTTP server written in Python using only the standard library.  
Supports basic in-memory storage and handles `GET`, `POST`, and `DELETE` requests.

---

## 🚀 Getting Started

### 1. Clone the repository (or copy the files)

```bash
git clone git@github.com:shaxzod02/http.git
cd  http
```

## Run the server
python3 main.py
###
Server will start on

# 📡 API Usage
### 🔸 POST /data — Store JSON data

curl -X POST http://127.0.0.1:8000/data \
  -H "Content-Type: application/json" \
  -d '{"name": "Ali", "age": 25}'

### Response:
<h1>Data created</h1>

# 🔸 GET /data — Retrieve data
curl http://127.0.0.1:8000/data
### Response:
```
{
  "name": "Ali",
  "age": 25
}
```

## 🔸 DELETE /data — Delete stored data
curl -X DELETE http://127.0.0.1:8000/data
### Response:
<h1>Data deleted</h1>

## 🧠 How It Works
The server uses socket and threading to handle multiple clients concurrently.

Data is stored in a global Python dictionary called MEMORY.

Each request path (e.g., /data) is treated as a unique key.

JSON is used for storing and retrieving POSTed data.

## 💡 Future Improvements
Serve static files from /static

Add route handlers with parameters

Data validation & error handling

Logging system

Token-based authentication

## 🧪 Test Script
### Create a file called test_api.sh with the following content:
#!/bin/bash

echo "Creating data..."
curl -X POST http://127.0.0.1:8000/data \
  -H "Content-Type: application/json" \
  -d '{"test": "Hello, world!"}'
echo -e "\n"

echo "Fetching data..."
curl http://127.0.0.1:8000/data
echo -e "\n"

echo "Deleting data..."
curl -X DELETE http://127.0.0.1:8000/data
echo -e "\n"

echo "Fetching again (should be 404)..."
curl http://127.0.0.1:8000/data
echo -e "\n"
### Then run:
bash test_api.sh



