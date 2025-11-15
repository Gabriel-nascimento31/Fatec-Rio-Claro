compra = float(input('Digite o valor da sua compra: '))
if compra > 100:
    print('Seu frete é grátis! ')
else:
    frete = compra + 15
    print('Você terá uma taxa de R$15,00 de frete, portanto sua compra ficará R${:.2f}' .format(frete))
