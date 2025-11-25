## Estruturas de Repetição em Python

As estruturas de repetição permitem executar um bloco de código várias vezes, de forma automática. Elas são fundamentais para resolver problemas que envolvem contagem, repetição de tarefas e processamento de listas.

Neste módulo você vai aprender:

O que são estruturas de repetição

Quais estruturas existem no Python

Como usar while e for

Como controlar o fluxo com break, continue e pass

Exemplos práticos

## O que é uma estrutura de repetição?

Uma estrutura de repetição (ou loop) é um comando que executa um trecho de código diversas vezes, enquanto uma condição é verdadeira ou para cada item em uma sequência.

## Tipos de repetição no Python

O Python possui dois tipos principais de loops:

#### 1. while: repete enquanto a condição é verdadeira

O loop while é ideal quando não sabemos exatamente quantas vezes vamos repetir.



Sintaxe

while condição:
    instruções


#### 2. for: repete para cada item de uma sequência

Usamos for quando já sabemos o número de repetições ou quando estamos percorrendo listas, textos ou intervalos.
Exemplo


###### Sintaxe

for variável in sequência:
    instruções




###### Exemplo com range()

for i in range(1, 6):
    print(i)



### Comandos de Controle do Loop
break — encerra o loop imediatamente

for i in range(10):
    if i == 5:
        break
    print(i)



###### continue — pula para a próxima repetição

for i in range(6):
    if i % 2 == 0:
        continue
    print(i)




###### pass — não faz nada (placeholder)

for i in range(3):
    pass




## Exercícios desta pasta

Nesta pasta você encontrará exercícios envolvendo:

Repetição com while

Repetição com for

Uso de range()

Contadores e acumuladores

Comandos break e continue

Validações usando repetição