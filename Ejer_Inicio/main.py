import random

aleatorio = random.randint(1, 100)
exito = False

while not exito:

    numero = int(input("Introduce un número entre 1 y 100"))

    if numero == aleatorio:
        exito = True
    elif numero > aleatorio:
        print("Mas bajo")
    else:
        print("Apunta mas alto")

print("Acertatste, enhorabuena")


