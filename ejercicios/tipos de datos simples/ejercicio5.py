"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
horas = int(input("Ingresa el total de horas trabajadas:"))
costo_p_hora = int(input("Ingresa el valor x hora:$")) 

total_h = horas * costo_p_hora

print(f"El total de tu sueldo es: ${total_h} por {horas} horas.")
