
def square(number):
    resultat = number * number
    return resultat


nombre = int(input("entrez un nombre pour voir son carre: "))

carre = square(nombre)
print(f"le carre du nombre {nombre} est {carre}")