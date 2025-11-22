# Leia três notas informadas pelo usuário e calcule a média.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

notaTotal = nota1 + nota2 + nota3
media = notaTotal / 3

print(f"a nota com a média aplicada é de: {media:.1f}")