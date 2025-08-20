"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
y muestre por pantalla cada uno de los productos en una línea distinta.
"""

prodcutos = str(input("Introduce los productos que deseas agregar (separalos por comas): "))

lista = prodcutos.split(",")

print(" --- Lista de prodcutos ----")
for prodcutos in lista:
    print(prodcutos.strip())