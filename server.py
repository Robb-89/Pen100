#!/usr/bin/python3
#server.py

import socket 
import threading

host = "192.168.1.130"
port = 8080
     
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('Server is listening for incoming connections')
     
while True:
#accept connections from outside
    (clientsocket, address) = server.accept()
    print(clientsocket, address)
ct = server_thread(clientsocket)
ct.run()