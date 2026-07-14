# Guide Ultime pour l'Examen Pratique (Objectif : < 30 min)

Ce guide fournit des modèles détaillés (templates) classés par structures de données et par concepts. L'objectif est de vous fournir des "recettes" prêtes à l'emploi que vous pouvez mentalement copier-coller et adapter à n'importe quel problème pour terminer rapidement et sans erreur.

---

## 🌟 Le Menu Interactif (`while True`)
**Quand l'utiliser :** Dès qu'un exercice demande un programme qui "roule en continu" ou "roule en boucle" et donne des choix à l'usager.

```python
# 1. TOUJOURS initialiser vos structures principales AVANT la boucle
ma_liste = []
mon_dictionnaire = {}

def afficher_options():
    print("\n--- Menu Principal ---")
    print("1- Voir tous les éléments")
    print("2- Ajouter un élément")
    print("3- Supprimer un élément")
    print("q- Quitter (ou tapez Entrée)")

# 2. La boucle infinie
while True:
    afficher_options()
    choix = input("Entrez votre choix : ")

    if choix == "1":
        # Appeler la fonction d'affichage
        pass
    elif choix == "2":
        # Appeler la fonction d'ajout
        pass
    elif choix == "3":
        # Appeler la fonction de suppression
        pass
    elif choix == "q" or choix == "":
        print("Fin du programme...")
        break # <-- Essentiel pour sortir de la boucle
    else:
        print("Erreur : Choix non-valide! Veuillez réessayer.")
```

---

## 1. 📦 Les Listes (`[]`)
**Quand l'utiliser :** Pour stocker une collection ordonnée d'éléments simples (ex: un historique de noms, une liste d'adresses IP créées, une liste de nombres).

### Exemple 1.1 : Gestion complète d'une liste (Ajouter, Afficher, Compter, Chercher)
```python
def ajouter_a_la_liste(liste, nouvel_element):
    """Ajoute un élément avec validation (pas vide, pas de doublon)."""
    if nouvel_element == "":
        print("Erreur : Impossible d'ajouter un élément vide.")
        return # Quitte la fonction immédiatement

    if nouvel_element in liste:
        print(f"Erreur : L'élément '{nouvel_element}' existe déjà dans la liste.")
    else:
        liste.append(nouvel_element)
        print(f"Succès : '{nouvel_element}' a été ajouté!")

def afficher_la_liste(liste):
    """Affiche le contenu et la taille de la liste."""
    if len(liste) == 0:
        print("La liste est actuellement vide.")
        return

    print(f"Il y a {len(liste)} éléments dans la liste :")
    for element in liste:
        print(f"- {element}")

def chercher_dans_liste(liste, element_recherche):
    """Vérifie si un élément est présent."""
    if element_recherche in liste:
        print(f"Oui, '{element_recherche}' est bien dans la liste!")
    else:
        print(f"Non, '{element_recherche}' est introuvable.")

def supprimer_de_la_liste(liste, element_a_supprimer):
    """Supprime un élément s'il existe."""
    if element_a_supprimer in liste:
        liste.remove(element_a_supprimer)
        print(f"'{element_a_supprimer}' a été supprimé.")
    else:
        print("Erreur : Élément introuvable.")
```

### Exemple 1.2 : Filtrer une liste avec une condition
```python
def compter_mots_longs(liste_mots):
    """Exemple : Compter les mots qui ont plus de 4 caractères."""
    compteur = 0
    for mot in liste_mots:
        if len(mot) > 4:
            compteur += 1 # Équivaut à compteur = compteur + 1
    print(f"Il y a {compteur} mots qui ont plus de 4 caractères.")
```

---

## 2. 📖 Les Dictionnaires (`{}`)
**Quand l'utiliser :** Quand vous devez associer deux données liées (Clé -> Valeur), ou quand vous devez COMPTER le nombre d'apparitions d'éléments (fréquence).

### Exemple 2.1 : Association Clé-Valeur (ex: Contacts téléphoniques)
```python
def ajouter_ou_modifier_contact(dico_contacts, nom, numero):
    """Ajoute un contact s'il n'existe pas, ou le met à jour."""
    if numero == "":
        print("Erreur : Le numéro ne peut pas être vide.")
        return

    if nom in dico_contacts:
        print(f"Le contact '{nom}' existe déjà, mise à jour du numéro.")

    # Cette ligne crée la clé ou met à jour la valeur si la clé existe
    dico_contacts[nom] = numero
    print(f"Contact {nom} enregistré avec succès!")

def voir_numero_contact(dico_contacts, nom):
    """Cherche et affiche le numéro d'un contact spécifique."""
    if nom in dico_contacts:
        numero = dico_contacts[nom]
        print(f"Le numéro de {nom} est {numero}")
    else:
        print(f"Erreur : Le contact '{nom}' n'existe pas.")

def supprimer_contact(dico_contacts, nom):
    """Supprime un contact du dictionnaire en toute sécurité."""
    if nom in dico_contacts:
        del dico_contacts[nom]
        print(f"Le contact '{nom}' a été supprimé.")
    else:
        print(f"Erreur : Impossible de supprimer, '{nom}' introuvable.")

def afficher_tous_les_contacts(dico_contacts):
    """Parcourt toutes les paires clé/valeur."""
    if len(dico_contacts) == 0:
        print("Aucun contact enregistré.")
        return

    for cle, valeur in dico_contacts.items():
        print(f"Nom : {cle} --- Numéro : {valeur}")
```

### Exemple 2.2 : Compter des occurrences (ex: Mots dans une phrase)
**C'est un modèle TRÈS fréquent aux examens.**
```python
def compter_frequence_mots(phrase):
    """Sépare une phrase et compte combien de fois chaque mot apparaît."""
    # .split() sépare la phrase en liste de mots par les espaces
    liste_des_mots = phrase.split()
    compteur = {}

    for mot in liste_des_mots:
        if mot in compteur:
            # Le mot est déjà dans le dictionnaire, on ajoute 1 à sa valeur
            compteur[mot] = compteur[mot] + 1
        else:
            # C'est la première fois qu'on voit le mot, on l'initialise à 1
            compteur[mot] = 1

    # Affichage du résultat final
    print("\nCompte des mots :")
    for mot, frequence in compteur.items():
        print(f"Le mot '{mot}' apparaît {frequence} fois.")
```

---

## 3. ⚙️ Les Fonctions (`def`)
**Pourquoi l'utiliser :** Le professeur exige souvent l'utilisation de fonctions pour nettoyer le code (souvent pour 15% de la note). Ne laissez pas de logique complexe (les `if/else` d'ajout ou de recherche) directement dans votre `while True`.

### Principes fondamentaux des fonctions :
- **Passage par référence (Listes et Dictionnaires) :** En Python, si vous passez une liste ou un dictionnaire à une fonction, et que vous le modifiez avec `.append()` ou `dict[clé] = val`, **l'objet original est modifié**. Vous n'avez PAS besoin d'utiliser `return` dans ce cas.
- **Utiliser `return` pour les validations et calculs :**
```python
def est_addresse_ip_valide(n1, n2, n3, n4):
    """Vérifie si les 4 nombres forment une IP valide. Retourne un booléen."""
    if (0 <= n1 <= 255) and (0 <= n2 <= 255) and (0 <= n3 <= 255) and (0 <= n4 <= 255):
        return True
    return False

# Utilisation dans la boucle principale :
# if est_addresse_ip_valide(n1, n2, n3, n4) == True:
#     ip_complete = f"{n1}.{n2}.{n3}.{n4}"
#     liste_ip.append(ip_complete)
```

---

## 4. 🧬 Programmation Orientée Objet (Classes)
**Quand l'utiliser :** Quand le problème décrit des "choses" qui ont plusieurs caractéristiques spécifiques (ex: "Une Auto a une marque, une année et un modèle" ou "Un Étudiant a un nom et un code").

### Exemple 4.1 : Une classe simple avec la méthode `__str__`
```python
class Vehicule:
    # 1. Le constructeur (__init__) initialise les attributs
    def __init__(self, marque_vehicule, annee_vehicule):
        self.marque = marque_vehicule
        self.annee = annee_vehicule

    # 2. La méthode magique __str__ dicte comment l'objet s'affiche
    # (le prof le demande presque toujours).
    def __str__(self):
        return f"Véhicule {self.marque} (Année: {self.annee})"

# Utilisation :
mon_auto = Vehicule(marque_vehicule="Mazda", annee_vehicule="2010")
print(mon_auto) # Va afficher ce qui est défini dans le __str__
```

### Exemple 4.2 : Une classe contenant une liste (Avancé)
**Cas classique : Un "Cours" qui contient une liste "d'Étudiants".**
```python
class Cours:
    def __init__(self, code, titre):
        self.code = code
        self.titre = titre
        # On initialise une liste VIDE À L'INTÉRIEUR de l'objet
        self.etudiants_inscrits = []

    def inscrire_etudiant(self, nom_etudiant):
        """Méthode pour ajouter un élément dans la liste interne."""
        self.etudiants_inscrits.append(nom_etudiant)
        print(f"'{nom_etudiant}' a été inscrit au cours {self.code}.")

    def afficher_etudiants(self):
        """Méthode pour afficher la liste interne."""
        if len(self.etudiants_inscrits) == 0:
            print("Aucun étudiant inscrit.")
            return

        print(f"Étudiants inscrits au cours de {self.titre} :")
        for etudiant in self.etudiants_inscrits:
            print(f"- {etudiant}")

    def __str__(self):
        return f"Cours: {self.code} - {self.titre}"

# Utilisation :
cours_math = Cours(code="MATH101", titre="Introduction aux Mathématiques")
cours_math.inscrire_etudiant("Alice")
cours_math.inscrire_etudiant("Bob")
cours_math.afficher_etudiants()
```

---

## 🎯 Liste de contrôle rapide pour l'examen (Stratégie < 30 min) :
1. **Lisez l'énoncé attentivement :**
   - Vous stockez un historique simple ? -> **Liste (`[]`)**
   - Vous associez deux infos ou vous comptez ? -> **Dictionnaire (`{}`)**
   - Vous créez des objets complexes (Voiture, Avion) ? -> **Classe (OOP)**
2. **Préparez la boucle principale :** Si le programme doit rouler en continu, copiez-collez le modèle du menu `while True`.
3. **Sortez la logique :** Créez une fonction `def` pour chaque option du menu (Ajouter, Afficher, etc.).
4. **Validez toujours vos ajouts/suppressions :** Les points faciles sont ici. Utilisez toujours `if element in liste:` ou `if cle in dico:` avant d'ajouter ou de supprimer.
5. **Utilisez les `f-strings` :** Pour l'affichage, c'est la méthode la plus rapide et propre : `print(f"Mon message avec {ma_variable}")`.
