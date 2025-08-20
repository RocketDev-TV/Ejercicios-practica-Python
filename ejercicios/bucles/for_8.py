
"""
Pide al usuario un número entero positivo impar. 
Luego, muestra en pantalla una figura triangular donde cada línea comienza desde el número ingresado
y va bajando de 2 en 2, hasta llegar al 1, agregando un número más en cada fila.

7
7 5
7 5 3
7 5 3 1
"""

numero_2 = int(input("Ingresa un número impar positivo desde donde quieres empezar: "))

# Validamos que sea impar y positivo
if numero_2 % 2 == 0 or numero_2 <= 0:
    print("Debes ingresar un número impar y positivo.")
else:
    # Bucle externo: número de filas
    for y in range(1, (numero_2 // 2) + 2):  # porque vamos agregando 1 número por fila
        valor = numero_2
        for x in range(y):
            print(valor, end=" ")
            valor -= 2
        print("")
