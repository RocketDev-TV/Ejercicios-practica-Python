# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

PI = 3.14

def a_circulo (r):
    return PI * r**2

def v_cilindro(h,r):
    return a_circulo(r) * h
    
print("Area del circulo = ", a_circulo(2))
print("Volumen del cilindro = ", v_cilindro(5,2))