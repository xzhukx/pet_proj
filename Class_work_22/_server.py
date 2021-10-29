import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65434    # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(conn)
        print(addr)

        with conn:
            print('Connected by', addr)
            while True:
                # GET
                data = conn.recv(25)
                print(data)
                if not data:
                    break
