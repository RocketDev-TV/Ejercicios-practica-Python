# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    fac = 1
    for i in range(1,numero+1):
        fac *= i
    return fac

print(factorial(3))