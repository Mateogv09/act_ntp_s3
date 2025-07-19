import random

numero_aleatorio = random.randint(1, 10)
while True:
    intento = int(input("Adivina el número entre 1 y 10: "))
    if intento == numero_aleatorio:
        print("¡Felicidades, has adivinado el número!")
        break
    else:
        print("Intenta de nuevo.")
