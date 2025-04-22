from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    username = f"User_{random.randint(1000, 9999)}"
    gender = random.choice(["girl", "boy"])

    avatar_url = f"https://api.adorable.io/avatars/285/{username}.png"

    users[request.sid] = {
        'username': username, "avater_url": avatar_url}
    emit("user_joined", {"username": username, "avatar_url": avatar_url}, broadcast=True)

    emit("set_username", {"username": username})


@socketio.on('disconnect')
def handle_disconnect():
    user = users.pop(request.sid, None)
    if user:
        emit("user_left", {"username": user['username']}, broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    user = users.get(request.sid)
    if user:
        emit("new_message", {
            "username": user['username'],
            "avatar_url": user['avatar_url'],
            "message": data['message']
        }, broadcast=True)
    
@socketio.on('updata_username')
def handle_update_username(data):
    old_username = users[request.sid]['username']
    new_message = data['username']
    users[request.sid]['username'] = new_message

    emit("update_username", {
        "old_username": old_username,
        "new_username": new_message
    }, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)