#!/usr/bin/python3 
import requests as req
import sys 
Url = 'http://192.168.197.68:8080/bijection/'

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


flag= []
for number in numbers:
    info = {'index': number}
    print('Trying: ', number)
    x = req.post(Url,data=info)
    print(x.text)

"""for letters in x.text:
    flag.append(letters)
    print(flag)"""