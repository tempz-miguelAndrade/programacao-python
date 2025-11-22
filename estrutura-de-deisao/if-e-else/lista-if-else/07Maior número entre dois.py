#   Leia dois números e informe qual deles é o maior.  
#   Se forem iguais, informe `"Números iguais"`.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))



if num1 == num2 :
    print("Os números são iguais!")
elif num1 > num2 :
    print(f"O número {num1} é maior que o número {num2}")
else :
    print(f"O número {num2} é maior que o número {num1}")