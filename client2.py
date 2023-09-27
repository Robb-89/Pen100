#!/usr/bin/python3
import socket
from time import sleep 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.197.68"
port = 2001

print("Defined Host: {0}".format(host))
print("Defined Port: {0}".format(port))

client.connect((host, port)) # Connect to our client
print("Connecting to host: {0}:{1}".format(host, port))

connected = True
print("Connected!")

while True:
    try:
        for number in range(0,11):
            msg = client.recv(1024)
            data = msg.decode('ascii')
            print ("Response {}: {}".format(number, data))
            client.send(data.encode());
    except socket.error:
        connected = False
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connection lost... reconnecting")
        while not connected:
            try:
                client.connect((host,port))
                connected = True
                print("We are Connected Again")
            except socket.error:
                sleep(2)
    finally:
        print("Connected to host: {0}:{1}".format(host, port))
        break
client.close()