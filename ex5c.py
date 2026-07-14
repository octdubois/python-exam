# 4- écrire un programme qui contient 5 marques d'autos secrètes
# différentes, et demande à l'usager de deviner une de ces marques
# pour gagner.mettre la logique qui vérifie si l'usager a gagné ou
# pas dans une FONCTION et utiliser cette fonction,la fonction doit
# prendre la marque devinée par l'usager comme argument.


def affiche_resultat_jeu(liste,marque_devinee):
    for marque in liste:
        if marque == marque_devinee:
            print("vous avez gagne!")
            return # si usager gagne, on fait 'return' avec aucune valeur juste pour ne pas se rendre à la ligne 13
                   # il y a d'autres manières de contrôler si la ligne 13 exécute ou pas, mais return est la plus simple (vous pouvez essayer d'autres approches!)
    print("vous avez perdu!")

liste = ["bmw","audi","mazda","kia","ferrari"]
marque_devinee = input("devinez une marque: ")
affiche_resultat_jeu(liste,marque_devinee)