# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
import math 

def operaciones(lista):
    diccionario = {}

    suma = 0
    suma_2 = 0
    
    # Sacamos la suma de los valroes
    for i in lista:
        suma += i
    media = suma / len(lista)
    
    # Varianza : s² = Σ (xᵢ - x̄)² / (n - 1)
    for i in lista:
        suma_2 += (i - media) ** 2
    varianza = suma_2 / (len(lista) - 1)
    
    # Desviacion    
    desviacion = math.sqrt(varianza)
    
    return {
    "media": media,
    "varianza": varianza,
    "desviacion": desviacion
    }

    
print(operaciones([1,2,3,4,5]))
