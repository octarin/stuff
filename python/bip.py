#!/usr/bin/python2

import sys

t = 0x2055418
# t = 0x20554181354654656435416564616541

while 1:
    c = ((t & 60) * (t >> 15) | t*(((t>>15)|(t>>8))&(60&(t>>12)))) & 0xff
    # print(chr(c), end="")
    bug = sys.stdout.write(chr(c))
    t+=1
    # t+=5

