"""
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
"""

def transformacion(diccionario):
    dic_s = {}
    for materia, nota in diccionario.items():
        if nota < 6:
            dic_s[materia.upper()] = "Nota mala"
        elif nota >= 6 and nota < 8:
            dic_s[materia.upper()] = "Nota regular"
        elif nota >= 8 and nota <= 9:
            dic_s[materia.upper()] = "Nota buena"
        elif nota > 9:
            dic_s[materia.upper()] = "Nota excelente"
    return dic_s


dicc = {
    'Matematicas': 10,
    'Fisica': 8,
    'Ingles': 7
}

res = transformacion(dicc)
print(res)