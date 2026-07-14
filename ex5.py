# ex4:

# Écrire un programme qui utilise un dictionnaire pour maintenir le nombre de points de joueurs.
#
# Le dictionnaire doit commencer avec:
# - "bashar" avec 10 points
# - "leo" avec 8 points
# - "sara" avec 12 points
#
# Le programme doit:
# - demander le nom d'un joueur.
# - si le joueur existe, augmenter ses points de 1. sinon, inserer ce joueur avec 1 point.
# - afficher tous les joueurs et leurs points, chacun avec un message complet comme:
#    le jour bashar a 10 points
# (pas besoin de boucle ici, le programme accomplit ces tâches dans l'ordre demandée puis se termine )

dict_nombre_points = {
    "bashar":10,
    "leo": 8,
    "sara":12
}

nom_joueur:str = input("entrez un nom de joueur pour augmenter ses points de 1 ou l'inserer s'il n'est pas deja la: ")

if nom_joueur in dict_nombre_points:
    #augmenter le nombre de points existans du joueur (+1)
    nombre_points_actuels =  dict_nombre_points[nom_joueur]
    dict_nombre_points[nom_joueur] = nombre_points_actuels + 1
    print(f"le joueur {nom_joueur} a maintenant {nombre_points_actuels + 1} points")
else:
    dict_nombre_points[nom_joueur] = 1
    print(f"le joueur {nom_joueur} a ete insere avec 1 point!")


# - afficher tous les joueurs et leurs points, chacun avec un message complet comme:
#    le jour bashar a 10 points

print("\nliste des joueurs avec leurs points: ")
for joueur,points in dict_nombre_points.items():
    print(f"le jour {joueur} a {points} points")