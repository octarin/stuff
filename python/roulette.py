#!/usr/bin/python

import random

total = 100
continuer = 1
while continuer:
    check = 1
    while check:
        try:
            numero = int(input("Entrez un numéro entre 0 et 49 : "))
            assert not (numero < 0 and numero > 49)
            check = 0
        except ValueError:
            print("Un NUMERO !!!")
            check = 1
        except AssertionError:
            print("ENTRE 0 ET 49 !!!")
            check = 1
    
    check = 1
    while check:
        try:
            mise = int(input("Misez ce que vous voulez : "))
            assert mise > 0 and mise <= total
            check = 0
        except ValueError:
            print("Un nombre merde !!!")
            check = 1
        except AssertionError:
            print("Allez, espèce de radin...")
            check = 1

    bille = random.randrange(50)
    if numero == bille:
        print("Vous gagnez ! Vous recevez %d €." % 3 * mise)
    elif numero % 2 == bille % 2:
        print("Vous recevez %d €." % (mise // 2))
        total += mise / 3
    else:
        print("Vous perdez votre mise :( (%d€)" % mise)
        total -= mise

    continuer = input("Continuer ? (O/N) : ")
    if total > 0 and continuer == 'O':
        continuer = True
    else:
        continuer = False

