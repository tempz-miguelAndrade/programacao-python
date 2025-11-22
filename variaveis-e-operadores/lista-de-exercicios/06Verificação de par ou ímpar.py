# Leia um número inteiro e informe se ele é par ou ímpar.

numero = int(input("informe um número inteiro: "))

par = numero % 2 == 0
impar = not par 

resultado = "Par" * par + "ímpar" * impar

print(resultado)
