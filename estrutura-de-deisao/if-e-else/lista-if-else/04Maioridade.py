# Pergunte a idade de uma pessoa e diga se ela é maior de idade (18 anos ou mais) ou menor de idade.

idade = int(input("Informe sua idade: "))

if idade < 18 :
    print("Você não atingiu a maior idade!")
elif idade >= 18 : 
    print("Você atingiu a maior idade!")