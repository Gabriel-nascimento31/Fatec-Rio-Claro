preço = float(input('Digite o preço do produto: R$ '))
desconto = preço - (preço * 10 / 100)
print(f'O preço do produto com 10% de desconto ficará a R${desconto:.2f} ')
