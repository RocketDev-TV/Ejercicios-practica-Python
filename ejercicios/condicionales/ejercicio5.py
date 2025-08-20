"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
superiores a 1000 USD mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla 
si el usuario tiene que tributar o no.
"""

edad = int(input("Introduce tu edad:"))
salario = float(input("Introduce el total de tus ingresos:$"))

if edad >= 16 and salario >= 1000:
    print("Debes realizar tus declaraciones.")
else:
    print("No es necesario que relices tu declaracion.")