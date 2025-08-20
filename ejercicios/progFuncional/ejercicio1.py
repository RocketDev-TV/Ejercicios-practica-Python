"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y 
una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos 
de la cesta y devolver el precio final de la cesta.
"""

def aplicar_descuento(precio, porcentaje):
    total = precio - (precio * porcentaje / 100)
    return total

def aplicar_IVA(precio, IVA=16):
    total = precio + (precio * IVA / 100)
    return total
    
def procesar_cesta(cesta, funcion):
    total = 0
    for producto, (precio, porcentaje) in cesta.items():
        precio_final = funcion(precio, porcentaje)
        print(f"{producto}: {precio} -> {precio_final:.2f}")
        total += precio_final
    return total

cesta = {
    "pan": (20.0, 10),
    "leche": (15.0, 16),
    "queso": (80.0, 5),
}

total_descuento = procesar_cesta(cesta, aplicar_descuento)
print(f"Total con descuento: {total_descuento:.2f}")

total_IVA = procesar_cesta(cesta, aplicar_IVA)
print(f"Total con IVA: {total_IVA:.2f}")
    