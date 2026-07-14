# 4- Créer une classe Auto et une classe Moto et une classe Avion et créer quelques attributs
# pertinents pour chaque classe.
# Il faut aussi creer la methode speciale __str__ 
# Créer plusieurs objets de type auto et moto et avion dans un programme simple de votre choix,
# soyez créatifs (si vous le voulez). Par exemple, on peut avoir un programme qui
# permet a l'usager de creer des objets de chaque type en boucle, puis affiche tous les objets
# créés avant de terminer.

# 5a- Créer une classe Animal et une classe Personne.
# Créer quelques attributs pertinents pour chaque classe comme le nom et l'age.
# Ajouter aussi un attribut qui permet d'associer un animal
# avec son propriétaire, car tous les animaux doivent avoir un propriétaire dès qu'ils sont créés.
# Utiliser ces 2 classes pour créer des animaux et des personnes
# (n'oubliez pas que chaque animal doit avoir un propriétaire à tout moment).


# 5b- créer une application qui roule en continue et qui permet à l'usager de:
#
# - créer une personne ou un animal en utilisant les classes de ex3a. On distingue les personnes
# et animaux par leur nom, donc les noms doivent etre uniques dans le systeme.
# - afficher les infos de tous les animaux qui appartiennent à une personne choisie
# par l'usager

# Les personnes et animaux créés doivent être persistés dans la mémoire du programme.

--------------------------------

# 6a- Créer une classe Livre avec les attributs titre, auteur et annee_publication. Ajouter la
# méthode __str__ pour afficher ces informations dans un message complet.

# 6b- Créer une classe Page avec les attributs numero_page et contenu (string qui represente le texte
# de la page) et sa methode __str__ .

# 6c- Modifier les attributs des classes de la manière appropriée afin de pouvoir associer des pages à des livres,
# donc chaque livre doit avoir des pages. Aussi ajouter la methode afficher_pages() dans la classe
# Livre qui va afficher le contenu de toutes les pages du livre.

# 6d- Créer un programme avec ces 2 classes. Le programme commence avec 4 livres et leurs pages que VOUS créez
# dans le code (donc sans demander à l'usager). Gardez le contenu des pages simple et créez un
# petit nombre de pages par livre pour garder l'exercice simple. Il faut que ces livres soient insérés
# dans une liste globale dans le progamme.

# Par la suite, le programme roule en continu et offre à l'usager les fonctionnalités suivantes:

# 1- choisir un livre à visualiser par son titre. (donc il faut afficher tout le contenu des pages
# du livre choisi).

# 2- faire une recherche des livres disponibles par annee de publication (juste afficher leur titre).

# 3- faire une recherche des livres disponibles par auteur (juste afficher leur titre).

# BONUS: comment faire pour rendre la recherche non-sensible a la casse ?


-------------------------------------------------------

7- refaire ce probleme du cours5 mais en utilisant une class Voiture, chaque voiture doit avoir
une marque, annee et couleur:


# ex8.a:

# écrire un programme en Python qui demande une liste d'autos à l'usager.
# Par exemple, l'usager peut choisir d'entrer :   bmw bmw audi honda mazda kia honda
# à vous de choisir comment l'usager va entrer cette liste de marquesm mais Il faut que l'usager
# entre au moins 1 marque avant de continuer

# Le programme doit par la suite afficher la valeur totale avant taxes ET après taxes de tous les autos
# de la liste. Les taxes sont de 15%.

# voici la valeur de chaque marque connue AVANT taxes:

# "mazda":         23000$
# "kia":           20000$
# "ferrari":      100000$
# "bmw":           30000$
# "honda":         24500$
# "toyota":        25000$
# "audi":          40000$
# "mercedes":      45000$
# "chevrolet":     27000$
# "ford":          26000$
# "nissan":        24000$
# "volkswagen":    28000$
# "hyundai":       22000$
# "jeep":          32000$
# "subaru":        26000$
# "lexus":         39000$
# "tesla":         55000$
# "porsche":       90000$
# "land rover":    70000$
# "volvo":         42000$
# "mitsubishi":    21000$
# "cadillac":      48000$
# "acura":         35000$
# "lincoln":       47000$
# "infiniti":      36000$
# "mini":          29000$
# "alfa romeo":    43000$
# "fiat":          19500$
# "chrysler":      31000$
# "buick":         34000$
# "gmc":           37000$
# "ram":           38000$
# "dodge":         33000$
# "genesis":       45000$
# "peugeot":       27000$
# "renault":       26000$
# "citroen":       25000$
# "saab":          24000$
# "skoda":         23000$
# "seat":          22000$
# "suzuki":        20000$
# "tata":          18000$
# "mahindra":      19000$
# "baic":          17000$
# "geely":         16500$
# "byd":           28000$
# "nio":           60000$
# "lucid":         85000$
# "rivian":        75000$
# "koenigsegg":  1500000$
# "bugatti":     3000000$


# Pour toute marque qui ne se trouve pas dans cette liste de prix, le prix par défaut est de 45000$.

# Votre programme doit être assez générique pour fonctionner avec n'importe quelle
# liste d'autos entrés par l'usager.


# ex8.b:
# Adapter votre solution pour ex8.a afin d'accomoder les majuscules et les espaces vides laissées par l'usager avant 
# et/ou après chaque marque entrée. Par exemple, si l'usager entre "Mazda", votre programme doit comprendre que c'est une
# "mazda" et doit chercher le prix approprié. Même chose si l'usager entre " Mazda" ou "Mazda " ou " Mazda   " ou
# " mazda " , etc ...

# Pour faire ce problème, vous devez explorer et utiliser les fonctions strip() et lower() qui agissent
# sur les strings (similairement à append() qui agit sur les listes par exemple)
