#!/usr/bin/python

import sys

if len(sys.argv) > 1:

    fd = open(sys.argv[1], "rb")
    dump = fd.read()
    fd.close()

    offset = 0
    for offset in range(int(len(dump)/8)):
        offset *= 8
        buf = 0
        for bit in range(offset, offset + 8):
            buf += (dump[bit] & 0x1) << (7 - (bit - offset))
        print(chr(buf), end="")

    print()

