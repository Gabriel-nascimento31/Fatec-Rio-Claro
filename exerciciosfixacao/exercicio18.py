usuario = str(input('Usuário: '))
senha = str(input('Senha: '))
u = 'maracuja30'
s = 'maracuja123'
if usuario != u or senha != s:
    for i in range(2):
        print('Usuário e/ou senha incorretos! Tente novamente! ')
        usuario = str(input('Usuário: '))
        senha = str(input('Senha: '))
        if usuario == u and senha == s: 
            print('ACESSO PERMITIDO')
            break
    else:
        print('Seu acesso foi bloqueado')
else:
    print('ACESSO PERMITIDO')
    










