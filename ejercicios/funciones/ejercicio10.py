# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def binario_a_decimal(binario):
    decimal = 0
    potencia = len(binario) - 1
    for digito in binario:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1
    return decimal

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

print(decimal_a_binario(28))

print(binario_a_decimal("101011"))