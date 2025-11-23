# Lista de Exercícios – Match / Case (Python)

## Objetivo

Praticar estruturas de decisão usando **match / case** (equivalente ao switch case) introduzido no Python 3.10.

## Exercícios

1. **Exercício 01 – Dia da semana**
   Leia um número de 1 a 7 e use `match` para exibir o dia correspondente (1 = Domingo, 2 = Segunda...).

2. **Exercício 02 – Operações matemáticas**
   Leia dois números e uma operação (`+`, `-`, `*`, `/`) e use `match` para executar a operação correta.

3. **Exercício 03 – Classificação de notas**
   Leia uma nota de 0 a 10 e exiba:

   * `A` (8–10)
   * `B` (6–7.9)
   * `C` (4–5.9)
   * `D` (0–3.9)

4. **Exercício 04 – Tipo de animal**
   Leia o nome de um animal e classifique:

   * "cachorro" ou "gato" → **Mamífero**
   * "cobra" ou "lagarto" → **Réptil**
   * "sapo" → **Anfíbio**
     Se não estiver na lista, exibir **"Animal não identificado"**.

5. **Exercício 05 – Menu de um sistema**
   Mostre opções:

   1. Cadastrar
   2. Listar
   3. Excluir
      Use `match` para exibir qual ação a pessoa escolheu.

6. **Exercício 06 – Classificação de veículo pela placa**
   Pergunte a última letra da placa e exiba:

   * `A` ou `B` → **Rodízio segunda**
   * `C` ou `D` → **Rodízio terça**
   * `E` ou `F` → **Rodízio quarta**
   * etc.

7. **Exercício 07 – Turno escolar**
   Leia `M`, `V` ou `N` e exiba:

   * `M` → **Matutino**
   * `V` → **Vespertino**
   * `N` → **Noturno**
     Caso contrário, informar **inválido**.

8. **Exercício 08 - Mês do ano**
   Leia um número de 1 a 12 e exiba o nome do mês.

9. **Exercício 09 – Conversão de temperaturas**
   Pergunte qual conversão deseja:

   * 1 → Celsius → Fahrenheit
   * 2 → Fahrenheit → Celsius
     Use `match` para identificar a escolha.

10. **Exercício 10 – Tipos de usuário**
    Leia um código de usuário:

    * `1` → Administrador
    * `2` → Usuário comum
    * `3` → Visitante
      Caso contrário, exibir **Código inválido**.
