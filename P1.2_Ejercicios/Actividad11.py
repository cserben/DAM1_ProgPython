n = int(input("Introduce un entero positivo: "))

if n <= 0:
    print("Por favor, introduce un entero positivo.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los enteros desde 1 hasta {n} es {suma}.")
