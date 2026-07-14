Notes de cours: fonctions, scopes, mutabilité
================================================

1. Les fonctions
----------------

Une fonction est un bloc de code défini une seule fois, puis exécuté quand on le demande.
On peut appeler une fonction autant de fois qu'on veut, après sa définition.

En Python, une fonction est définie avec:

- le mot-clé `def`
- le nom de la fonction
- des parenthèses
- le symbole `:`
- un bloc de code indenté

Une fonction est exécutée seulement quand elle est appelée avec son nom suivi de parenthèses.

Exemple:

```python
def dis_hello():
    print("hello")

dis_hello()
```

Ici, `dis_hello` est une fonction qui ne retourne aucune valeur. Elle fait seulement une action:
afficher du texte. La fonction `print()` fonctionne de manière semblable: elle affiche quelque chose,
mais elle ne retourne pas une valeur utile à réutiliser. Python définit déjà des fonctions pour nous qui sont prêtes
à être utilisées, print() et input() sont des exemples.


2. Fonctions qui retournent une valeur
-------------------------------------

Une fonction peut retourner une valeur avec le mot-clé `return`.
La valeur retournée peut ensuite être stockée dans une variable, affichée, utilisée dans un calcul,
ou passée à une autre fonction. La fonction termine directement quand `return` est exécuté.

Exemples:

Définitions:
```python
def get_favorite_number():
    return 7

def get_tax_rate():
    return 0.14975  # Exemple: taux de taxe au Québec

def get_greeting():
    return "Hello, student!"

def is_python_fun():
    return True

def get_top_3_languages():
    return ["Python", "JavaScript", "C++"]
```

Utilisation:

```python
number = get_favorite_number()
print(number)

tax_rate = get_tax_rate()
print(tax_rate)

print(get_greeting())
print(is_python_fun())
print(get_top_3_languages())
```

Une fonction peut être appelée plusieurs fois:

```python
print(get_favorite_number())
print(get_favorite_number())
print(get_favorite_number())
```


3. Paramètres et arguments
-------------------------

Une fonction peut prendre des paramètres.
Les paramètres indiquent les valeurs qu'on doit passer à la fonction quand on l'appelle.

Quand la fonction est exécutée, chaque paramètre devient une nouvelle variable locale créée
automatiquement dans le corps de la fonction.

L'argument est la valeur réelle qu'on donne à la fonction au moment de l'appel.

Exemple:

```python
def square(number):
    return number * number

print(square(5))
```

Dans cet exemple:

- `number` est le paramètre.
- `5` est l'argument.
- Quand la fonction est appelée, Python crée une variable locale `number` qui contient la valeur `5`.

Le nom du paramètre est simplement un nom de variable.

Autres exemples:

```python
def multiply(a, b):
    return a * b

def greet(name):
    print(f"Hello, {name}!")

def print_sum(x, y):
    print(f"The sum of {x} and {y} is {x + y}")

def format_full_name(first, middle, last):
    return f"{first} {middle} {last}"
```

L'ordre des paramètres est important:

```python
print(format_full_name("John", "William", "Smith"))
```

Ici:

- `first` reçoit `"John"`
- `middle` reçoit `"William"`
- `last` reçoit `"Smith"`


4. Exemple: fonction qui retourne la somme d'une liste de nombres, et retourne 0 si la liste est vide
----------------------------

```python
def somme_liste(liste_nombres):
    if len(liste_nombres) == 0:
        return 0
    else:
        somme = 0
        for x in liste_nombres:
            somme = somme + x
        return somme
```

Utilisation:

```python
print(somme_liste([1, 2, 3]))
print(somme_liste([]))
```

Le `else` n'est pas obligatoire ici, parce que `return 0` termine déjà la fonction:

```python
def somme_liste(liste_nombres):
    if len(liste_nombres) == 0:
        return 0

    somme = 0
    for x in liste_nombres:
        somme = somme + x
    return somme
```

Attention: Python ne donne pas toujours une erreur immédiatement si on passe un argument
dont le type est différent de ce que la fonction attend.

Par exemple, si une fonction attend une liste de nombres, mais qu'on lui passe une chaîne de caractères,
le comportement peut être différent de ce qu'on voulait.


5. Exemple: restructurer un programme avec des fonctions
-----------------------------------------------------

Programme de départ:

```python
while True:
    print("Welcome to the calculator app!")
    print("Hope you find it useful!\n")

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print(f"The sum of {x} and {y} is {x + y}")
    print(f"The difference of {x} and {y} is {x - y}")
    print(f"The product of {x} and {y} is {x * y}")
```

Version avec fonctions:

```python
def print_welcome_message():
    print("Welcome to the calculator app!")
    print("Hope you find it useful!\n")

def print_results(x, y):
    print(f"The sum of {x} and {y} is {x + y}")
    print(f"The difference of {x} and {y} is {x - y}")
    print(f"The product of {x} and {y} is {x * y}")

while True:
    print_welcome_message()

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print_results(x, y)
```

Les fonctions permettent de regrouper du code qui a une responsabilité claire.
Le programme devient plus facile à lire et à orgraniser. Les fonctions sont essentielles dans n'importe
quel programme qui commence à être long, sinon il est impossible d'organiser le programme et il devient
très difficle à comprendre pour les humains.

---------------------------------------
Exemple de documentation des fonctions, et annotation des types de paramètres et de valeur retournée par les fonctions:

def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b


toute la partie suivante est la documentation de la fonction, qui apparaît lorsqu'on met la souris sur le nom
de la fonction dans VSCode ou tout autre éditeur de code:

    """
    Add two integers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The sum of a and b.
    """

les mots clés 'Args:' et 'Returns:', ainsi que l'écriture de chaque paramètre avec son type entre paranthèse
comme 'a (int)', et le type de la valeur retournée comme 'int:' suivie de sa description permettent 
d'annoter le tout de manière structurée qui sera comprise par VSCode.
Cette documentation est complètement ignorée par Python, tout comme les commentaires, mais elle est essentielle pour
les humains qui développent le code afin de comprendre exactement ce que toutes les fonctions font et comment elles sont doivent être utilisées.