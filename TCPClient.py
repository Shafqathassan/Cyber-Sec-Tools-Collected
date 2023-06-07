#!/usr/bin/python3
#credit:freecodecamp-hackerspoilt

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#specify host
#host = '192.168.1.104'
host = socket.gethostbyname()

port = 444

clientsocket.connect(('192.168.1.104', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

