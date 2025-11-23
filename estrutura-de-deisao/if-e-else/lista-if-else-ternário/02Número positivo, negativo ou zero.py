# Leia um número e determine se ele é positivo, negativo ou zero, utilizando ternário aninhado.

numero = int(input("Informe um número: "))

resultado = "Positivo" if numero > 0 else "negativo" if numero < 0 else "zero"

print(resultado)