#!/usr/bin/python

import sys
import os
import re
import random

NOM_PAGE_BASE = "biblio"
NOMBRE_IMG_PAGE = 50
TYPES_IMG = "\.(jpg)|(png)|(bmp)|(jpeg)|(gif)|(PNG)|(JPG)$"
HTML_HEADER = '<html>\n\t<head>\n\t\t<meta charset="utf-8" />\n\t\t<meta name="generator" content="Python generator (c) Pierre Bonnet aka octarin" />\n\t\t<title>Liste des images du dossier</title>\n\t\t<link rel="stylesheet" href="style.css" />\n\t</head>\n\t<body>\n\n'
HTML_FOOTER = "\n\t\n</body>\n</html>\n"

def img_rand(img_list):
    try:
        while 1:
            buf = input()
            if buf == '':
                buf = '1'
            random.shuffle(img_list)
            os.system("feh \"{0}\" &".format("\" \"".join(img_list[:int(buf)])))
    except:
        pass

def makepage(numero, img_list):
    fd = open("{0}{1}.html".format(NOM_PAGE_BASE, numero), 'w')
    sys.stdout = fd
    links = "\t\t<p>\n"

    print(HTML_HEADER)

    if numero > 0:
        links += '\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Précédent</a>\n'.format(NOM_PAGE_BASE, numero-1)
    if numero < int(len(img_list) / NOMBRE_IMG_PAGE):
        links += '\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Suivant</a>'.format(NOM_PAGE_BASE, numero+1)

    links += "\t\t</p>"
    
    print(links)

    for i in range(NOMBRE_IMG_PAGE*numero, NOMBRE_IMG_PAGE*(numero+1)-1):
        if i < len(img_list):
            print('\t\t<a href="{0}"><img src="{0}" alt="{0}" height=200/></a>'.format(img_list[i]))

    print(links)
    print(HTML_FOOTER)

    sys.stdout = sys.__stdout__
    fd.close()

os.system('rm -rf *.html')

img_list = sorted([i for i in os.listdir('.') if re.search(TYPES_IMG, i) != None])

for i in range(0, int(len(img_list) / NOMBRE_IMG_PAGE) + 1):
    makepage(i, img_list)

rep = input("Ouvrir la bibliotheque/Images random/Fermer (1/2/3) : ")
if rep == '1':
    os.system('firefox {0}0.html& 2> /dev/null > /dev/null'.format(NOM_PAGE_BASE))
elif rep == '2':
    img_rand(img_list)

sys.exit(0)

