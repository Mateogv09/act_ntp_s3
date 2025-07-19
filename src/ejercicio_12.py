n = int(input("Ingresa un número entero para calcular su factorial: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f"El factorial es: {factorial}")
