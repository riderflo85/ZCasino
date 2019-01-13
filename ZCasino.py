#! /usr/bin/env python3.7
# coding: utf-8
import random
import math


# Booléen qui reste vrai tant qu'on continue la partie et tant qu'il y a de l'argent en banque
continuer_partie = True 

# Demander la somme à déposer pour jouer (input)
argent_en_banque = input("Bonjour et bienvenu à la roulette. Veuillez indiquer la somme que vous voulez placer en banque : ")

# Vérifie qu'il s'agit bien d'un nombre
try:
    argent_en_banque = int(argent_en_banque)
except ValueError:
    print("Vous n'avez pas saisi de nombre : ")
# Vérifie si la somme est supérieur à 0
if argent_en_banque < 0 or argent_en_banque == 0:
    print("Veuillez saisir un nombre positif")

if argent_en_banque > 0:
    argent_en_banque = argent_en_banque


# Boucle principal pour pouvoir jouer tant qu'il y a de l'argent
while continuer_partie:
    
    # Pour créer la condition de la boucle qui suit
    nombre_mise = -1
    # Boucle qui demande au joueur de miser un nombre. Tant que la mise n'est pas comprise entre le nombre 0 et 49 (cela évite de mettre beaucoup de if et else)
    while nombre_mise < 0 or nombre_mise > 49:
        # Demande sur quelle nombre miser (input)
        nombre_mise = input("Veuillez saisir un nombre compris entre 0 et 49 pour miser desssus : ")
        # Vérifie que le nombre est compris entre 0 et 49 (bloc try: except:)  /  Convertion du input (donc str) en int
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre : ")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Vous avez saisi un nombre négatif")
        if nombre_mise > 49:
            print("Vous avez saisi un nombre supérieur à 49")

    # Boucle qui demande de miser une somme d'argent. Tant que la somme est égal à 0 ou supérieur à la somme de la banque
    somme_mise = 0
    while somme_mise <= 0 or somme_mise > argent_en_banque:
        # Demande la somme à miser (input)
        somme_mise = input("Veuillez définir la somme à miser : ")
        # Vérifie que la somme est compris entre 0 la somme de la banque (bloc try: except:)  /  Convertion du input (donc str) en int
        try:
            somme_mise = int(somme_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre : ")
            somme_mise = -1
            continue
        if somme_mise < 0:
            print("Votre mise est une somme négative")
        if somme_mise > argent_en_banque:
            print("Votre mise est impossible car elle est supérieur à votre crédit qui est de ", argent_en_banque, "$")
    
    # Tirage au "hasard" d'un nombre compris entre 0 et 50
    nb_gagnant = random.randrange(50)
    print("La roulette tourne... ... ... et le numéro gagnant est ... ", nb_gagnant)

    # Établissement des gains
    if nb_gagnant == nombre_mise:
        print("Félicitation, vous avez gagner : ", somme_mise * 3, " $")
        # Incrémentation de la somme en banque part les gains
        argent_en_banque += somme_mise * 3
    # Si numéro de la même couleur
    elif nb_gagnant % 2 == nombre_mise % 2:
        # Arrondissement du numéro au supérieur
        somme_mise = math.ceil(somme_mise * 0.5)
        print("Vous avez miser sur la bonne couleur, vous gagner : ", somme_mise, " $")
        argent_en_banque += somme_mise
    else:
        print("Vous avez perdu votre mise")
        argent_en_banque -= somme_mise
    
    # Si il y a plus d'argent en banque, fin de la parti
    if argent_en_banque <= 0:
        print("Vous avez plus d'argent en banque, la parti est fini")
        continuer_partie = False
    else:
        # Demander si le joeur veut quitter la partie (input)
        print("Vous avez ", argent_en_banque, " $ en banque !")
        quitter = input("Voulez-vous quitter la partie?  (o/n) :")
        if quitter == "o" or quitter == "O" or quitter == "oui":
            print("À bientôt ! :)")
            continuer_partie = False