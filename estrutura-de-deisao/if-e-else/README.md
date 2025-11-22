# Estruturas de Decisão – if / else (Python)

## Objetivo  
Neste exercício você irá praticar o uso das estruturas de decisão em Python: `if`, `else` e `elif`.  
O foco está em usar corretamente expressões condicionais, comparações lógicas, e ramificar o fluxo de execução do programa conforme diferentes cenários.

## Conteúdo  
Você vai trabalhar com os seguintes conceitos:  
- Comparadores: `==`, `!=`, `<`, `>`, `<=`, `>=`  
- Operadores lógicos: `and`, `or`, `not`  
- Estrutura básica de decisão:  
  ```python
  if condição:
      bloco_verdadeiro
  else:
      bloco_falso

**Usando elif**
if condição1:
    …
elif condição2:
    …
else:
    …


# exemplo simples: verificar se o número é par ou ímpar
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é **par**.")
else:
    print(f"O número {numero} é **ímpar**.")


# exemplo com múltiplas condições: faixa etária
idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("Você é criança.")
elif idade < 20:
    print("Você é adolescente.")
else:
    print("Você é adulto ou idoso.")
    