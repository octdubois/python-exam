# la bonne version:  on passe explicitement le string "x global"
# comme argument a la fonction

def func(x):
    print("la valeur de x dans la fonction est:", x)

x = "x global"
print("la valeur de x avant la fonction est:", x)
func(x)