"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
frutas = {
    "platano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

while True:
    fruta_b = input("Introduce la fruta que deseas cotizar: ").lower()
    
    if fruta_b in frutas:
        kilos = float(input("Introduce el número de kilos que deseas cotizar: "))
        precio_kilo = frutas[fruta_b]
        total = precio_kilo * kilos
        print(f"Fruta = {fruta_b}\nPrecio = ${precio_kilo}")
        print(f"El total de {kilos} kilo(s) de {fruta_b} es ${total:.2f}")
        break
    else:
        print("No encontramos la fruta que ingresaste.\nPor favor vuelve a intentarlo.")



# Solucion 2

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")