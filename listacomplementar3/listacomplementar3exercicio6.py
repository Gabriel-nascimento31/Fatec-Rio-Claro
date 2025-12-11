idade = int(input('Digite a sua idade: '))
if idade < 6:
    print('Idade inválida! ')
elif idade <= 10:
    print('Lobinho ')
elif idade <= 14:
    print('Escoteiro ')
elif idade <= 17:
    print('Sênior ')
elif idade <= 21:
    print('Pioneiro ')
else:
    print('Líder ')
