# Estruturas de Decisão – Python

As estruturas de decisão permitem que um programa tome diferentes caminhos de execução dependendo de condições. Elas são usadas para **avaliar expressões** e **executar blocos de código específicos** conforme o resultado da análise lógica.

Em Python, as principais estruturas de decisão são:
`if`, `elif`, `else` e `match-case`.

---

## 1. `if`

A estrutura `if` é usada para testar uma condição.
Quando a condição é verdadeira, o bloco interno é executado.

É sempre a **primeira condição** a ser verificada.

---

## 2. `elif`

O `elif` é verificado somente quando o `if` não for verdadeiro.
Ele serve para testar novas condições sem abrir um novo `if`.

Podemos ter quantos `elif` forem necessários.

---

## 3. `else`

O `else` é executado quando **nenhuma das condições anteriores** é verdadeira.
Ele **não recebe condição**.

Deve ser sempre o **último bloco** da estrutura.

---

## 4. `match-case`

O `match-case` é usado quando queremos comparar um valor fixo com várias possibilidades específicas.

Funciona como um “menu de escolhas”.

É útil para decisões baseadas em uma única variável, como:

* opções de menu
* códigos pré-definidos
* números específicos
* comandos simples

Além disso, o `match` permite usar condicionais dentro do `case`, como:

* `case _ if condição:`

Esse formato amplia a flexibilidade do `match`, tornando possível testar faixas, intervalos e regras especiais.

---

# Operadores Lógicos

Operadores lógicos são usados para combinar condições dentro das estruturas de decisão.

## `and`

As duas condições precisam ser verdadeiras para que o resultado seja verdadeiro.

## `or`

Apenas uma das condições precisa ser verdadeira.

## `not`

Inverte o valor lógico:

* `not True` → False
* `not False` → True

Esses operadores são fundamentais para validar dados, criar filtros e montar expressões mais complexas dentro de `if`, `elif` ou até mesmo dentro de `case _ if`.

---

# Operadores Bitwise (não usados como operadores lógicos)

Python também possui operadores que se parecem com operadores lógicos, mas não servem para lógica condicional.

* `&` → operação bit a bit, **não é** `and`
* `|` → operação bit a bit, **não é** `or`
* `~` → operação bit a bit, **não é** `not`

Eles funcionam sobre bits, não sobre lógica booleana.

Qualquer funcionamento “aparente” quando usados com True/False é apenas consequência da representação interna desses valores — **não substituem operadores lógicos**.
