
print("programme commence ici!")

def dis_hello():
    print("hello")

def get_favorite_number():
    x = 2
    y = 4
    z = x + y
    return z

def get_tax_rate():
    return 0.14975  # Exemple: taux de taxe au Québec

def get_greeting():
    return "Hello, student!"

def is_python_fun():
    return True

def get_top_3_languages():
    return ["Python", "JavaScript", "C++"]


print("juste avant l'appel de la fonction")
dis_hello()


valeur_retournee = get_favorite_number()
print(valeur_retournee)


print(get_favorite_number())