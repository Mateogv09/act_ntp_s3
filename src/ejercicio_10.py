contador_palabras = 0
while True:
    palabra = input("Ingresa una palabra (escribe 'fin' para terminar): ")
    if palabra.lower() == "fin":
        break
    contador_palabras += 1
print(f"Se leyeron {contador_palabras} palabras.")
