"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

inversion = float(input("Ingresa la cantidad que deseas invertir: $"))
interes = float(input("Ingresa el interés anual (en %): "))
tiempo = int(input("Escribe cuántos años deseas invertir: "))

for i in range(1, tiempo + 1):
    capital = inversion * (1 + interes / 100) ** i
    print(f"Año {i}: Capital acumulado con {interes}% anual: ${capital:.2f}")
