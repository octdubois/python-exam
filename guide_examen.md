# Guide Extensif et Ultime pour l'Examen Pratique (Objectif : < 30 min)

Ce guide fournit des modèles détaillés (templates) classés par structures de données et par concepts. Il contient les **explications, les bonnes pratiques** et des **systèmes complets** prêts à être adaptés à votre examen.

---

## 🎯 Stratégie Globale pour l'Examen
1. **Lisez l'énoncé attentivement :** Identifiez les structures (Listes pour stocker, Dictionnaires pour associer/compter, Classes pour des objets complexes).
2. **Utilisez le modèle de Menu Interactif (`while True`) :** Presque tous les examens demandent un programme qui tourne en boucle.
3. **Faites des fonctions :** Sortez la logique complexe (ex: validation, recherche) en dehors du `while True`.
4. **Validez toujours :** Vérifiez si un élément existe avant de l'ajouter (pour éviter les doublons) ou avant de le supprimer.

---

## 🌟 Le Menu Interactif Standard (`while True`)

**Quand l'utiliser :** Dès qu'un exercice demande un programme qui "roule en continu" ou donne des choix à l'usager.

```python
# TOUJOURS initialiser les structures AVANT la boucle
donnees_systeme = []
mon_dictionnaire = {}

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
        break # <-- Essentiel pour sortir de la boucle
    else:
        print("Erreur : Choix invalide.")
```

---

## 1. 📦 Les Listes (`[]`)

**Quand l'utiliser :** Pour stocker une collection ordonnée d'éléments simples (ex: un historique de noms, une liste d'adresses IP créées, une liste de nombres).
**Bonnes pratiques :**
- Toujours vérifier les doublons avant l'ajout avec `if element in liste:` (sauf si on veut explicitement garder des doublons).
- Utiliser `len(liste)` pour vérifier si la liste est vide avant d'afficher.

### Système 1.1 : Recherche, Filtrage et Gestion de base
**Idéal pour :** Extraire des données spécifiques d'une liste selon des conditions (ex: noms longs).

```python
liste_etudiants = ["Alex", "Beatrice", "Charles", "Diana"]

def ajouter_a_la_liste(liste, nouvel_element):
    """Ajoute un élément avec validation (pas vide, pas de doublon)."""
    if nouvel_element == "":
        print("Erreur : Impossible d'ajouter un élément vide.")
    elif nouvel_element in liste:
        print(f"Erreur : L'élément '{nouvel_element}' existe déjà.")
    else:
        liste.append(nouvel_element)
        print(f"Succès : '{nouvel_element}' a été ajouté!")

def chercher_noms_longs(liste_noms, longueur_minimum):
    """Trouve et affiche tous les noms plus longs qu'une certaine taille."""
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
```

### Algorithme : Trouver Maximum / Minimum manuellement
```python
liste_nombres = [12, 45, 2, 88, 34]

max_actuel = liste_nombres[0] # On commence par le premier élément
for nb in liste_nombres:
    if nb > max_actuel:
        max_actuel = nb
print(f"Le maximum est {max_actuel}")
```

---

## 2. 📖 Les Dictionnaires (`{}`)

**Quand l'utiliser :** Quand vous devez associer deux données liées (Clé -> Valeur), ou quand vous devez COMPTER le nombre d'apparitions d'éléments (fréquence).
**Bonnes pratiques :**
- Toujours vérifier l'existence de la clé avant de lire ou supprimer : `if cle in dictionnaire:`.
- Pour ajouter ou mettre à jour, utiliser simplement `dictionnaire[cle] = nouvelle_valeur`.

### Système 2.1 : Gestion de Contacts (Association Clé -> Valeur)
**Idéal pour :** Associer deux informations uniques (Nom -> Numéro) ou (Code -> Produit).

```python
mes_contacts = {}

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
```

### Système 2.2 : Inventaire et Comptage (Fréquence)
**Idéal pour :** Gérer des quantités (ajouter/retirer du stock) ou compter des occurrences.

```python
mon_inventaire = {"pomme": 10, "banane": 5}

def ajouter_stock(inventaire, produit, quantite):
    if produit in inventaire:
        inventaire[produit] += quantite # Ajoute à la quantité existante
    else:
        inventaire[produit] = quantite  # Crée le produit à cette quantité
    print(f"Nouveau stock de {produit} : {inventaire[produit]}")

def retirer_stock(inventaire, produit, quantite):
    if produit not in inventaire:
        print("Erreur : Produit inexistant.")
    elif inventaire[produit] < quantite:
        print("Erreur : Stock insuffisant.")
    else:
        inventaire[produit] -= quantite
        print(f"Retrait réussi. Stock restant : {inventaire[produit]}")
```

### Algorithme : Compter l'occurrence des mots dans une phrase
```python
phrase = "chat chien chat oiseau chien chat"
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

---

## 3. ⚙️ Les Fonctions (`def`)

**Pourquoi l'utiliser :** Pour nettoyer le code du `while True` (souvent exigé pour des points partiels).
**Bonnes pratiques :**
- **Passage par référence :** Quand vous passez une Liste ou un Dictionnaire à une fonction et que vous le modifiez dedans, l'objet original est modifié. Pas besoin de faire de `return`.
- **Utiliser `return` pour les validations :** Séparez la logique de validation de l'affichage.

### Algorithme : Valider une entrée utilisateur complexe (Ex: IP)
```python
def valider_ip(n1, n2, n3, n4):
    """Retourne l'adresse formatée si valide, sinon None."""
    try:
        n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
        if (0 <= n1 <= 255) and (0 <= n2 <= 255) and (0 <= n3 <= 255) and (0 <= n4 <= 255):
            return f"{n1}.{n2}.{n3}.{n4}"
        else:
            return None
    except ValueError:
        return None # Cas où l'usager a entré des lettres

# Utilisation:
# ip = valider_ip(192, 168, 0, 1)
# if ip is not None:
#    liste_ip.append(ip)
```

---

## 4. 🧬 Programmation Orientée Objet (Classes)

**Quand l'utiliser :** Quand le problème décrit des "choses" qui ont plusieurs caractéristiques spécifiques (ex: Une Auto a une marque et une année, un Étudiant a un code et des notes).
**Bonnes pratiques :**
- Le professeur demande presque toujours la méthode magique `__str__` pour gérer l'affichage avec un `print(objet)`.

### Système 4.1 : Système Scolaire / Gestion (Objet contenant une liste)
**Idéal pour :** Les entités qui possèdent une liste interne de données (comme des notes, des employés, etc.).

```python
class Etudiant:
    def __init__(self, nom, matricule):
        self.nom = nom
        self.matricule = matricule
        self.notes = [] # Liste interne initialisée à vide

    def ajouter_note(self, note):
        if 0 <= note <= 100:
            self.notes.append(note)
            print(f"Note {note} ajoutée pour {self.nom}.")
        else:
            print("Erreur : La note doit être entre 0 et 100.")

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    def __str__(self):
        return f"Étudiant: {self.nom} ({self.matricule}) - Moyenne: {self.calculer_moyenne():.2f}"

# Utilisation
etudiant1 = Etudiant("Alice", "12345")
etudiant1.ajouter_note(85)
etudiant1.ajouter_note(90)
print(etudiant1)
```

### Système 4.2 : Système Bancaire (Objet avec interactions mathématiques)
**Idéal pour :** Les objets dont l'état change via des opérations (dépôt, retrait).

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt réussi. Nouveau solde : {self.solde}")
        else:
            print("Erreur : Le montant doit être positif.")

    def retirer(self, montant):
        if montant <= 0:
            print("Erreur : Le montant doit être positif.")
        elif montant > self.solde:
            print("Erreur : Fonds insuffisants.")
        else:
            self.solde -= montant
            print(f"Retrait réussi. Nouveau solde : {self.solde}")

    def __str__(self):
        return f"Compte de {self.titulaire} : {self.solde} $"
```
