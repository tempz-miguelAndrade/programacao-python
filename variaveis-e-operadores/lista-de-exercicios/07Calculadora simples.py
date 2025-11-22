# Peça dois números e uma operação (+, -, *, /).  
# Realize a operação escolhida e mostre o resultado.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
operador = input("Informe um operador (+, -, *, /): ")

resultado = (
    (operador == "+") * (num1 + num2) +
    (operador == "-") * (num1 - num2) +
    (operador == "*") * (num1 * num2) +
    (operador == "/") * (num1 / num2)
)

print(f"O resultado da sua operação é: {resultado}")