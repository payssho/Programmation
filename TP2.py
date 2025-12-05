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