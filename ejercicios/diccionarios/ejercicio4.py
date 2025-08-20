"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en 
formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

mes = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

fecha = input("Escribe una fecha en formato dd/mm/aaaa: ")
fecha_separada = fecha.split("/")

# Convertimos el mes a entero para buscarlo en el diccionario
mes_numero = int(fecha_separada[1])

if mes_numero in mes:
    print(f"{fecha_separada[0]} de {mes[mes_numero]} de {fecha_separada[2]}")
else:
    print("Mes inválido.")
