"""
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""

def calificaciones(notas): 
    tipo_nota = []
    for nota in notas:
        if nota < 6:
            tipo_nota.append("Nota baja")
        elif nota >= 6 and nota <= 8:
            tipo_nota.append("Nota regular")
        elif nota > 8 and nota < 9:
            tipo_nota.append("Nota buena")
        elif nota >= 9:
            tipo_nota.append("Nota excelente")
    return tipo_nota

lista_notas = [10, 5.5, 6, 8, 8.7, 4, 9]
res = calificaciones(lista_notas)
print(f"Lista de notas: {lista_notas}")
print(f"Tipo de nota: {res}")

    

