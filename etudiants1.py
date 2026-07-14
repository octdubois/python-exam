class CompteUtilisateur:
    def __init__(self, nom_donne: str, role_donne: str):
        self.nom = nom_donne
        self.role = role_donne # exemple: admin, assistant
        self.actif = True
        self.permissions = [] # exemples: "lire base donnees", "modifier acces"
    
    def __str__(self):
        return f"usager {self.nom} avec un role {self.role}, actif = {self.actif}"
    
    def activer_compte(self):
        self.actif = True
        
    
    def desactiver_compte(self):
        if self.actif:
            self.actif = False
            print(f"desactiver_compte: le compte de {self.nom} est maintenant desactive")
        else:
            print(f"desactiver_compte: le compte de {self.nom} est deja desactive")

compte1 = CompteUtilisateur("bashar","admin")
# compte1 est cree avec actife = True par defaut
print(compte1)

compte1.desactiver_compte()
print(compte1)

compte1.activer_compte()
print(compte1)