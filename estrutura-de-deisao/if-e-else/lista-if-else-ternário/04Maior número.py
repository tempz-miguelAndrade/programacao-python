#   Leia dois números e mostre qual é o maior usando ternário.
#   Se forem iguais, exiba "Números iguais".

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

resultado = f"Os dois número são iguais!" if num1 == num2 else f"O número {num1} é maior que o número {num2}" if num1 > num2 else f"O número {num2} é maior que o número {num1}" 

print(resultado)