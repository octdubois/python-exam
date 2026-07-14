class etudiant:
    def __init__(self, nom_etudiant: str, code_etudiant: str):
        self.nom = nom_etudiant
        self.code = code_etudiant
        self.noms_cours_inscrits = ["algorithmie", "gestion serveurs"]
    
    def nom_contient_charactere(self,character : str):
        if character in self.nom:
            return True
        else:
            return False
        
    def nom_majuscsule(self):
        nom_majuscule = self.nom.upper()
        return nom_majuscule
    
    def nombre_cours_insecrits(self):
        return len(self.noms_cours_inscrits)



etudiant1 = etudiant(nom_etudiant="bashar1",code_etudiant="eb08_1")
etudiant2 = etudiant(nom_etudiant="bashar2",code_etudiant="eb08_2")
etudiant3 = etudiant(nom_etudiant="bashar3",code_etudiant="eb08_3")

nombre_cours_etuidiant1 = etudiant1.nombre_cours_insecrits()
print(nombre_cours_etuidiant1)

liste_chaipasquoi = []

dict_etudiants = { 
    "eb08_1" : etudiant1,
    "eb08_2" : etudiant2,
    "eb08_3" : etudiant3
}

etudiant1_lu = dict_etudiants["eb08_1"]

print(etudiant1_lu.nom)
print(etudiant1_lu.code)

phrase = "chat chien chai pa quoi"
phrase.split()

list_etudiants = []
list_etudiants.append(etudiant1)
list_etudiants.append(etudiant2)