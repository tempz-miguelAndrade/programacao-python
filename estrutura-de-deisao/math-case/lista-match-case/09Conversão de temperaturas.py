#   Pergunte qual conversão deseja:
#   * 1 → Celsius → Fahrenheit
#   * 2 → Fahrenheit → Celsius
#     Use `match` para identificar a escolha.

conversao = input("Qual conversão você deseja?(1.celsius para fahrenheit ou 2.fahrenheit para celsius)\n:").lower()

match conversao:
    case _ if conversao == "1" or conversao == "celsius para fahrenheit":
        celsius = float(input("Informe a temperatura em celsius: "))
        calculo = (celsius * 9/5) + 32
        print(f"Os {celsius:.1f}C° em fahrenheit é: {calculo:.1f}F°")

    case _ if conversao == "2" or conversao == "fahrenheit para celsius":
        fahrenheit = float(input("Informe a temperatura em fahrenheit: "))
        calculo = (fahrenheit - 32) * 5/9
        print(f"Os {fahrenheit:.1f}F° em celsius é: {calculo:.1f}C°")

    case _:
        print("Informações inválidas!")
