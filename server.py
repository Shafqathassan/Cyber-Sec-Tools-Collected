#create TCP server in python3

#!/usr/bin/python3

import socket

#creating the socket object
serversocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#store host name
host = socket.gethostbyname()
port = 444

#bind values to socket
serversocket.bind((host, port))

#listen for TCP connections(TCP listener)
serversocket.listen(3)

#while loop
while True:
    clientsocket, address = serversocket.accept()
    
    print ("Recieved connection from "% str(address))
    
    message = 'Thank you for connecting to the server :)' + "\r\n"
    clientsocket.send(message)
    clientsocket.close()
