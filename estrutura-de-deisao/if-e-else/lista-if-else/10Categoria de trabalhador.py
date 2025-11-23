#    Leia a idade e exiba:  
#    - `"Jovem aprendiz"` se idade < 18  
#    - `"Trabalhador adulto"` se idade entre 18 e 59  
#    - `"Aposentado"` se idade ≥ 60

idade = int(input("Informe sua idade: "))

if idade <= 13 :
    print("Sem idade para trabalhar!")
elif idade >= 14 and idade < 18 :
    print("Jovem Aprendiz")
elif idade >= 18 and idade <= 59 :
    print("Trabalhador")
else :
    print("Aposentado")