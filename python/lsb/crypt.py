#!/usr/bin/python

import sys
import random

if len(sys.argv) <= 1:
    sys.exit(1)

with open("a.out", "wb") as fd:

    for lettre in sys.argv[1]:
        for bit in range(8):
            char = random.randrange(2, 0xff)
            char = ((char & 0xfe) + ((ord(lettre) >> 7 - bit) & 0x1)) & 0xff
            out = hex(char)[2:]
            if len(out) % 2:
                out = "0" + out
            fd.write(bytes.fromhex(out))

