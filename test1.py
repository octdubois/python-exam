
# meme programme que ex1.py mais en boucle pour rouler continuellement
while True:
    chiffre = int(input("entrez un chiffre entre 1 et 9 pour avoir sa table de multiplication: "))

    if 1 <= chiffre and chiffre <= 9:   # c'est pas bon comme ca:  1 <= chiffre <= 9
        # ici chiffre est valide
        for i in range(1,11):
            print(f"{chiffre} x {i} = {chiffre * i}")
    else:
        print("chiffre n'est pas entre 1 et 9")

    # apres le if-else on se rend ici
