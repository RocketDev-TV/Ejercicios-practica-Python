"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha = str(input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa:"))

if len(fecha) == 10:
    print(f"Dia:{fecha[:fecha.find('/')]}\nMes:{fecha[fecha.find('/')+1:5]}\nAño:{fecha[6:]}")
else:
    print("Introduce una fecha valida")

# Solucion chat

fecha = input("Introduce tu fecha de nacimiento en formato d/m/aaaa o dd/mm/aaaa: ")

partes = fecha.split("/")

if len(partes) == 3:
    dia, mes, anio = partes
    print(f"Día: {dia}\nMes: {mes}\nAño: {anio}")
else:
    print("Formato incorrecto. Asegúrate de usar '/' como separador (ej: 1/1/2000).")

# Solucion 1

fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

# Solucion 2

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)