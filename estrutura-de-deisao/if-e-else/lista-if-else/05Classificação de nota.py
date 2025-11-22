#   Leia uma nota de 0 a 10 e imprima:
#   - `"Muito ruim"` para notas abaixo de 4  
#   - `"Ruim"` entre 4 e 5.9  
#   - `"Bom"` entre 6 e 7.9  
#   - `"Ótimo"` entre 8 e 10

nota = float(input("Informe uma nota: "))


if nota < 0 :
    print("A nota deve ser positivo!")
elif nota < 4 :
    print("Muito ruim!")
elif nota >= 4 and nota <= 5.9 :
    print("Ruim!")
elif nota >= 6 and nota <= 7.9 :
    print("Bom!")
elif nota >= 8 and nota <= 10 :
    print("ótima!")
else :
    print("Perfeita!")