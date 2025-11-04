from random import randint
computador = randint(1, 50)
usuario =int(input('Digite um número: ')) 
contador = 1
while usuario != computador:
    contador = contador + 1
    
    
    if usuario > computador:
        print('NÚMERO ALTO. Tente novamente')
    else:
        print('NÚMERO BAIXO. Tente novamente')
    usuario = int(input('Digite um número: '))
print('PARABÉNS. VOCÊ ACERTOU')



