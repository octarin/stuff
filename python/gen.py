#!/usr/bin/env python3

import sys
import os
import re

#Some variables you can modify
NOM_PAGE_BASE = "biblio"
NOMBRE_IMG_PAGE = 50
TYPES_IMG = "\.(jpg)|(png)|(bmp)|(jpeg)|(gif)|(PNG)|(JPG)$"

def makepage(numero, img_list):
    buf ='<html>\n\t<head>\n\t\t<meta charset="utf-8" />\n' \
        '\t\t<title>Liste des images du dossier</title>\n' \
        '\t\t<link rel="stylesheet" href="style.css" />\n' \       #You can add your own stylesheet
        '\t</head>\n\t<body>\n' \
        '\n\t\t<p>'

    nav = ''
    if numero > 0:
        nav += '\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Précédent</a>\n'.format(NOM_PAGE_BASE, numero-1)
    if numero < int(len(img_list) / NOMBRE_IMG_PAGE):
        nav += '\t\t\t<a href="{0}{1}.html" alt="{0}{1}.html">Suivant</a>\n'.format(NOM_PAGE_BASE, numero+1)

    buf += nav + "\t\t</p>"

    for i in range(NOMBRE_IMG_PAGE*numero, NOMBRE_IMG_PAGE*(numero+1)-1):
        if i < len(img_list):
            buf += '\t\t<a href="{0}"><img src="{0}" alt="{0}" height=200/></a>'.format(img_list[i])

    buf += '\t\t<p>' + nav + '\t\t</p>' + '\n\t</body>\n</html>'

    with open("{0}{1}.html".format(NOM_PAGE_BASE, numero if numero else ''), 'w') as fd:
        fd.write(buf)


os.system('rm {0}*.html'.format(NOM_PAGE_BASE))

img_list = sorted([file_ for file_ in os.listdir('.') if re.search(TYPES_IMG, file_) != None])

for nb_page in range(0, int(len(img_list) / NOMBRE_IMG_PAGE) + 1):
    makepage(nb_page, img_list)

sys.exit(0)

