from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from time import sleep
# import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socket = SocketIO(app, cors_allowed_origins="*", manage_session=True)

# SERVER

@socket.on('connected')
def handlelogs(connection):
    file = open('app.log','r')
    data = file.read()
    lines = data.split('\n')
    for line in lines[-10:]:
        emit('logged', {'data': line})
        print(line)
    last_len = len(lines)
    while True:
        
        c = 0
        with open('app.log') as f:
            for line in f:
                c += 1
                if c > last_len:
                    print(line)
                    emit('logged', {'data': line})
        last_len = c
        sleep(0.5)
    

# END SERVER

if __name__ == '__main__':
    socket.run(app)