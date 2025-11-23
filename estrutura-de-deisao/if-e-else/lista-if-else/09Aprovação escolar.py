#   Leia a média final de um aluno:  
#   - Se média < 5 → `"Reprovado"`  
#   - Se média entre 5 e 6.9 → `"Recuperação"`  
#   - Se média ≥ 7 → `"Aprovado"`

nota = float(input("Informe a nota do aluno: "))

if nota < 0 :
    print("Informe uma nota válida!")
elif nota >= 0 and nota < 5 :
    print("REPROVADO")
elif nota >= 5 and nota <= 6.9 :
    print("RECUPERAÇÃO")
elif nota <= 10 and nota >= 7 :
    print("APROVADO")
else :
    print("Informe uma nota válida!")