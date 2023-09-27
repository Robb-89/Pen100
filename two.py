#!/usr/bin/python3
 
import requests
 
flag_list = []
for page in range(1, 50):
    response = requests.get(f'http://192.168.169.68:8080/{page}.html')
    flag_list.append(response.text)
 
print(''.join([flag.strip("\n") for flag in flag_list])) 