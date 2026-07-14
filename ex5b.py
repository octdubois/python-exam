# 3b- modifier l'exercice 3a en utilisant une nouvelle classe Livre, il faut alors remplacer les #dictionnaires internes qui représentaient des livres par des objets de type Livre. Donc avant, on avait un #dictionnaire comme :

#{
#     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
#     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de #programmation"}
#}

#maintenant on essaie de remplacer les dictionnaires comme {"auteur":  "simon barette", "annee" : "1999", #"titre" : "bashar est beau" } par un objet de type Livre qui va contenir l'auteur et titre et annee.
class Livre:
    def __init__(self, titre: str, auteur: str, annee: str):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee


class Bibliotheque:
    def __init__(self, nom:str, addresse:str):
        self.nom = nom
        self.addresse = addresse
        self.dict_livres : dict[str,Livre] = {}
        #{
        #     "bashar est beau" : {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" },
        #     "complement de programmation" : {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
        #}
        # maintenant devient :
        #{
        #     "bashar est beau" : Livre(...)
        #     "complement de programmation" : Livre(...)
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
            self.dict_livres[titre] = Livre(titre=titre,auteur=auteur, annee=annee)  # {"auteurr": auteur, "annee": annee, "titre": titre}
    
    def afficher_livres(self):
        """
        methode qui affiche titre ,auteur et annee de tous les livres de la bibliotheque
        """
        #3 options pour traverser dicitonnaire:
        # self.dict_livres.items()
        # self.dict_livres.keys()
        # self.dict_livres.values()
        for livre in self.dict_livres.values():
            #dictionnaire_interne  va etre qqch comme :
            # {"auteur":  "simon barette", "annee" : "1999", "titre" : "bashar est beau" }
            # ou :
            # {"auteur": "bashar", "annee": "2025", "titre" : "complement de programmation"}
            titre =    livre.titre   #dictionnaire_interne["titre"] # "bashar est beau" 
            annee =    livre.annee   #dictionnaire_interne["annee"] # "1999"
            auteur =   livre.auteur   #dictionnaire_interne["auteur"] #"simon barette"
            print(f"titre: {titre};  auteur: {auteur}; annee: {annee}")

    def trouver_livre(self,titre:str):
        """
        Recherche un livre dans la bibliothèque en fonction de son titre et affiche ses détails
        (titre, auteur, annee).
        Si le livre n'existe pas, affiche un message indiquant qu'il n'est pas trouvé.
        """
        if titre in self.dict_livres:
            livre = self.dict_livres[titre]
            annee =  livre.annee  #dictionnaire_livre["annee"] # "1999"
            auteur = livre.auteur #dictionnaire_livre["auteur"] #"simon barette"
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