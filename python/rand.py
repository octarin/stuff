#!/usr/bin/python3

import os
import random
import re
import sys

FILES = "\.(jpg)|(JPG)|(png)|(PNG)|(bmp)|(jpeg)|(gif)$"
COMMAND = "feh -.d"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        FILES = sys.argv[1]
    lp = [i for i in os.listdir('.') if re.search(FILES, i)]
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

            random.shuffle(lp)
            os.system("{0} \"{1}\" &".format(COMMAND, "\" \"".join(lp[:int(com)])))

        except:
            break

