#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

# sym = ".+-*/^()"
sym = "+-*/^"
usr = " "

def calc(string):
    in_nb = True
    nbs = []
    calcs = []
    ret = 0.

    string = "".join([i for i in string if i in "0123456789"+sym])

    for i in string:
        if i in "0123456789":
            if in_nb:
                nbs[-1][-1] += i
            else:
                nbs[-1].append(i)
                in_nb = True
        else:
            if in_nb and i in "+-":
                nbs.append(i)
                in_nb = False
    # Principe de fonctionnement général : 
    # 1) lecture opération
    # 2) ret <opération> float(nbs[indicesuivant])
    # 3) indice += 2

    return string

print "\x1b[0;31m===Super calculatrice===\x1b[0;32m" 

while usr != "":
    try:
        usr = raw_input("> ")
    except:
        print
        break
    
    usr = "".join([i for i in usr if i != " "])
    if usr != "":
        print "\x1b[0;34m" + str(calc(usr)), "\x1b[0;32m"

sys.stdout.write("\x1b[0;0m")
