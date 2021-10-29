import socket
import csv
# https://realpython.com/python-sockets/

HOST = '0.0.0.0'  # The server's hostname or IP address
PORT = 65434       # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

_file = "test_send.csv"

with open(_file, "rb") as csv_file:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = csv_file.read(1024)
            print('Sending data')
            s.sendall(data)
            print('Sent data')
            if not data:
                break



    # while True:
    #     msg = input('msg: ')
    #     # SEND
    #     s.sendall(msg.encode()+b"f")
    #     # GET
    #     data = s.recv(1024)
    #     print('Received', repr(data))