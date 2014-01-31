#!/usr/bin/python

# This program generate a brainfuck code
# printing the given string

import sys

if (len(sys.argv) >= 2):
    s = sys.argv[1]

    for i in s:
        print(ord(i) * '+' + "." + ord(i) * '-')

