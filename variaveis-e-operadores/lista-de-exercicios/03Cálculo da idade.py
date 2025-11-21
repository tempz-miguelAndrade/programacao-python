# Peça o ano de nascimento do usuário e calcule a idade atual.

anoNascimento = int(input("Informe sua data de nascimento: "))


import datetime

hoje = datetime.date.today()
anoAtual = hoje.year


calculoIdade = anoAtual - anoNascimento

print(f"A sua idade atualmente é: {calculoIdade}");