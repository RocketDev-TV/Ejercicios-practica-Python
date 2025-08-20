"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
muestre por pantalla su media y desviación típica.
"""
import math

lista = []

tam = int(input("Ingresa el tamanño que deseas para la lista:"))

for i in range(1,tam+1):
    numeros = int(input(f"Ingresa el valor {i}:"))
    lista.append(numeros)
print("La lista es la siguiente:")
for i in lista:
    print(f"{i},", end = "")

# Media
# M = suma de n / tam
media = sum(lista) / tam

print(f"El valor de la media es = {media:.2f}")

# Desviacion tipica
# S = raiz((1/n-1)*suma(xi-media)²)

suma_valores = 0

for i in lista:
    suma_valores += (i-media) ** 2

S = math.sqrt((1/(tam-1)) * suma_valores)

print(f"El valor de la desviacion es = {S:.2f}")
#print("\nLista = ", lista)


