"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

numeros = []
print("Ingresa los 6 numeros ganadores de la loteria:")

for i in range(6):
    num = int(input("Valor = "))
    numeros.append(num)

numeros.sort()
print(f"Los numeros ganadores son: {numeros}")