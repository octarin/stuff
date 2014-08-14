#!/usr/bin/env python3

from sys import argv

bin2str = lambda string: "".join([chr(int(string[i*8:i*8+8], 2)) for i in range(len(string)//8)])

if __name__ == '__main__':
    if len(argv) > 1:
        print(bin2str(argv[1]))

