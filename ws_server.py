import os
import time
import socket
from flask import Flask, render_template
from flask_sockets import Sockets

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8500)
sock.bind(server_address)
sock.listen(1)

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/get_data')
def dataChanel(ws):
    """Send data."""
    while not ws.closed:
        connection, client_address = sock.accept()
        try:
            msj = ""
            while True:
                data = connection.recv(1).decode("utf-8")
                if data and data != "\n":
                    msj += data
                elif data == "\n":
                    # print(msj)
                    ws.send(msj)
                    msj = ""     
        finally:
            connection.close()

@sockets.route('/submit')
def dataChanel(ws):
    """Recives incoming data."""
    while not ws.closed:
        data = ws.receive()
        if data:
            print(data)

@app.route('/')
def hello():
    return 'Hello World!'
            
if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()