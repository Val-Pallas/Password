"""Comparer les mots de passe afin de ne pas avoir 2 fois le même mot de passe
enregistré dans le fichier."""

import json

with open('job02_my_passwords.json') as f:
    data = json.load(f)

my_chaine = []
for i in data:
    allPassword = data[i]['my_password']
    if allPassword in my_chaine:
        print(allPassword , "two equals passwords!")
        break
    else:
        my_chaine.append(allPassword)
else:
    print("no repet object")



        
