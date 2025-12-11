nomes = []
for c in range(5):
    nome = input('Digite um nome:')
    nomes.append(nome)
    
nome_mais_longo = max(nomes, key=len)

print(f'O nome mais longo é {nome_mais_longo}')
print(f'Ele tem {len(nome_mais_longo)} caracteres')



