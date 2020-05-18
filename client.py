import socket

host = '127.0.0.1'
port = 63431

socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_instance.connect((host, port))


# send -> max data acc to NIC
# sendall -> sends all data in parts
socket_instance.sendall(b'Hello Server from Client')

data=socket_instance.recv(1024)

while data:
    print(data)
    data=socket_instance.recv(1024)