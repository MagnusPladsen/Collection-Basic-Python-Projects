#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:19:56 2021
@author: Magnus Pladsen
Tester brage sin ide om å lage en billån kalkulator
"""

restart = True

import time

while restart != False:
    print("Hei, velkommen til Santander sin billånkalkulator!")
    time.sleep(1)
    alder = int(input(("Hvor gammel er du? ")))
    # Velkommen og sjekk av alder, må være 18 år for å få lån
    
    if alder < 18:
        print("Du må være 18 år for å få billån ")
        time.sleep(1)
        restart = True
    else:
        penger = int(input("Hvor mye tjener du i løpet av året? "))
    # Sjekke hvor mye årslønn til bruker her, så avgjør programmet hvor mye
    # bruker kan låne.    
        
    if penger < 200000:
        print("Du tjener dessverre ikke nok til å få billån. Prøv på nytt eller skaff deg ny jobb :D")
        restart = False
    elif penger >= 200000 and penger < 400000:
        print("Du tjener nok til å få billån på opptil 200 000,- NOK.")
        time.sleep(1)
        lan = int(input("Hvor mye lån vil du ta? "))
    elif penger >= 400000 and penger < 700000:
        print("Du tjener nok til å få billån på opptil 400 000,- NOK.")
        time.sleep(1)
        lan = int(input("Hvor mye lån vil du ta? "))
    elif penger >= 700000 and penger < 1000000:
        print("Du tjener nok til å få billån på opptil 600 000,- NOK.")
        time.sleep(1)
        lan = int(input("Hvor mye lån vil du ta? "))
    elif penger >= 1000000:
        print("Du tjener nok til å få billån på opptil 800 000,- NOK.")
        time.sleep(1)
        lan = int(input("Hvor mye lån vil du ta? "))
    else:
        print("Dette er ikke en gyldig årslønn!")
        break
    # Midlertidlig nå så stopper bare programmet om man skriver noe som ikke er tall
    
    print("Takk for at du valgte Santander til å ta billån! Renten på lånet vårt er 11%")
    rente = 0.11
    years = int(input("Hvor mange år vil du ta lånet på? Det kan være maks 10 år! "))
    # Spørre hvor mange år bruker vil ha lånet på
    
    rente_kr = lan * rente
    totalt = lan + rente_kr
    totalt_ar = (lan + rente_kr) / years
    
    # Regne ut først hva renten er av lånebeløp over hvor mange år bruker valgte
    # Deretter regne ut totalt hva lån + renter * år =
    
    if years > 10:
        print ("Det kan være maks 10 år!")
        break
    else:
        print("Lånet ditt vil være %s og vil betales ned over %s år." % (lan,years))
        time.sleep(1)
        print("Du vil da totalt måtte betale %s etter at renten er regnet ut" % (int(totalt)))
        time.sleep(1)
        print("Renten vil totalt være %s" % (int(rente_kr)))
        time.sleep(1)
        print("Da vil det koste deg %s per år." % (int(totalt_ar)))
        restart = False
        
        
        
    