#!/usr/bin/python3

import socket 
import telnetlib

#telnet 
def interact(socket):
    t = telnetlib.Telnet()
    t.sock = socket
    t.interact()


#connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.169.68"
port = 2003

client.connect((host, port))
msg = client.recv(1024)
print(msg.decode('ascii'))
interact(client)


#close connection 
client.close()
