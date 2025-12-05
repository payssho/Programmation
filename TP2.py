#Les listes de liste
table1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(table1)):
    for j in range(len(table1[i])):
        if i == 2 and j == 3:
            print(table1[i][j])
            table1[i][j] = 6
        print("Valeur actuelle", table1[i][j])

#Tuples
tuple1 = (1, 4, 5, 2, "f", 2.5)
print(tuple1[1])
liste1 = list(tuple1)
liste1[2] = 12
tuple1 = tuple(liste1)

#Dictionnaires
dictionnaire1 = {"nom": "DUrand", "age": 20, "ville": "Albi"}
dictionnaire1["num"] = "06 51 89 67 16"
del dictionnaire1["age"]
print(dictionnaire1)

#Début du TP
for i in range(1, 11):
    print(9, "*", i, "=", 9 * i)

def tailleArbre(année):
    return 30 + 14 * année

print(tailleArbre(8))

def pyramideBille(hauteur):
    total = 0
    for i in range(1, hauteur + 1):
        total += i * i
    return total

print(pyramideBille(100))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

def nbOccurence(phrase, lettre):
    total = 0
    for i in range(len(phrase)):
        if phrase[i] == lettre:
            total += 1
    return total

print(nbOccurence("y que fe", "e"))

def calcDiviseurs():
    input1 = int(input("Entrez un nombre : "))
    for i in range(1, input1 + 1):
        if input1 % i == 0:
            print(i)

calcDiviseurs()

from random import randint
#Quizz magique
def quizzMagique():
    while True:
        try:
            input2 = int(input("Entrez un nombre de questions a poser : "))
            if input2 > 0:
                break  # Sort de la boucle si c'est un nombre valide > 0
            else:
                print("Erreur : entrez un nombre supérieur à 0 !")
        except ValueError:
            print("Erreur : entrez un nombre entier !")
    bonnesReponses = 0
    for i in range(1, input2 + 1):
        random1 = randint(1, 100)
        random2 = randint(1, 100)
        print("Question", i, ":", random1, "+", random2, "=")
        while True:
            try:
                input3 = int(input("Entrez la réponse : "))
                break
            except ValueError:
                print("Erreur : entrez un nombre entier !")
        if input3 == random1 + random2:
            print("Correct !")
            bonnesReponses += 1
        else:
            print("Faux, la bonne réponse est", random1 + random2)
    
    # Résultats finaux
    pourcentage = (bonnesReponses / input2) * 100
    print("\n--- Résultats ---")
    print("Bonnes réponses :", bonnesReponses, "/", input2)
    print("Pourcentage de réussite :", pourcentage, "%")

    if pourcentage >= 80:
        print("Excellent ! Bravo !")
    elif pourcentage >= 50:
        print("Pas mal, tu peux faire mieux !")
    else:
        print("Il faut réviser...")
    
    return pourcentage

# Menu principal
meilleurScore = 0

while True:
    score = quizzMagique()
    
    if score > meilleurScore:
        meilleurScore = score
        print("Nouveau record !")
    
    print("\n1. Rejouer")
    print("2. Meilleur score")
    print("3. Quitter")
    choix = input("Choix : ")
    
    if choix == "1":
        pass
    elif choix == "2":
        print("Meilleur score :", meilleurScore, "%")
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide")