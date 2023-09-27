#!/usr/bin/python3 

import itertools
password_start = 'discourse'
password_suffix = '!@#%&'
x = itertools.permutations(password_suffix)
print(list(x))