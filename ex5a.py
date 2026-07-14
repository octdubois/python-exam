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
    def __init__(self, nom:str, addresse:str):
        self.nom = nom
        self.addresse = addresse
        self.dict_livres : dict[str,dict] = {}
        #{
        #     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
        #     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
        #}

    def ajouter_livre(self,titre:str, auteur:str, annee:str):
        """
        Ajoute un livre à la bibliothèque. Les titres sont uniques (titres vont etre
        les cles dans dictionnaire)
        """
        if titre == "":
            print("titre vide non-acceptee!")
        elif titre in self.dict_livres:
            print(f"titre {titre} existe deja, impossible de le rajouter!")
        else:
            # va inserer une entree comme:
            #  "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" }
            self.dict_livres[titre] = {"auteur": auteur, "annee": annee, "titre": titre}
    
    def afficher_livres(self):
        """
        methode qui affiche titre ,auteur et annee de tous les livres de la bibliotheque
        """
        #3 options pour traverser dicitonnaire:
        # self.dict_livres.items()
        # self.dict_livres.keys()
        # self.dict_livres.values()
        for dictionnaire_interne in self.dict_livres.values():
            #dictionnaire_interne  va etre qqch comme :
            # {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" }
            # ou :
            # {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
            titre = dictionnaire_interne["titre"] # "bashar est beau" 
            annee = dictionnaire_interne["annee"] # "1999"
            auteur = dictionnaire_interne["auteur"] #"simon barette"
            print(f"titre: {titre};  auteur: {auteur}; annee: {annee}")

    def trouver_livre(self,titre:str):
        """
        Recherche un livre dans la bibliothèque en fonction de son titre et affiche ses détails
        (titre, auteur, annee).
        Si le livre n'existe pas, affiche un message indiquant qu'il n'est pas trouvé.
        """
        if titre in self.dict_livres:
            dictionnaire_livre = self.dict_livres[titre]
            annee = dictionnaire_livre["annee"] # "1999"
            auteur = dictionnaire_livre["auteur"] #"simon barette"
            print(f"titre: {titre};  auteur: {auteur}; annee: {annee}")
        else:
            print(f"aucun livre avec le titre {titre}")


biblio = Bibliotheque(nom = "biblio de bashar", addresse="1970 rue montreal")

#{
#     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
#     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
#}

biblio.ajouter_livre(titre="bashar est beau",auteur="simon barette",annee="1999")
biblio.ajouter_livre(titre="complement de programmation" ,auteur="bashar",annee="2025")


print("\n-----------------------------\n")

biblio.afficher_livres()

print("\n-----------------------------\n")

biblio.trouver_livre("bashar est beau")

biblio.trouver_livre("bashar est laid")