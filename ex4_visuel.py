# ex2:

# Écrire un programme qui utilise un dictionnaire pour garder les notes de 4 étudiants.
#
# Le dictionnaire doit contenir:
# - "alice" avec la note 85
# - "bob" avec la note 72
# - "charlie" avec la note 90
# - "diana" avec la note 68
#
# Le programme doit:
#  -afficher la note de bob
#  -afficher la note de diana
#  -demander un nom à l'usager: si le nom existe dans le dictionnaire, afficher sa note. Sinon, afficher un message qui dit que cet étudiant n'existe pas.
# (pas besoin de boucle ici, le programme accomplit ces tâches dans l'ordre demandée puis se termine )

dict_notes = {
    "alice": 85,
    "bob": 72,
    "charlie": 90,
    "diana": 68
}

note_bob = dict_notes["bob"]
note_diana = dict_notes["diana"]

print(f"bob a la note {note_bob}")
print(f"diana a la note {note_diana}")

nom_choisi = input("entrez un nom pour voir sa note: ")

if nom_choisi in dict_notes:
    note_de_letudiant_choisi = dict_notes[nom_choisi]
    print(f"letudiant {nom_choisi} a la note: {note_de_letudiant_choisi}")
else:
    print(f"l'etudiant {nom_choisi} n'existe pas!")