# 5a - écrire un programme qui aide un admin de réseau à composer une addresse IP.
# Le programme demande à l'usager d'entrer chacun des 4 nombres qui composent
# l'addresse IP, puis fait la validation des 4 nombres entrés.
# si les 4 nombres sont valides, le programme affiche
# l'address comme :  "address valide:  192.168.1.1"
# sinon le programme doit afficher un message d'erreur de validation.

print("entrez les 4 nombres qui composent l'addresse IP ...")
nbr1 : int = int(input("entrez le 1er nombre: "))
nbr2 : int = int(input("entrez le 2e nombre: "))
nbr3 : int = int(input("entrez le 3e nombre: "))
nbr4 : int = int(input("entrez le 4e nombre: "))

if nbr1 >= 0 and nbr1 <= 255 and nbr2 >= 0 and nbr2 <= 255 and nbr3 >= 0 and nbr3 <= 255 and nbr4 >= 0 and nbr4 <= 255:
    addresse_complete = f"{nbr1}.{nbr2}.{nbr3}.{nbr4}"
    #on pourrait aussi faire:    addresse_complete = str(nbr1) + "." + str(nbr2) + "." + str(nbr3) + "." + str(nbr4)
    print(f"address valide: {addresse_complete}")
else:
    print("addresse non-valide!")