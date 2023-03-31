#!/bin/python3

import sys
import socket
from datetime import datetime

#Defining target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translates hostname to ipv4
else:
    print("Invalid amount of args")
    print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close() 
except KeyboardInterupt:
    print("/nExiting program. ")
    sys.exit
    
except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect")
    sys.exit
