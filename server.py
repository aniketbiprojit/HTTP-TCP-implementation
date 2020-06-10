import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('localhost',8080))
serversocket.listen(1)

send_message = b"""
HTTP/1.1
Content-Type: text/html

<html>
<body>
<b>Hello World</b>
</body>
</html>

"""

while True:
    (clientsocket,address)=serversocket.accept()
    clientsocket.send(send_message)

    msg = clientsocket.recv(1024)

    print(f"Received {msg} from {address}")