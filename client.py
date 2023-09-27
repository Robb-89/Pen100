#!/usr/bin/python3
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8080

print("Defined Host: {0}".format(host))
print("Defined Port: {0}".format(port))

client.connect((host, port)) # Connect to our client
print("Connecting to host: {0}:{1}".format(host, port))


client.connect((host, port)) # Connect to our client
msg = client.recv(1024)
client.close()

print (msg.decode('ascii'))

