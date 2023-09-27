#!/usr/bin/python3

import math 

def is_pronic(n):
    for i in range(1, n):
        if i * (i + 1) == n:
            return True
    return False

def main():
    for i in range(4000, 4999):
        if is_pronic(i):
            print(i)

if __name__ == "__main__":
    main()