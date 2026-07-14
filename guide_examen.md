# Guide Extensif et Ultime pour l'Examen Pratique (Objectif : < 30 min)

Ce guide fournit des modèles détaillés (templates) classés par structures de données et par concepts. Il contient les **explications, les bonnes pratiques** et des **systèmes complets** (incluant des notions avancées vues en classe) prêts à être adaptés à votre examen.

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

### Système 2.2 : Dictionnaires Imbriqués (Avancé)
**Idéal pour :** Stocker plusieurs informations pour une même clé (ex: Gestion d'une Bibliothèque).

```python
# Clé = Titre du livre, Valeur = Dictionnaire d'informations
bibliotheque = {
    "Harry Potter": {"auteur": "J.K. Rowling", "annee": 1997},
    "Le Petit Prince": {"auteur": "Antoine de Saint-Exupéry", "annee": 1943}
}

def ajouter_livre(biblio, titre, auteur, annee):
    if titre in biblio:
        print("Ce livre existe déjà.")
    else:
        biblio[titre] = {"auteur": auteur, "annee": annee}
        print(f"Livre '{titre}' ajouté.")

def afficher_livres(biblio):
    for titre, infos in biblio.items():
        print(f"Titre: {titre} | Auteur: {infos['auteur']} | Année: {infos['annee']}")
```

### Système 2.3 : Inventaire et Comptage (Fréquence)
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

---

## 3. ⚙️ Les Fonctions et Manipulation de Chaînes (`def` & `Strings`)

**Pourquoi l'utiliser :** Pour nettoyer le code du `while True` (souvent exigé pour des points partiels).
**Bonnes pratiques :**
- Ne **JAMAIS** utiliser une variable globale à l'intérieur d'une fonction sans la passer en paramètre.
- **Passage par référence :** Quand vous passez une Liste ou un Dictionnaire à une fonction et que vous le modifiez dedans, l'objet original est modifié. Pas besoin de faire de `return`.

### Manipulation de Chaînes (Strings)
Souvent utile pour nettoyer les entrées de l'utilisateur ou manipuler des textes.

```python
# 1. Diviser une phrase en liste de mots
phrase = "chat chien oiseau"
liste_mots = phrase.split() # Devient: ["chat", "chien", "oiseau"]

# 2. Convertir en minuscules (Très utile pour éviter les erreurs de casse)
entree = input("Entrez un nom : ").lower().strip() # " ALiCe " devient "alice"
```

### Algorithme : Valider une entrée utilisateur complexe (Gestion d'Exceptions)
**Idéal pour :** S'assurer que le programme ne plante pas si l'usager entre des lettres au lieu de chiffres.

```python
def demander_nombre_entier():
    """Demande un nombre jusqu'à ce que l'usager entre un entier valide."""
    while True:
        try:
            valeur = int(input("Entrez un nombre entier : "))
            return valeur # Si ça fonctionne, on sort de la boucle et on retourne la valeur
        except ValueError:
            print("Erreur : Ce n'est pas un nombre valide. Essayez encore.")

# Exemple de validation d'IP
def valider_ip(n1, n2, n3, n4):
    try:
        n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
        if (0 <= n1 <= 255) and (0 <= n2 <= 255) and (0 <= n3 <= 255) and (0 <= n4 <= 255):
            return f"{n1}.{n2}.{n3}.{n4}"
        else:
            return None
    except ValueError:
        return None
```

---

## 4. 🧬 Programmation Orientée Objet (Classes)

**Quand l'utiliser :** Quand le problème décrit des "choses" qui ont plusieurs caractéristiques spécifiques et des actions (ex: Un Chien qui peut "courir" ou dont on peut calculer le prix).
**Bonnes pratiques :**
- Le professeur demande presque toujours la méthode magique `__str__` pour gérer l'affichage avec un `print(objet)`.

### Système 4.1 : Classe avec calculs internes
**Idéal pour :** Des objets qui prennent des décisions basées sur leurs attributs.

```python
class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def anniversaire(self):
        """Modifie un attribut interne."""
        self.age += 1
        print(f"Joyeux anniversaire {self.nom}! Il a maintenant {self.age} ans.")

    def calculer_prix(self):
        """Retourne une valeur calculée selon l'état de l'objet."""
        if self.age < 1:
            return 3000
        elif self.race == "Chiwawa":
            return 6000
        else:
            return 1000

    def __str__(self):
        return f"Chien: {self.nom} (Race: {self.race}, Âge: {self.age})"
```

### Système 4.2 : Système Scolaire / Gestion (Objet contenant une liste)
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
```

### Système 4.3 : Bibliothèque (Composition d'Objets)
**Idéal pour :** L'exercice classique où une classe (Bibliothèque) possède un Dictionnaire d'autres Objets (Livre).

```python
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} ({self.annee})"

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.dict_livres = {} # Clé: Titre, Valeur: Objet Livre

    def ajouter_livre(self, livre_obj):
        if livre_obj.titre in self.dict_livres:
            print("Le livre existe déjà dans la bibliothèque.")
        else:
            self.dict_livres[livre_obj.titre] = livre_obj
            print(f"Livre ajouté à la bibliothèque {self.nom}.")

    def afficher_tout(self):
        print(f"--- Bibliothèque: {self.nom} ---")
        for titre, livre_obj in self.dict_livres.items():
            print(livre_obj)

# Utilisation
biblio = Bibliotheque("Ma Super Bibliothèque")
livre1 = Livre("Python pour les Nuls", "John Doe", 2020)
biblio.ajouter_livre(livre1)
```

---

## 📁 5. Manipulation de Fichiers (File I/O)

**Quand l'utiliser :** Si l'examen demande de sauvegarder des données ou de les charger depuis un fichier texte (vu dans `cours.py`).

```python
# 1. Lire tout le contenu d'un fichier
def lire_fichier(nom_fichier):
    try:
        fichier = open(nom_fichier, "r", encoding="utf-8")
        contenu = fichier.read()
        fichier.close()
        return contenu
    except FileNotFoundError:
        return "Le fichier n'existe pas."

# 2. Écrire dans un fichier (écrase le contenu précédent)
def ecrire_fichier(nom_fichier, texte):
    fichier = open(nom_fichier, "w", encoding="utf-8")
    fichier.write(texte)
    fichier.close()

# 3. Ajouter à un fichier existant (sans effacer le reste)
def ajouter_au_fichier(nom_fichier, texte):
    fichier = open(nom_fichier, "a", encoding="utf-8")
    fichier.write(texte + "\n")
    fichier.close()
```
