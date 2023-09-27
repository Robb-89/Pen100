#!/usr/bin/python3 
#Post.py
import requests 



url = 'http://192.168.197.68:8080/login-1/'
cred = {'Username':'thobbes', 'Password':'leviathan'}

x = requests.post(url, data=cred)

print(x.text)