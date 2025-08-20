"""
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
 primeros enteros positivos puede ser calculada de la siguiente forma:
"""
n = int(input("Ingresa el valor: "))

if n > 0:
    suma = n * (n + 1) // 2  # Usamos // para que el resultado sea entero

    print("Los números que se están sumando son:")
    for i in range(1, n + 1):  # Va de 1 a n (incluyendo n)
        if i < n:
            print(f"{i} + ", end="")  # Imprime en la misma línea
        else:
            print(f"{i}")  # El último número sin el '+'

    print("El valor final es:", suma)
else:
    print("El valor es inválido, solo se aceptan números positivos.")
