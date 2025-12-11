produtos = {}
for p in range(5):
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    produtos[produto] = preco
print(produtos)
maximo = max(produtos, key=produtos.get)
print(f'O produto mais caro é  {maximo}')

