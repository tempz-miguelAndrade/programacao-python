# Leia uma lista de números e determine qual é o maior usando apenas for.

lista = [1, 2, 3, 4, 5]

maior = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

print(f"O maior número da lista {lista} é: {maior}")