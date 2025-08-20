"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de 
cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último
pedido y calcule el peso total del paquete que será enviado.
"""

peso_1 = 112
peso_2 = 75

payasos = int(input("Ingresa el valor total de payasos:"))
munecas = int(input("Ingresa el valor total de las muneas:"))

total = (peso_1*payasos) + (peso_2*munecas)

print(f"El peso total de el paquete es de: {total} KG")