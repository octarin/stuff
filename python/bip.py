#!/usr/bin/python2

# You shall couple it with aplay to make it work ;)

import sys

t = 0x2055418

while 1:
    c = ((t & 60) * (t >> 15) | t*(((t>>15)|(t>>8))&(60&(t>>12)))) & 0xff
    bug = sys.stdout.write(chr(c))
    t+=1

