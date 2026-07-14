
# ne PAS faire ca: python est capable de lire x global a partir de la fonction
# mais ca peut creer des problemes dans des cas plus complexes,
# on evite de le faire.
# Dans les fonctions: toujours utiliser des variables qui sont creees
# DANS la fonction, ou les parametres
def func():
    print("la valeur de x dans la fonction est:", x)

x = "x global"
print("la valeur de x avant la fonction est:", x)
func()



