"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""

def media(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total / len(numeros)

print(media(2, 2, 4))

# Respuesta doc
def mean(sample):
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))

    