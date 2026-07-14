# 1- Écrire un programme qui permet d’effectuer la saisie d’un nom, d’un prénom
#  et affiche ensuite le nom complet. Créer une fonction qui prend le prénom et nom de famille comme arguments
#  et affiche le nom complet.

def affiche_nom_complet(prenom_param:str, nom_param: str):
    nom_complet = f"mon prenom est {prenom_param} et mon nom est {nom_param}"
    print(nom_complet)

prenom:str = input("entrez un  prenom: ")
nom:str = input("entrez un  nom: ")


affiche_nom_complet(prenom_param=prenom,nom_param=nom)