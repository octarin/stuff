#!/usr/bin/env python3

from os import listdir
from subprocess import call
from random import shuffle
from re import search
import sys

FILE_MATCH = "\.(jpg)|(JPG)|(png)|(PNG)|(bmp)|(jpeg)|(gif)$"
COMMAND = "feh -.d --zoom=max"

if len(sys.argv) > 1:
    FILE_MATCH = sys.argv[1]

pictures_list = [_file for _file in listdir('.') if search(FILE_MATCH, _file)]
if len(pictures_list) == 0:
    print("Error: the current directory does'nt contains any pictures matching the regex \"{0}\"".format(FILE_MATCH))
    sys.exit(-1)

nb_to_load = 1

while True:
    try:
        _ = input()

        if _ != "":                             #Does'nt modify nb_to_load if user inputs nothing
            nb_to_load = int(_)

        if nb_to_load > len(pictures_list):
            nb_to_load = len(pictures_list);
            print("Warning : max len", nb_to_load, 
                  "\nLoading", nb_to_load, "pictures by default", file=sys.stderr)

        shuffle(pictures_list)

        call(COMMAND.split() + pictures_list[:int(nb_to_load)])

    except:
        break

