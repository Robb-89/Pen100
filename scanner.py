#!/usr/bin/python3 

import socket 
import time 

#We are going to use this variable to store the time it takes to start the application. 
startTime = time.time()

target = input('Please specify the host that you want to scan: ')
target_IP = socket.gethostbyname(target)
print('Initializing Scan for host: ', target_IP)


#instead of socket.connect use socket.connect_ex <-- this will produce an error if there is a block output from scanning
for x in range(3000, 3999):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = scanner.connect_ex((target_IP, x))
    print(connection)
    if(connection == 0):
        print (' Port %d: OPEN' %(x))
    scanner.close()


endTime = time.time()
totalTime = endTime - startTime 
print('Total Time: %s' %(totalTime))