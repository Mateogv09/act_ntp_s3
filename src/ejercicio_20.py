mayor_edad = -1
while True:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > mayor_edad:
        mayor_edad = edad
print(f"La mayor edad ingresada es: {mayor_edad}")
