from random import randint
computador = randint(1, 100)

for g in range(5):
    jogador = int(input('Digite um número entre 1 e 100: '))
    if jogador == computador:
        print('PARABÉNS! VOCÊ VENCEU! ') 
        break
    else:
        print('Número não sorteado! Tente novamente! ')

else:
    print('VOCÊ PERDEU! ')
    



    
        
        

    
    