#!/usr/bin/python3

import socket 

remote_host = "http://192.168.169.68:8080/crawling"
remote_port = 80

request = "GET / HTTP/1.1\r\nHost: http://192.168.169.68:8080/crawling\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host, remote_port))
client.send(request.encode())

response = client.recv(4096)
print(response.decode())

