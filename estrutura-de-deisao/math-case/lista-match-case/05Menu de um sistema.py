#   Mostre opções:
#   1. Cadastrar
#   2. Listar
#   3. Excluir
#      Use `match` para exibir qual ação a pessoa escolheu.

opcao = input(
    "Escolha uma das opções:\n" \
    "1.Cadastrar\n" \
    "2.Listar\n" \
    "3.Excluir\n" \
    ":"
    ).lower()

match opcao:
    case _ if opcao == "1" or opcao == "cadastrar":
        print("Você se cadastrou!")
    case _ if opcao == "2" or opcao == "listar":
        print("Você listou!")
    case _ if opcao == "3" or opcao == "excluir":
        print("Você excluio!")
    case _:
        print("Opção inválida!")