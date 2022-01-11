#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:38:28 2021
@author: Magnus Pladsen
automate boring stuff with python 2nd edition
COLLATZ Syndrome
"""
import time

def collatz():
    global number
    if (number % 2) == 0:
        print("%s / 2 = " % (str(number)))
        number = number // 2
        print(number)
        print("")
        time.sleep(1)
    else:
        print("(%s * 3) + 1 =" % (str(number)))
        number = 3 * number + 1
        print(number)
        print("")
        time.sleep(1)

main = True

while main == True:
    start = True
    try:
        number = int(input("Skriv inn ett tall så skal jeg bruke matte for å få det til å bli 1 UANSETT= "))
        while start == True:
            collatz()
            if number == 1:
                print("Nå er tallet 1")
                start = False
                
    except ValueError:
        print("Skriv inn ett tall!")