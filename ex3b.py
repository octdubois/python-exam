# 1- Créer une classe Rectangle avec les attributs longueur et largeur.
# Ajouter des méthodes pour :
# Calculer l'aire.
# Calculer le périmètre.
# il faut utiliser cette classe pour creer des objets et tester les 2 methodes.
# il est preferable de documenter le code aussi.

class Rectangle:
    def __init__(self, longueur_param: float , largeur_param : float):
        self.longeur:float = longueur_param
        self.largeur:float = largeur_param
        # ici finit la definition de la methode __init__

    def calculer_aire(self) -> float:
        """
        methode qui calcule et retourne l'aire de ce rectangle
        """
        aire = self.longeur * self.largeur
        return aire
    
    def calculer_perimetre(self) -> float:
        """
        methode qui calcule et retourne le perimetre de ce rectangle
        """
        perimetre = 2 * (self.longeur + self.largeur)
        return perimetre
    
    def changer_longueur(self,nouvelle_longueur: float):
        self.longeur = nouvelle_longueur

    def __str__(self):
        resultat = f"rectangle avec longueur : {self.longeur} et largeur : {self.largeur}"
        return resultat
    
# ici la definiotn de la classe est terminee parce qu'on revient 
# a 0 espaces vides

rec1 = Rectangle(longueur_param=10,largeur_param=5)
rec2 = Rectangle(longueur_param=10,largeur_param=5)
rec3 = Rectangle(longueur_param=10,largeur_param=5)
rec4 = Rectangle(longueur_param=10,largeur_param=5)
rec5 = Rectangle(longueur_param=10,largeur_param=5)
rec6 = Rectangle(longueur_param=10,largeur_param=5)
rec7 = Rectangle(longueur_param=10,largeur_param=5)
rec8 = Rectangle(longueur_param=10,largeur_param=5)

aire_rec1 = rec1.calculer_aire()
print(f"l'aire de rectangle 1 est {aire_rec1}")

# pour changer longeur du rectangle 1 :
rec1.longeur = 20
# OU
rec1.changer_longueur(20)

aire_rec1 = rec1.calculer_aire()
print(f"l'aire de rectangle 1 est {aire_rec1}")


aire_rec2 = rec2.calculer_aire()
print(f"l'aire de rectangle 2 est {aire_rec2}")