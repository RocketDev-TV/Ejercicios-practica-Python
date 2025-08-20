"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces
que contiene cada vocal.
"""

# Solucion 1
palabra = input("Escribe una palabra:").lower()
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for i in palabra:
    if i == "a":
        contador_a+=1
    if i == "e":
        contador_e+=1
    if i == "i":
        contador_i+=1
    if i == "o":
        contador_o+=1
    if i == "u":
        contador_u+=1

print(f"La letra a aparece {contador_a} veces.")
print(f"La letra e aparece {contador_e} veces.")
print(f"La letra i aparece {contador_i} veces.")
print(f"La letra o aparece {contador_o} veces.")
print(f"La letra u aparece {contador_u} veces.")

# Solucion 2

word = input("Introduce una palabra: ").lower()
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print(f"La vocal {vocal} aparece {times} veces")




