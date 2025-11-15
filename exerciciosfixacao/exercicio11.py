from random import randint
computador = randint(1, 10)
usuario = int(input('Tente adivinhar o número que estou pensando entre 1 e 10: '))
if usuario > computador:
    print('MUITO ALTO! ')
elif usuario < computador:
    print('MUITO BAIXO! ')
else:
    print('PARABÉNS! ')

    