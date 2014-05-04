#!/usr/bin/env python3

import sys
import os
import subprocess
import re

#Some variables you can modify
NOM_PAGE_BASE = "biblio"
NOMBRE_IMG_PAGE = 50
TYPES_IMG = "\.(jpg)|(png)|(bmp)|(jpeg)|(gif)|(PNG)|(JPG)$"

def makepage(numero, img_list):
    fd = open("{0}{1}.html".format(NOM_PAGE_BASE, numero), 'w')
    sys.stdout = fd

    print('<html>\n\t<head>\n\t\t<meta charset="utf-8" />\n\t\t<meta name="generator" content="Python generator (c) Pierre Bonnet aka octarin" />')
    print('\t\t<title>Liste des images du dossier</title>')
    print('\t\t<link rel="stylesheet" href="style.css" />')
    print('\t</head>\n\t<body>')

    print("\n\t\t<p>")
    if numero > 0:
        print('\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Précédent</a>'.format(NOM_PAGE_BASE, numero-1))
    if numero < int(len(img_list) / NOMBRE_IMG_PAGE):
        print('\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Suivant</a>'.format(NOM_PAGE_BASE, numero+1))

    print("\t\t</p>")

    for i in range(NOMBRE_IMG_PAGE*numero, NOMBRE_IMG_PAGE*(numero+1)-1):
        if i < len(img_list):
            print('\t\t<a href="{0}"><img src="{0}" alt="{0}" height=200/></a>'.format(img_list[i]))

    print("\t\t<p>")
    if numero > 0:
        print('\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Précédent</a>'.format(NOM_PAGE_BASE, numero-1))
    if numero < int(len(img_list) / NOMBRE_IMG_PAGE):
        print('\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Suivant</a>'.format(NOM_PAGE_BASE, numero+1))

    print("\t\t</p>")

    print('\n\t</body>\n</html>')

    sys.stdout = sys.__stdout__
    fd.close()

os.system('rm {0}*.html'.format(NOM_PAGE_BASE))

img_list = sorted([i for i in os.listdir('.') if re.search(TYPES_IMG, i) != None])

for i in range(0, int(len(img_list) / NOMBRE_IMG_PAGE) + 1):
    makepage(i, img_list)

sys.exit(0)

