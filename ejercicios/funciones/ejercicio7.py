# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def cuadrados(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i**2)
    return lista_2

print(cuadrados([2,3,4]))