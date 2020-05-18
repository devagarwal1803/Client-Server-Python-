import socket

# Kind of protocol -> ipv4
# kind of transport protocol -> tcp(SOCK_STREAM),udp(SOCK_DGRAM)
socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host Address and port number
socket_instance.bind(("127.0.0.1", 63431))

socket_instance.listen()

conn, address = socket_instance.accept()
# conn is also instance of socket class


print("Just got connected by:", address)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    conn.sendall(b'I received data from you :-)')