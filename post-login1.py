#!/usr/bin/python3 

import requests as req
from requests.auth import HTTPBasicAuth

Login_url = "http://192.168.197.68:8080/login-2/"

auth=({'username':'thobbes','password':'leviathan'})

x = req.post(Login_url, data=auth)
print(x.text)
