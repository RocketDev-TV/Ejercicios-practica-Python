"""
Una panadería vende barras de pan a 3.49 dolares cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y el coste final total.
"""
# Constantes
precio_pan = 3.49
descuento = 0.60

# Entrada de datos
barras = int(input("Escribe el numero de barras que no son del dia: "))

# Ticket
print("----PANADERIA LA CONCHA DE LA LORA---")
print(f"Barra de pan: ${precio_pan} USD")
prec = barras * precio_pan

print(f"{barras} barras x ${precio_pan}: ${prec}")
desc = descuento * 100
prec_1 = barras * precio_pan * (descuento)

print(f"Descuento del %{desc} en {barras} pzs: -${prec_1}")
prec_2 = barras * precio_pan - prec_1

print(f"Total: ${prec_2}")