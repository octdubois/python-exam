x = "x global" # x est global
l = [1, 2, 3] # l est global aussi

def func(l):
    print(x)
    l.append(4)
    print(l)
    l.append(4)
    l = []

func(l)