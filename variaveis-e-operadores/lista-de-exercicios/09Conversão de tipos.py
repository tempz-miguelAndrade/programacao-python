#Leia um valor como string e mostre:  
# - Em letras maiúsculas  
# - Em letras minúsculas  
# - Quantos caracteres tem

valor = input("Infome uma palavra: ")

print(f"A palavra em letra maiúsculas: {valor.upper()}\nE em minúsculo: {valor.lower()}\nE a quantidade de caracteres é de: {len(valor)}")