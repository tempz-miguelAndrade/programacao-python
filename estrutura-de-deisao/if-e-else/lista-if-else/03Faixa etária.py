#   Leia a idade de uma pessoa e imprima:
#   - `"Criança"` se for menor que 13  
#   - `"Adolescente"` se for de 13 a 19  
#   - `"Adulto"` se for de 20 a 64  
#   - `"Idoso"` se for 65 ou mais

idade = int(input("Informe sua idade: "))

if idade < 13 : 
    print("Criança!")
elif idade >= 13 and idade < 18 :
    print("Adolescente!")
elif idade >= 18 and idade < 60 : 
    print("Adulto!")
else : 
    print("Idoso!")