"""● Il doit contenir au moins 8 caractères.
● Il doit contenir au moins une lettre majuscule.
● Il doit contenir au moins une lettre minuscule.
● Il doit contenir au moins un chiffre.
● Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).
● Voici comment votre programme devrait fonctionner :
1. Demandez à l'utilisateur de choisir un mot de passe.
2. Vérifiez si le mot de passe choisi respecte les exigences de sécurité.
3. Si le mot de passe est valide, affichez un message de confirmation et quittez le
programme.
4. Si le mot de passe n'est pas valide, affichez un message d'erreur et demandez à
l'utilisateur de choisir un nouveau mot de passe.
5. Répétez les étapes 2 à 4 jusqu'à ce que l'utilisateur choisisse un mot de passe
valide.
utilisez sha256() pour créer un objet de calcul d'empreinte avec l'algorithme SHA-256."""
import hashlib

def my_password():
    majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chiffres = '0123456789'
    caractere_special = '!@#$%^&*'

    while True:
        password = input("Entrez votre mot de passe: ")
        if len(password) < 8:
            print("Le mot de passe doit avoir au moins 8 caractères.")
        elif not any(char in majuscules for char in password):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(char in password for char in chiffres):
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not any(char in caractere_special for char in password):
            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            break
    
    hashed_password = sha256(password)
    print('Le mot de passe haché est:', hashed_password)

def sha256(string):
    hash_object = hashlib.sha256(string.encode('utf-8'))
    return hash_object.hexdigest()

my_password()
