"""
Escribir una función que calcule el módulo de un vector.
"""

import math

def calculo_modulo(x,y):
    return math.sqrt(pow(x,2) + pow(y,2))

print(round(calculo_modulo(2,6),2))