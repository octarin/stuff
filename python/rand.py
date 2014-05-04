#!/usr/bin/env python3

from os import listdir
from subprocess import call
from random import shuffle
from re import search
import sys

FILES = "\.(jpg)|(JPG)|(png)|(PNG)|(bmp)|(jpeg)|(gif)$"
COMMAND = "feh -.d"

if len(sys.argv) > 1:
    FILES = sys.argv[1]

lp = [i for i in listdir('.') if search(FILES, i)]
if len(lp) == 0:
    print("Error: the current directory does'nt contains any pictures matching the regex \"{0}\"".format(FILES))
    sys.exit(-1)

com = 1

while 1:
    try:
        c_ = input()

        if c_ != "":
            com = c_

        if int(com) > len(lp):
            com = len(lp);
            print("Warning : max len", com, file=sys.stderr)
            print("Loading", com, "pictures by default", file=sys.stderr)

        shuffle(lp)

        call(COMMAND.split() + lp[:int(com)])

    except:
        break

