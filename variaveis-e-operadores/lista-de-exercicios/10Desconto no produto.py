# Receba o valor de um produto e calcule o preço final com 10% de descont0

produto= float(input("Informe o valor de um produto: "))

desconto = 10
valorFinal = produto - ( produto * ( 10 / 100 ))

print(f"O valor do produto com o desconto aplicado, foi de: {valorFinal:.2f}")

