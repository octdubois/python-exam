personne : dict = { }
# dict initialisé avec quelques paires de clé et valeur
personne = {
    "nom": "Alice", # chaque clé
    "âge": 30,
    "ville": "Montréal",
    1 : "string associé à la clé 1",
}

nom_lu_du_dictionnaire = personne["nom"]
print(f"le nom trouve est {nom_lu_du_dictionnaire}")

personne["nom"] = "nouvelle valeur de la cle nom!"
personne["Date_naissance"] = "2 octobre"
print(personne)

# Pour vérifier si une clé existe, par exemple 'ville', on utilise l'opérateur 'in': 
if "cle qui n'existe pas" in personne:
    print("Clé 'cle qui n'existe pas' présente")
else:
    print("Clé 'cle qui n'existe pas' non-présente")

