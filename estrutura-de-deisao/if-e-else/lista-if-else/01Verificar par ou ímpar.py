# Leia um número inteiro e imprima `"PAR"` se ele for par, ou `"ÍMPAR"` se for ímpar.

numero = int(input("Informe um número inteiro: "))

if numero % 2 != 0 :
    print("Esse número é ímpar!")
else :
    print("Esse número é par!")