# TD02 - Programmation Python
# Exercices sur les fonctions

import random
import math
#1 exos 

def majorite(prenom, age):
    print("Bonjour", prenom)
    if age < 18:
        print("Tu es mineur.")
    else:
        print("Tu es majeur.")


def volumeSphere(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume


def airePerimRect(longueur, largeur):
    aire = longueur * largeur
    perimetre = (longueur + largeur) * 2
    return aire, perimetre


def supprimElementsNegatifs(liste):
    resultat = []
    for element in liste:
        if element >= 0:
            resultat.append(element)
    return resultat




# DEbut de l'exos 
def demander_limites():
    while True:
        mini = int(input("Borne min : "))
        maxi = int(input("Borne max : "))
        if mini < maxi:
            return mini, maxi
        else:
            print("borne min inf a brone max.")


def tirer_nombre_mystere(mini, maxi):
    return random.randint(mini, maxi)


def demander_proposition(mini, maxi):
    while True:
        try:
            proposition = int(input("Proposez un nombre entre " + str(mini) + " et " + str(maxi) + " : "))
            if mini <= proposition <= maxi:
                return proposition
            else:
                print("Erreur : le nombre doit etre entre", mini, "et", maxi)
        except ValueError:
            print("Erreur : entrez un nombre entier valide.")


def analyser_proposition(proposition, secret):
    if proposition < secret:
        print("Trop petit")
        return -1
    elif proposition > secret:
        print("Trop grand")
        return 1
    else:
        print("C'est juste")
        return 0


def jouer_une_partie():
    # Demander les limites
    mini, maxi = demander_limites()
    
    # Tirer le nombre mystere
    secret = tirer_nombre_mystere(mini, maxi)
    
    # Boucle de jeu
    essais = 0
    resultat = -1
    
    while resultat != 0:
        proposition = demander_proposition(mini, maxi)
        resultat = analyser_proposition(proposition, secret)
        essais += 1
    
    print("Tu as trouve en", essais, "essais.")
    return essais


def demander_rejouer():
    while True:
        try:
            reponse = input("rejeouer ? (o ou n pour repondre) : ")
            if reponse.lower() == "o" :
                return True
            elif reponse.lower() == "n":
                return False
            else:
                print("Repondre par 'o' ou 'n'.")
        except ValueError:
            print("Repondre par 'o' ou 'n'.")



    
# ex 1
print("Ex 1")
majorite("bernidel hugo le goat", 17)
majorite("pzerbz", 25)

#  2
print("\nEx 2")
print("Volume d'une sphere de rayon 5 :", volumeSphere(5))

# 3
print("\nEx 3")
aire, perimetre = airePerimRect(10, 5)
print("Rectangle 10x5 : aire =", aire, ", perimetre =", perimetre)

# 4
print("\nEx 4")
liste_test = [3, -2, 7, -5, 0, -1, 8]
print("Liste originale :", liste_test)
print("Liste sans negatifs :", supprimElementsNegatifs(liste_test))

# ex5
print("\nLe jeu")
meilleur_score = None

# ex5
score = jouer_une_partie()
meilleur_score = score

# pour rejouerr
while demander_rejouer():
    score = jouer_une_partie()
    if score < meilleur_score:
        meilleur_score = score
        print("Nouveau record !")

print("Meilleur score :", meilleur_score, "essais")
print("Merci d'avoir joue !")

