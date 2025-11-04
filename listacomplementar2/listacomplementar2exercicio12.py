senha = 'jaboticaba123'
for s in range(3):
    usuario = input('Digite a senha: ')
    if usuario == senha:
        print('ACESSO PERMITIDO! ')
        break
    else:
        print('Senha incorreta! Tente novamente! ')
else:
    print('Seu acesso foi bloqueado! ')
    