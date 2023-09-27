#!/usr/bin/python3

import socket
import time 


startTime = time.time()

target = input('Please specify the host you want to scan: ')
host = socket.gethostbyname(target)
print("Initializing Scan for host", host)

def is_pronic_number(number):
    for i in range(1, number):
        if i * (i + 1) == number:
            return True
    return False

pronic_number = []
    
for number in range(3999, 5000):
        if is_pronic_number(number):
            pronic_number.append(number)

print(pronic_number)
x = 0


for value in pronic_number:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = scanner.connect_ex((host, value))
        if (connection == 000):
            print(' Port %d: OPEN' %(value))
        scanner.close()
    
endTime = time.time()
totalTime = endTime - startTime
print('Total TIme: %s' %(totalTime))
