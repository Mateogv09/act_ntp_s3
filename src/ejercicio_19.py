frase = "programacion es divertida"
vocales = "aeiou"
contador_vocales = sum(1 for letra in frase if letra.lower() in vocales)
print(f"Cantidad de vocales: {contador_vocales}")
