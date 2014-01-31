#!/usr/bin/python

"""
    This program prints a memory dump
    of a brainfuck program, which is usefull
    for debugging.
"""

import sys
import os

def getchar():
    """
        Simulate the libc standard fonction "getchar".
    The buffer "buf" must be created before this definition
    """
    global buf

    if buf == []: buf = list(sys.stdin.read())
    ret = buf.pop(0)
    return ord(ret)

if len(sys.argv) <= 1:
    fd = sys.stdin

else:
    fd = open(sys.argv[0], 'r')

try:
    string = fd.read()
except IOError:
    print("This file does'nt exists.")

ip = 0
mp = 0
mem = [0 for i in range(500)]
stack = []
buf = []

while ip < len(string):
    if string[ip] == ">":
        if mp != 499:
            mp += 1
        else:
            mp = 0
    elif string[ip] == "<":
        if mp != 0:
            mp -= 1
        else:
            mp = 499
    elif string[ip] == '+':
        if mem[mp] != 255:
            mem[mp] += 1
        else:
            mem[mp] = 0
    elif string[ip] == '-':
        if mem[mp] != 0:
            mem[mp] -= 1
        else:
            mem[mp] = 255
    elif string[ip] == '[':
        if mem[mp]:
            stack.append(ip)
        else:
            ip += 1
            while string[ip] != ']':
                ip += 1
    elif string[ip] == '[':
        if mem[mp]:
            ip = stack[-1]
        else:
            stack = stack[:-1]
    elif string[ip] == ',':
       mem[mp] = getchar()
    elif string[ip] == '.':
       sys.stdout.write(chr(mem[mp]))
    ip += 1

print(mem)
