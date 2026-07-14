# 1- Créer une classe Rectangle avec les attributs longueur et largeur.
# Ajouter des méthodes pour :
# Calculer l'aire.
# Calculer le périmètre.
# il faut utiliser cette classe pour creer des objets et tester les 2 methodes.
# il est preferable de documenter le code aussi.



# 2- Créer une classe Etudiant avec les attributs nom, age et notes (notes est une liste).
# Les notes sont des des notes sur 100.
# Créer une méthode qui permet
# d'ajouter une note à la liste de notes de l'étudiant (cette methode doit faire les validations
# necessaires), et une méthode qui permet de
# calculer la moyenne des notes de l'étudiant.
# Utiliser cette classe pour créer un programme simple de votre choix qui contient des étudiants
# qui ont des notes, par exemple vous pouvez donner des options a l'usager pour afficher, creer, enlever,
#  modifier des etudiants.


-----------------------------------

# 3a- Créez une classe Bibliothèque qui gère une collection de livres en utilisant un dictionnaire (donc 
# il n'y a pas de classe Livre pour le moment).
# Dans ce dictionnaire,la clé est le titre d'un livre et la valeur
# est un dictionnaire contenant le titre et l’auteur et l'année de publication du livre, on utilise alors un dicionnaire
# imbriqué. voici un exemple d'un tel dictionnaire une fois rempli:

#{
#     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
#     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
#}

# Implémentez les méthodes suivantes :

# ajouter_livre(titre, auteur, annee) : Ajoute un livre à la bibliothèque.

# afficher_livres() : Affiche la liste des livres avec leurs informations (titre, auteur, année).

# trouver_livre(titre) : Recherche un livre dans la bibliothèque en fonction de son titre et affiche ses #détails (titre, auteur, annee).
# Si le livre n'existe pas, affiche un message indiquant qu'il n'est pas trouvé.

#Le programme doit créer un objet de type Bibliotheque, puis utiliser ses 3 méthodes pour manipuler la #collection de
#livres comme vous voulez pour tester les fonctionnalités. Vous pouvez créer plusieurs objets Bibliotheque #si vous voulez représenter plusieurs bibliothèques dans le programme aussi.

#Commencez avec cette définition partielle de la classe:

class Bibliotheque:
    def __init__(self, nom, addresse):
        self.nom = nom
        self.addresse = addresse
        self.dict_livres = {}

-----------------------------------

# 3b- modifier l'exercice 3a en utilisant une nouvelle classe Livre, il faut alors remplacer les #dictionnaires internes qui représentaient des livres par des objets de type Livre. Donc avant, on avait un #dictionnaire comme :

#{
#     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
#     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de #programmation"}
#}

#maintenant on essaie de remplacer les dictoinnaires comme {"auteur":  "simon barette", "annee" : "1999", #"titre" : "bashar est beau" } par un objet de type Livre qui va contenir l'auteur et titre et annee.