idade = int(input('Digite a sua idade: '))
if idade < 14:
    print('Você não pode entrar na festa! ')
elif idade < 18:
    print('Você só pode entrar na festa com o acompanhamento de seus pais! ')
    print('Não pode beber! ')
elif idade >= 18:
    print('Você pode entrar na festa! ')
    print('Pode beber! ')
