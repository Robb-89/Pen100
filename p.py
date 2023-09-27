#!/usr/bin/python3 




def is_pronic_number(number):
    for i in range(1, number):
        if i * (i + 1) == number:
            return True
    return False

pronic_number = []
    
for number in range(4000,4999):
        if is_pronic_number(number):
            pronic_number.append(number)

print(pronic_number)