#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 23:28:59 2021
@author: Magnus Pladsen

"""

birthdays = {'anna': '10.November', 'brage': '4. March', 'magnus': '14.March'}

while True:
    name = input('''Enter a name to check when the person has their birthday.
> ''').lower()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name.title())
    else:
        print('I do not have the birthday for ' + name.title())
        newBirthday = input('''What is their birthday?
> ''')
        birthdays[name] = newBirthday
        print('Database updated!')