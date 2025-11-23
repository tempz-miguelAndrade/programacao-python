#   Leia a média final de um aluno e imprima:
#   * "Reprovado" se média < 5
#   * "Recuperação" se estiver entre 5 e 6.9
#   * "Aprovado" se média ≥ 7
#     Use ternários aninhados.

nota = float(input("Iforme sua nota: "))

resultado = "Informe uma nota válida!" if nota < 0 or nota > 10 else "Reprovado" if nota < 5 else "Recuperação" if nota >= 5 and nota <= 6.9 else "Aprovado"

print(resultado)