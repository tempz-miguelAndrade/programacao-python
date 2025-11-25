# Leia uma palavra e conte quantas vogais ela possui (a, e, i, o, u).

palavra = input("Informe uma palavra: ").lower()

contador = 0

for vogal in palavra :
    vogais = "aeiou"
    if vogal in vogais:
        contador += 1


print(f"As quantidade de vogais achadas da palavra {palavra}, foi de: {contador}")