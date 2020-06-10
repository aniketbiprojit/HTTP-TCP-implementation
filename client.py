import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8080))

msg=clientsocket.recv(1024)
clientsocket.send(b"Hello!! from client")
print(msg)