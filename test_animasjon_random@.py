#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:25:03 2021
@author: Magnus Pladsen
Lage en enkel kort animasjon
"""

import time, sys, random
indent = 0 # starter med 0 spaces
indentIncreasing = True # For å starte med å øke spaces

try:
    while True:
        print(" " * indent, end="") # poste spaces uten ny linjeskift
        print("********")  # Det som skal postes etter spaces
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1 # øke spaces
            stop = random.randint(20, 50)
            if indent == stop or indent == 50:  # random hvor langt "slangen" skal gå bort, stoppe om går over max så ikke bug
                indentIncreasing = False
    
        else:
            indent = indent - 1 # trekke fra spaces helt til det er på 0
            start = random.randint(0, 20)
            if indent == start or indent == 0:
                indentIncreasing = True # øke spaces igjen siden 0
        
except KeyboardInterrupt:  # for å lukke program
    sys.exit()