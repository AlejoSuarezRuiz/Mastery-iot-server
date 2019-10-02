import socket
# from rethinkdb import RethinkDB

# r = RethinkDB()
# r.connect("68.183.149.80", 32769).repl()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8500)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        msj = ""
        while True:
            data = connection.recv(1).decode("utf-8")
            if data and data != "\n":
                msj += data
            elif data == "\n":
                print(msj)
                msj = ""     
    finally:
        connection.close()