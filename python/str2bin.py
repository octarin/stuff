#!/usr/bin/env python3

from sys import argv

str2bin = lambda string: ''.join([bin(256+ord(i))[3:] for i in string])

if __name__ == "__main__":
    if len(argv) > 1:
        print(str2bin(" ".join(argv[1:])))



