# Leia um número e imprima sua tabuada de 1 a 10.

numero = int(input("Informe um número: "))

resultado = 0

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")