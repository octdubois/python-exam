# 2- Créer une classe Etudiant avec les attributs nom, age et notes
# (notes est une liste).
# Les notes sont des des notes sur 100.
# Créer une méthode qui permet
# d'ajouter une note à la liste de notes de l'étudiant
# (cette methode doit faire les validations
# necessaires), et une méthode qui permet de
# calculer la moyenne des notes de l'étudiant.

# Utiliser cette classe pour créer un programme simple de votre choix qui contient des étudiants
# qui ont des notes, par exemple vous pouvez donner des options a l'usager pour afficher, creer, enlever,
#  modifier des etudiants.

class Etudiant:
    def __init__(self,nom_param: str, age_param: int):
        self.nom = nom_param
        self.age = age_param
        # notes sur 100
        self.notes : list[int] = []

    def ajouter_note(self,nouvelle_note:int):
        if 0 < nouvelle_note and nouvelle_note < 100:
            self.notes.append(nouvelle_note)
        else:
            print("note doit etre entre 0 et 100")

    def calculer_moyenne(self):

        """
        methode qui calcule et retourne la moeynne des notes de l'etudiant.
        Si la liste de notes est vide, cette methode retourne la valeur -1 
        """
        if len(self.notes) == 0:
            return -1
        else:
            somme = 0
            for note in self.notes:
                somme = somme + note
            moyenne = somme / len(self.notes)
            return moyenne



etudiant1 = Etudiant("bashar",18)

moyenne_bashar = etudiant1.calculer_moyenne()
if moyenne_bashar == -1:
    print("aucune note!")
else:
    print(f"moyenne de bashar est {moyenne_bashar}")




etudiant2 = Etudiant("michel",30)
etudiant2.ajouter_note(100)
etudiant2.ajouter_note(7)
etudiant2.ajouter_note(90)

moyenne_michel = etudiant1.calculer_moyenne()
if moyenne_michel == -1:
    print("aucune note!")
else:
    print(f"moyenne de michel est {moyenne_michel}")

