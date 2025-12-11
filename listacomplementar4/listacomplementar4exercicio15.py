senha = '123mudar'
tentativas = 1
while True:
    usuario = input('Digite a senha: ')
    if usuario != senha:
        print('SENHA INCORRETA! TENTE NOVAMENTE! ')
        tentativas = tentativas + 1
        
    else:
        print('ACESSO PERMITIDO!')
        break
print(f'Foram necessárias {tentativas} tentativas para conseguir o acesso')




