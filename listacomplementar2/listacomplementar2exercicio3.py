preços = float(input('Digite o preço do produto, caso contrário digite 0 para sair: '))
contador = preços
while preços != 0:
    preços = float(input('Digite o preço do produto, caso contrário digite 0 para sair: '))
    contador = contador + preços
print(f'R${contador:.2f}')



if contador > 100:
    print('Você terá 10% de desconto na sua compra ')
    desconto = contador - (contador * 10 / 100)
    print(f'Sua compra com o desconto ficará R${desconto:.2f} ')
else:
    print('Você não terá desconto na sua compra ')
