# Leia um número e informe se ele é positivo, negativo ou igual a zero.

numero = float(input("Informe um número: "))

if numero % 1 != 0 :
    print("O número é decimal!")
elif numero > 0 : 
    print("O número é positivo!")
elif numero == 0 :
    print("O número é zero!")
else : 
    print("O número é negativo!")