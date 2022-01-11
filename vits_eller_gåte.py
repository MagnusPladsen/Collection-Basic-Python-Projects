#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:37:04 2021
@author: Magnus Pladsen
Anna sin ide om vitser og gåter
"""
import time, random, sys
start = True

vits_list = ['Hva kalles en samisk soldat? - Kruttlapp', 
             'Hvorfor har svenskene et kålhode i hanskerommet? - Fordi de bruker det som legitimasjon.',
             'Hva kaller du en tannlege som er veldig forsiktig i arbeidet sitt? Svar: Tannpirker.',
             'Hva står skrevet under alle flaskene i Sverige? Åpnes i den andre enden.',
             'Hva står i toppen av svenske luer? - Skal brukes på hodet!',
             'Hva kaller du en intelligent, kjekk og følsom mann? Et rykte.',
             'Hva kalles samenes overhode? - Laptop',
             'Vet du hvordan man kan se om det har vært en elefant i kjøleskapet? - Det er fotspor i leverposteien!',
             'Alle barna kikket ut fra skyskraperen untatt Inger, hun trodde hun hadde vinger.',
             'Alle barna kastet snøball på læreren unntatt Svein, han kastet stein.',
             'Hørt om svensken som gikk til politiet fordi paraplyen hans var slått ned.',
             'Alle barna hadde blitt større unntatt Sindre, han hadde blitt mindre.',
             'Alle barna var på besøk i fengselet untatt Helle, hun satt på enecelle.',
             'Alle barna vart bleikere unntatt Runar han vart brunar.',
             'Alle barna var fattige, unntatt Otto, han spilte lotto.',
             'Alle barna plukket seg i nesen untatt Inger, hun hadde ingen finger.',
             'Alle barna spilte wow untatt Siv, hun hadde et liv.',
             'Hvorfor flyr fugler sørover om vinteren? – Det er for langt å gå.',
             'Jeg tenker på å fjerne ryggraden. – Jeg føler at det bare er den som holder meg oppe.',
             'Jeg valgte å selge støvsugeren min. – Den bare samler støv.',
             'Hvorfor ble kokken arrestert? – Han knuste et egg.',
             'Har du noen gang prøvd å spise en klokke? – Det er veldig tidkrevende!',
             'Du er ikke sann! – Nei! Jeg er grus.',
             'Har du fyr? – Nei jeg har dame..',
             'Det var en gang, men nå er det en korridor.',
             'Jeg forstår fullt ut hvordan det føles å være et batteri. Jeg blir også sjeldent inkludert i ting.',
             'En blind mann går inn i en bar. Og et bord. Og en stol.',
             'Hvorfor liker rednecks å gjøre det «doggy-style»? – På den måten kan de begge se wrestling på TV.',
             'Hva er en rednecks siste ord? Hold ølen min og følg med nå!',
             'Jenta sier: «Jeg er kald!» Fyren svarer: «Gå bort til hjørnet, der er det 90 grader!»',
             'Hvorfor slo fysikklæreren opp med biologilæreren? De hadde ingen kjemi.',
             'Visste du at håndklær er den største årsaken til tørr hud?',
             'Et eple kom seg ikke inn i en bar, fordi i døra sto det en eplenektar',
             'Hva er likheten mellom Plantasjen og Galtvort? Du finner harry potter begge steder',
             'Det var fest i fruktfatet. "Hvorfor ble det plutselig så mørkt?" sa eplet til bananen. "Fordi pæra har gått"',
             'Hva heter Kinas rikeste person? Full Peng-Pung',
             'Hva kaller man soldater som holder hånd i hånd? Leiesoldater',
             'Hvorfor har okser horn? Fordi det hadde sett dumt ut med rundstykker',
             'To nåler satt på et gjerde. Så sier den ene til den andre: "Meh, vi stikker!"',
             'Vet du hvorfor vinden er flau? Fordi den har løyet.',
             'Hva får du hvis du krysser et piggsvin med en slange? Piggtråd',
             'Hvilket instrument spiller elgen? El-gitar',
             'Hvorfor kan ikke jeg hoste når Morten Harket?',
             'Hvorfor kan ikke jeg skyte når Karl Eirik Schjøtt Pedersen?',
             'Hva sa den ene strømledningen til den andre? For en spennende dag!',
    ]   # 45 vitser

gåte_list = ['Hva er forskjellen mellom en loppe og en elefant?',
             'Hva er svart når den er ren, men hvit når den er skitten?',
             'Hvilken kopp kan du ikke drikke av?',
             'Hva er mindre enn en mus, men fyller et helt hus?',
             'Hvilket tau kan du ikke dra i?',
             'De fattige har det, de rike trenger det, og hvis du spiser det, dør du. Hva er det?',
             'Hvem er sønnen til foreldrene mine, men likevel ikke broren min?',
             'Hvilken hage trenger ikke å vannes?',
             'Hvilket dyr er det høfligste?',
             'Hvilke duer kan ikke fly?',
             'Hvis du gjetter riktig, har du gjettet galt. Hvis du gjetter galt, har du gjettet riktig. Hva er jeg?',
             'Hva kan høre uten ører, snakke uten munn og svare på alle språk?',
             'Fire jenter gikk til skolen, og hadde bare en ødelagt paraply på deling. Hvordan kan det ha seg at ingen av dem ble våte?',
             'Hva har ben, men kan ikke gå, og har mat, men kan ikke spise?',
             'Hva er rundt som en ball, gjennomsiktig som glass, lett som en fjær, vakkert som en regnbue og skapes og ødelegges av et pust?',
             'Hvor er havet uten bølger, elvene uten vann, skogene uten trær, byene uten mennesker og fjellene helt flate?',
             'Hvilket dyr legger seg med skoene på?',
             'Hva får du hvis du tråkker på en flaggermus?',
             'Hva holder til på bakken, men blir aldri møkkete?',
             'Hva kan spilles uten regler, og uten at noen vinner eller taper?',
             'Emilie løper maraton. Like før målstreken passerer hun løperen på andre plass. Hvilken plass kommer Emilie på?',
             'Hvilket spørsmål kan du ikke svare ja på uten å lyve?',
             'Hvor langt kan en kanin løpe inn i skogen?',
             'En voksen mann holder et vannglass høyt over hodet, og slipper det ned på gulvet uten å søle en dråpe. Hvordan klarer han det?',
             'Hvilken oppfinnelse gjør det mulig å se tvers gjennom en murvegg?',
             'Hvordan kan du få en ball til å stoppe midt i lufta, snu og kommer tilbake til deg uten at den treffer noe underveis?',
             'Hva kan du holde i din høyre hånd, som du ikke kan holde i din venstre?',
             'Hvilket ord på fire bokstaver blir kortere når du legger til tre bokstaver?',
             'Hva er tre pluss tre pluss tre pluss tre pluss tre?',
             'Hvilken nøkkel kan ikke låse opp noen dør?'
    ]   # 30 gåter


gåte_svar = ['En elefant kan ha lopper, men en loppe kan ikke ha elefanter!',
             'Tavle.',
             'Edderkoppen.',
             'Sneglen.',
             'Fortauet.',
             'Ingenting',
             'Meg selv.',
             'Barnehagen.',
             'Bukken.',
             'Vinduer.',
             'Ordet galt.',
             'Ekkoet.',
             'Det regnet ikke.',
             'Bordet.',
             'Såpeboblen.',
             'På kartet.',
             'Hesten.',
             'Flaggermos.',
             'Skyggen.',
             'Et instrument.',
             'Andre plass.',
             'Sover du?',
             'Halvveis. Deretter løper den ut av skogen.',
             'Vannglasset er tomt.',
             'Vinduet.',
             'Ved å kaste den rett opp.',
             'Venstre hånd.',
             'Kort.',
             'Skog.',
             'Skiftenøkkel.'
    ]   # 30 svar, svar 1 hører til gåte 1 osv.


while start == True: # Main program loop
    svar = input('''Vil du høre en vits eller en gåte? Skriv "exit" for å gå ut.
> ''').lower()
    if svar == "vits" or svar == "en vits":
        vits = True
        while vits == True:
            time.sleep(0.5)
            print (vits_list[random.randint(0,45)])
            vitsFortsette = input("""Vil du høre en vits til?
> """).lower()
            if vitsFortsette == "ja":
                time.sleep(0.5)
                
            elif vitsFortsette == "nei":
                vits = False
            
            elif vitsFortsette == "exit":
                sys.exit()
                
            else:
                print('Svar "ja" eller "nei" din løk! Da får du en ny vits. Håper den er like teit som deg :P')
            
    elif svar == "gåte" or svar == "en gåte":
        gåte = True
        while gåte == True:
            nummer = random.randint(0,30)
            time.sleep(0.5)
            print (gåte_list[nummer])
            gåteSvar = input("""Skriv svaret ditt her
> """)
            if gåteSvar == gåte_svar[nummer]:
                time.sleep(0.5)
                print("Hva faen... Har du hørt den før?")
                
            elif gåteSvar == "exit":
                sys.exit()
            
            else: 
                time.sleep(0.5)
                print("FEIL! Riktig svar er...")
                time.sleep(0.5)
                print(gåte_svar[nummer])

            time.sleep(0.5)
            gåteFortsette = input("""Vil du høre en gåte til?
> """).lower()
            if gåteFortsette == "ja":
                time.sleep(0.5)
                
            elif gåteFortsette == "nei":
                gåte = False
                
            elif gåteFortsette == "exit":
                sys.exit()
                
            else:
                print('Svar "ja" eller "nei" din løk! Da får du en ny gåte. Håper den er like teit som deg :P')
    
    elif svar == "exit":
        sys.exit()           
    
    else:
        time.sleep(0.5)
        print('Prøv igjen! Svar enten "vits" eller "gåte"')
        
