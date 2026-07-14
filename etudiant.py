class Cours:
    def __init__(self, code, titre):
        self.code = code
        self.titre = titre
        self.etudiants_inscrits = []

    def inscrire_etudiant(self, etudiant):
        self.etudiants_inscrits.append(etudiant)

    def __str__(self):
        return f"Code : {self.code}, Titre : {self.titre}"