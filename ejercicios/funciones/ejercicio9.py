# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

print(mcd(12, 18))
print(mcm(12, 18))
