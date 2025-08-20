"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

materias = ["Matemáticas","Física","Química","Historia","Lengua"]
materias_rep = []
nota = []

print("Introduce las calificaciones de las asignaturas:")

for i in materias:
    calif = int(input(f"Calificacion para {i}:"))
    if calif >= 6:
        pass
    else:
        materias_rep.append(i)

print("Materias que no aprobaste y debes recursar:")
for i in materias_rep:
    print(f"Materia = {i}")