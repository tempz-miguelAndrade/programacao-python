# Leia um número inteiro e informe "PAR" ou "ÍMPAR" usando operação ternária.

numero = int(input("Informe um número: "))

resultado = "Ímpar" if numero % 2 != 0  else "Par"

print(resultado)