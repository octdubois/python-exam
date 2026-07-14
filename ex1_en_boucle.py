
def somme_liste(liste_nombres:list[int]) -> int:
    """
    additionne tous les nombres qui sont dans une liste

    Args:
        liste_nombres (list[int]): liste de nombres.

    Returns:
        int: la somme des nombres de liste_nombres.
    """

    if len(liste_nombres) == 0:
        return 0
    else:
        somme = 0
        for x in liste_nombres:
            somme = somme + x
        return somme
    

liste_nombres = [1,2,3]
bashar = somme_liste(liste_nombres)
print(f"la somme des nombres de la liste est : {bashar}")