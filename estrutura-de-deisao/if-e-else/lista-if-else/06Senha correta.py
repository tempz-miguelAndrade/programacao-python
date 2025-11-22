#   Peça ao usuário que digite uma senha.  
#   Se a senha for `"1234"`, escreva `"ACESSO PERMITIDO"`.  
#   Caso contrário, `"ACESSO NEGADO"`.

senha = int(input("Informe um senha: "))

if senha == 1234 :
    print("Acesso PERMITIDO!")
else : 
    print("Acesso NEGADO!")