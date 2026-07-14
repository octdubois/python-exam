# Guide Extensif et Ultime pour l'Examen Pratique (Objectif : < 30 min)

Ce guide fournit des modèles détaillés (templates) classés par structures de données, concepts, et contient des **systèmes complets** (gestion, inventaire, recherche) que vous pouvez utiliser comme base pour votre examen.

---

## 🎯 1. Stratégie Globale pour l'Examen
1. **Lisez l'énoncé attentivement :** Identifiez les variables (Listes pour stocker, Dictionnaires pour associer/compter, Classes pour des objets complexes).
2. **Utilisez le modèle de Menu Interactif (`while True`) :** Presque tous les examens demandent un programme qui tourne en boucle.
3. **Faites des fonctions :** Sortez la logique complexe (ex: validation, recherche) en dehors du `while True`.
4. **Validez toujours :** Vérifiez si un élément existe avant de l'ajouter (pour éviter les doublons) ou avant de le supprimer.

---

## 🌟 2. Le Menu Interactif Standard (`while True`)

C'est la base de tout programme d'examen interactif.

```python
# TOUJOURS initialiser les structures AVANT la boucle
donnees_systeme = []

def afficher_menu():
    print("\n--- Menu Principal ---")
    print("1- Afficher les données")
    print("2- Ajouter une donnée")
    print("q- Quitter")

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        # Appeler fonction affichage
        pass
    elif choix == "2":
        # Appeler fonction ajout
        pass
    elif choix.lower() == "q" or choix == "":
        print("Fin du programme.")
        break
    else:
        print("Erreur : Choix invalide.")
```

---

## 🚀 3. Systèmes Complets Recommandés

Voici des systèmes typiques demandés en examen. Adaptez-les selon le contexte.

### 3.1 Système de Gestion de Contacts (Dictionnaire)
**Idéal pour :** Associer deux informations (Nom -> Numéro de téléphone) ou (Code -> Produit).

```python
def ajouter_contact(contacts, nom, numero):
    if nom in contacts:
        print(f"Erreur : '{nom}' existe déjà avec le numéro {contacts[nom]}.")
    elif numero == "":
        print("Erreur : Le numéro ne peut pas être vide.")
    else:
        contacts[nom] = numero
        print(f"Contact {nom} ajouté.")

def chercher_contact(contacts, nom):
    if nom in contacts:
        print(f"Le numéro de {nom} est {contacts[nom]}.")
    else:
        print(f"Erreur : '{nom}' n'existe pas.")

def supprimer_contact(contacts, nom):
    if nom in contacts:
        del contacts[nom]
        print(f"Contact '{nom}' supprimé.")
    else:
        print("Erreur : Contact introuvable.")

# Initialisation
mes_contacts = {}
```

### 3.2 Système d'Inventaire (Dictionnaire + Mise à jour)
**Idéal pour :** Gérer des quantités, compter des fréquences.

```python
def ajouter_stock(inventaire, produit, quantite):
    if produit in inventaire:
        inventaire[produit] += quantite # Ajoute à la quantité existante
    else:
        inventaire[produit] = quantite  # Crée le produit
    print(f"Nouveau stock de {produit} : {inventaire[produit]}")

def retirer_stock(inventaire, produit, quantite):
    if produit not in inventaire:
        print("Erreur : Produit inexistant.")
    elif inventaire[produit] < quantite:
        print("Erreur : Stock insuffisant.")
    else:
        inventaire[produit] -= quantite
        print(f"Retrait réussi. Stock restant : {inventaire[produit]}")

# Initialisation
mon_inventaire = {"pomme": 10, "banane": 5}
```

### 3.3 Système de Recherche et de Filtrage (Listes)
**Idéal pour :** Extraire des données spécifiques d'une liste selon des conditions.

```python
def chercher_noms_longs(liste_noms, longueur_minimum):
    """Trouve et retourne tous les noms plus longs qu'une certaine taille."""
    resultats = []
    for nom in liste_noms:
        if len(nom) > longueur_minimum:
            resultats.append(nom)

    if len(resultats) == 0:
        print("Aucun nom ne correspond au critère.")
    else:
        print(f"{len(resultats)} noms trouvés :")
        for res in resultats:
            print(f"- {res}")
    return resultats

def verifier_presence(liste, element):
    """Vérifie si un élément précis est dans la liste."""
    if element in liste:
        print(f"Oui, '{element}' est présent.")
        return True
    else:
        print(f"Non, '{element}' est absent.")
        return False

# Initialisation
liste_etudiants = ["Alex", "Beatrice", "Charles", "Diana"]
```

### 3.4 Système Scolaire / Gestion d'Étudiants (Programmation Orientée Objet)
**Idéal pour :** Les questions nécessitant des classes (Classes imbriquées ou listes dans des objets).

```python
class Etudiant:
    def __init__(self, nom, matricule):
        self.nom = nom
        self.matricule = matricule
        self.notes = [] # Liste interne à l'objet

    def ajouter_note(self, note):
        if 0 <= note <= 100:
            self.notes.append(note)
            print(f"Note {note} ajoutée pour {self.nom}.")
        else:
            print("Erreur : La note doit être entre 0 et 100.")

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        total = sum(self.notes)
        return total / len(self.notes)

    def __str__(self):
        # La méthode magique pour l'affichage (Très demandé par le prof)
        return f"Étudiant: {self.nom} ({self.matricule}) - Moyenne: {self.calculer_moyenne():.2f}"

# Exemple d'utilisation du système POO
etudiant1 = Etudiant("Alice", "12345")
etudiant1.ajouter_note(85)
etudiant1.ajouter_note(90)
print(etudiant1) # Affiche: Étudiant: Alice (12345) - Moyenne: 87.50
```

### 3.5 Système Bancaire (POO)
**Idéal pour :** Les objets qui interagissent (retrait, dépôt, virements).

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} réussi. Nouveau solde : {self.solde}")
        else:
            print("Erreur : Le montant doit être positif.")

    def retirer(self, montant):
        if montant <= 0:
            print("Erreur : Le montant doit être positif.")
        elif montant > self.solde:
            print("Erreur : Fonds insuffisants.")
        else:
            self.solde -= montant
            print(f"Retrait de {montant} réussi. Nouveau solde : {self.solde}")

    def __str__(self):
        return f"Compte de {self.titulaire} : {self.solde} $"
```

---

## 🔍 4. Algorithmes Classiques (Copier-Coller)

### 4.1 Compter l'occurrence des mots dans une phrase
Ceci est une question d'examen classique (comme dans vos exercices).

```python
phrase = input("Entrez une phrase : ")
liste_mots = phrase.split()
dict_compte_mots = {}

for mot in liste_mots:
    if mot in dict_compte_mots:
        dict_compte_mots[mot] += 1
    else:
        dict_compte_mots[mot] = 1

for cle, valeur in dict_compte_mots.items():
    print(f"Le mot '{cle}' est présent {valeur} fois.")
```

### 4.2 Trouver la valeur Maximum / Minimum sans fonction pré-intégrée
Au cas où on vous demande de le faire manuellement avec une boucle `for`.

```python
liste_nombres = [12, 45, 2, 88, 34]

# Recherche du Maximum
max_actuel = liste_nombres[0] # On commence par le premier élément
for nb in liste_nombres:
    if nb > max_actuel:
        max_actuel = nb
print(f"Le maximum est {max_actuel}")
```

### 4.3 Valider une entrée utilisateur complexe (Ex: Adresse IP)
```python
def valider_ip(n1, n2, n3, n4):
    try:
        # Convertir en entier d'abord
        n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
        if (0 <= n1 <= 255) and (0 <= n2 <= 255) and (0 <= n3 <= 255) and (0 <= n4 <= 255):
            return f"{n1}.{n2}.{n3}.{n4}"
        else:
            return None
    except ValueError:
        # L'utilisateur a entré des lettres au lieu de chiffres
        return None
```
