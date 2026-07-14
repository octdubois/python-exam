class Chien:
    """
    classe qui represente un chien
    """
    def __init__(self, nom_donne: str, race_choisi: str,couleur_choisi:str,sexe_donne:str, age_donne: float):
        self.nom = nom_donne
        self.race = race_choisi
        self.couleur = couleur_choisi
        self.sexe = sexe_donne
        self.age = age_donne

    def courir(self):
        print(f"{self.nom} est en train de courir!!")

    def calculer_prix(self):
        """
        methode qui permet de calculer un prixe pour un chien en fonction de l'age
        et race et couleur
        """
        if self.age < 1:
            return 3000
        elif self.race == "chiwawa" and self.couleur == "roux":
            return 6000
        else:
            return 1000
        
    def changer_couleur(self,nouvelle_couleur):
        self.couleur = nouvelle_couleur

    def est_vieux(self):
        return self.age > 3
    
    def anniversaire(self):
        """
        methode qui augment l'age d'un chien de 1 an
        """
        self.age = self.age + 1

    #def __str__(self):
    #    return f"chien {self.nom} a {self.age} ans!"


max = Chien("max", "pitbull" ,"noir","M",1)
minou = Chien("minou", "chiwawa" ,"roux","M",2)
marc = Chien("marc", "pitbull" ,"noir","M",1)
bashar = Chien("bashar", "chiwawa" ,"roux","M",4)

print(max)

max.courir()

prix_max = max.calculer_prix()
print(f"prix de max est: {prix_max}")

# pour changer la valeur d'un attribut comme la couleur de max ici :
# maniere simple: 
max.couleur = "blanc"
# ou la maniere plus 'professionnelle' avec une methode qui contient la logique
# de modification:
max.changer_couleur("blanc")


print(f"prix de minou est: {minou.calculer_prix()}")


liste_chiens = [max,minou,marc,bashar ]

for chien in liste_chiens:
    if chien.age > 3:
    # ou:
    #if chien.est_vieux(): 
        print(f"{chien.nom} est vieux!")