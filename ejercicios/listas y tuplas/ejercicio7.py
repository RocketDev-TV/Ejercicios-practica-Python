"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen 
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
                #           #           #           #           #           #           #           #
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lista_n = []
posicion = 0
for i in abc:
    posicion+=1
    if posicion %3 == 0:
        pass
    else:
        lista_n.append(i)

for i in lista_n:
    print(f"{i} - ", end = "")