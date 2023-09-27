#!/usr/bin/python3
import socket
import sys



def receive_data(host, port, buffer_size=1024):
    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected")

    # Receive data in chunks
    received_data = b''
    while True:
        chunk = client.recv(buffer_size)
        if chunk:
            received_data += chunk
        else:
            break

    return received_data

if __name__ == "__main__":
    host = '192.168.169.68'
    port = 2002
    payload = receive_data(host, port)
    
imageArray = payload.split(b'\r\n\r\n')

for i in range(0, len(imageArray) - 1):
    pos = imageArray[i].find(b'\r\n')
    fileName = b'fetched_' + imageArray[i][0:pos]
    print(fileName.decode())
    fileContent = imageArray[i][pos + 2:-2]

with open(fileName.decode(), 'wb+') as f:
        f.write(fileContent)
    
