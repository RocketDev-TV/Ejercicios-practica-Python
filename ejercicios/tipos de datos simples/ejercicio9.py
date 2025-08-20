"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

inversion = int(input("Escribe la cantidad que deseas invertir en pesos mxn: $"))
interes = int(input("Escribe el interes anual de tu inversion %"))
tiempo = int(input("Escribe el numero de años que deseas invertir:"))

total = inversion * (interes / 100) * tiempo

print(f"El valor toda de tu inversion sera de ${total}")