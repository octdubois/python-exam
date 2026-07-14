fichier = open("texte.txt", "r", encoding="utf-8")

contenu = fichier.read()

fichier.close()

print(contenu)