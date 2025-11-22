# Receba uma temperatura em Celsius e converta para Fahrenheit.

celsius = float(input("informe uma temperatura em celsius: "))


conversao = (celsius * 9/5) + 32 
conversaoArredondado = round(conversao, 1)

print(f"a temperatura informada em celsius é {conversaoArredondado:.1f} graus F°")