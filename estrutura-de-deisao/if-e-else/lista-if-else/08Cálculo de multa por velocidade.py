#   Leia a velocidade de um carro.  
#   Se for maior que 80 km/h, mostre:  
#   `"Você foi multado! Valor da multa: R$ X"`  
#   (R$ 7 por km acima do limite).  
#   Caso contrário, imprima `"Dentro do limite"`.

velocidade = float(input("Informe a velocidade do seu carro: "))
limite = 80

if velocidade > limite :
    kmAcima = velocidade - limite
    multa = kmAcima * 7
    print(f"Você foi multado! Valor da multa: R$ {multa:.2f}")
else :
    print("Dentro do limite")