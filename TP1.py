#TP1
def majorite(prenom, age):
    if prenom == "Mathieu" :
        print("Moi tu m'parles pas d'age")
    print("Bonjour " + prenom)
    if age < 18:
        print("Tu es mineur")
    else:
        print("Tu es périmé")

majorite("Hugo", 18)