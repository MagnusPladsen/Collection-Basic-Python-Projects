# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:10:17 2021
Teste ut loop og if else 
Stein saks papir - 1 spiller
Automate boring stuff with python - 2nd edition
@author: Magnus Pladsen
"""

import time, sys, random

ties = 0
wins = 0
losses = 0
# lagre hvor mange ties, losses and wins

win = "You won!"
loss = "You lost!"
tie = "It is a TIE!"
# for å slippe å skrive samme setning om igjen 100 ganger

print(" Welcome to ROCK, PAPER AND SCISSORS. At any time PRESS Q to exit!")

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        
        # bruker sitt svar
        print("Rock, Paper or Scissors?")
        svar = input()#.lower
        if svar == "q":
            sys.exit()
        elif svar == "rock":
            bruker = "r"
            print("Rock versus...")
            time.sleep(1)
            break
        elif svar == "paper":
            bruker = "p"
            print("Paper versus...")
            time.sleep(1)
            break
        elif svar == "scissors":
            bruker = "s"
            print("Scissors versus...")
            time.sleep(1)
            break
        
        # CPU sitt svar
    random_number = random.randint(1, 3)
    if random_number == 1: # Rock
        cpu = "r"
        time.sleep(1)
        print("Rock!")
    elif random_number == 2: # Paper
        cpu = "p"
        time.sleep(1)
        print("Paper!")
    elif random_number == 3: # Scissors
        cpu = "s"
        time.sleep(1)
        print("Scissors!")

        # Finne vinner
    if bruker == cpu:
        print(tie)
        time.sleep(1)
        ties = ties + 1
    elif bruker == "r" and cpu == "p":
        print(loss)
        time.sleep(1)
        losses = losses + 1
    elif bruker == "r" and cpu == "s":
        print(win)
        time.sleep(1)
        wins = wins + 1
    elif bruker == "p" and cpu == "r":
        print(win)
        time.sleep(1)
        wins = wins + 1
    elif bruker == "p" and cpu == "s":
        print(loss)
        time.sleep(1)
        losses = losses + 1
    elif bruker == "s" and cpu == "p":
        print(win)
        time.sleep(1)
        wins = wins + 1
    elif bruker == "s" and cpu == "r":
        print(loss)
        time.sleep(1)
        losses = losses + 1

            
